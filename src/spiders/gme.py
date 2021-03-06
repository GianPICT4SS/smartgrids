import sys
import os
import time
import requests as req
from src.common.config import *
from src.loggerbot.bot import bot
from zipfile import ZipFile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sys.dont_write_bytecode = True

class GMESpider():
	"""Description

	Parameters
	----------
		log : logging.logger
			logger instalnce to display and save logs
	
	Attributes
	----------
		driver : selenium.webdriver.firefox.webdriver.WebDriver
			selenium instance creating a Firefox web driver
		log : logging.logger
			logger instalnce to display and save logs
	
	Methods
	-------
		passRestrictions()
		getData(gme, start, end)
		getFname(fname, start, end)
		checkDownload(fname)
		unzip(fname)
		updateHistory(flist)
	"""
	def __init__(self, log):
		# Set the firefox profile preferences
		profile = webdriver.FirefoxProfile()
		profile.set_preference("browser.download.folderList", 2)
		profile.set_preference("browser.helperApps.alwaysAsk.force", False)
		profile.set_preference("browser.download.manager.showWhenStarting",False)
		profile.set_preference("browser.download.dir", DOWNLOAD)
		profile.set_preference("browser.download.downloadDir", DOWNLOAD)
		profile.set_preference("browser.download.defaultFolder", DOWNLOAD)
		profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/html")
		
		# Class init
		self.driver = webdriver.Firefox(profile, log_path='logs/geckodrivers.log')
		self.driver.set_page_load_timeout(15)
		self.log = log
		self.passRestrictions()
	
		
	def passRestrictions(self):
		"""At the beginning of each session the GME website requires the flag and the submission
		of the Terms and Conditions agreement. Selenium emulate the user's click and passes this
		restrictions.
		"""
		connected = False
		restarted = False
		while not connected:
			try:
				self.driver.get(RESTRICTION)
				connected = True
				
				# Bot Notifications
				if restarted:
					try:
						bot('WARNING', 'GME', 'Connection is up again.')
						restarted = False
					except:
						pass
					
			except:
				self.log.error("GME connection failed. Trying again.")
				restarted = True
				time.sleep(5)

		# Flag the Agreement checkboxes
		_input = self.driver.find_element_by_id('ContentPlaceHolder1_CBAccetto1')
		_input.click()
		_input = self.driver.find_element_by_id('ContentPlaceHolder1_CBAccetto2')
		_input.click()
		# Submit the agreements
		_input = self.driver.find_element_by_id('ContentPlaceHolder1_Button1')
		_input.click()
		self.log.info("Agreements passed")
	
		
	def getData(self, gme, start, end):
		"""Insert the starting and ending date of data and download them by emulating the 
		user's click. After the download in the 'downloads/' folder, the file is checked.
		If the download failed, it is tried again.

		Parameters
		----------
			gme : dict
				GME url to retrieve data and name of the downloaded file without extension
			start : str
				starting date data are refearred to
			end : str
				ending date data are refearred to

		"""
		downloaded = False
		restarted = False
		while not downloaded:
			try:
				self.log.info("Retrieving data:\n\t{}\n\t{} - {}".format(gme['fname'], start, end))
				self.driver.get(gme['url'])
				# Set the starting and endig date.
				# The GME has the one-month restriction
				_input = self.driver.find_element_by_id('ContentPlaceHolder1_tbDataStart')
				_input.send_keys(start)
				_input = self.driver.find_element_by_id('ContentPlaceHolder1_tbDataStop')
				_input.send_keys(end)
				
				# Download file
				_input = self.driver.find_element_by_id('ContentPlaceHolder1_btnScarica')
				_input.click()
				
				# Check if download succeded
				downloaded = self.checkDownload(
					self.getFname(gme['fname'], start, end)
				)

				# Bot Notifications
				if downloaded and restarted:
					try:
						bot('WARNING', 'GME', 'Connection is up again.')
						restarted = False
					except:
						pass
			except:
				self.log.warning('Trying again...')
				restarted = True
				time.sleep(5)
	
		
	def getFname(self, fname, start, end):
		"""Build the downloaded zipped file name on the basis of the starting and 
		ending date.

		Parameters
		----------
			fname : str
				file name without extension retrieved by the dict. 
				in the config. file
			start : str
				starting date data are refearred to
			end : str
				ending date data are refearred to

		Returns
		-------
			str
				zipped file name
		"""
		dds,mms,yys = start.split("/")
		dde,mme,yye = end.split("/")
		period = yys+mms+dds+yye+mme+dde
		fname += period
		fname += '.zip'
		
		return fname
	
	
	def checkDownload(self, fname):
		"""Check if the file has been downloaded into the 'downloads/' folder.

		Parameters
		----------
			fname : str
				name of the downloaded file

		Returns
		-------
			bool
				True if the file has been downloaded, False otherwise
		"""
		if os.path.isfile(DOWNLOAD+'/'+fname):
			self.log.info("Zip file downloaded".format(fname))
			self.unZip(fname)
			
			return True
		else:
			self.log.error("{} download failed".format(fname))
			
			# Bot Notifications
			try:
				bot('ERROR', 'GME', 'Download failed.')
			except:
				pass

			return False
	
	
	def unZip(self, fname):
		"""Unzip the downloaded files and remove the zipped one from the folder.

		Parameters
		----------
			fname : str
				.zip file name
		"""
		unzipped = False
		while not unzipped:
			try:
				with ZipFile(DOWNLOAD+'/'+fname, 'r') as zip:  
					# extracting all the files 
					self.log.info("Extracting data...") 
					zip.extractall(DOWNLOAD) 
					self.log.info("Data extracted") 
			
				os.remove(DOWNLOAD+'/'+fname)
				unzipped = True
			
			except:	
				self.log.error(f"{fname} not found. Trying again...")
				
				# Bot Notifications
				try:
					bot('ERROR', 'GME', 'Unzip failed.')
				except:
					pass

				time.sleep(5)