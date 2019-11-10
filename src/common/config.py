import os

# ======================================
# SPIDERS
# ======================================

# Hide the Firefox window when automating with selenium
os.environ['MOZ_HEADLESS'] = '1'

# GME urls
DOWNLOAD = '/home/luca/Codes/smartgrids/downloads'
RESTRICTION = 'https://www.mercatoelettrico.org/It/Download/DownloadDati.aspx'
GME = [
	{
		'fname':'MGP_PrezziConvenzionali',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_PrezziConvenzionali'
	},
	{
		'fname':'MGP_LimitiTransito',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_LimitiTransito'
	},
	{
		'fname':'MGP_StimeFabbisogno',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_StimeFabbisogno'
	},
	{
		'fname':'MGP_Prezzi',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_Prezzi'
	},
	{
		'fname':'MGP_OfferteIntegrativeGrtn',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_OfferteIntegrativeGrtn'
	},
	{
		'fname':'MGP_Fabbisogno',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_Fabbisogno'
	},
	{
		'fname':'MGP_Transiti',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_Transiti'
	},
	{
		'fname':'MGP_Liquidita',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_Liquidita'
	},
	{
		'fname':'MGP_Quantita',
		'url':'https://www.mercatoelettrico.org/It/download/DownloadDati.aspx?val=MGP_Quantita'
	}
]

# GME data interval
INTER_DATA_GME = 86400 #24h

# Dynamic file history
HISTORY=[]

#EntsoeLoad

#auth credits

USERNAME = "s267534@studenti.polito.it"
PASSWORD = "SmartGridProject!"
LOGIN_URL = f"https://transparency.entsoe.eu/login?&username={USERNAME}&password={PASSWORD}" # f--> permette di aggiungere {}

list_dataItem = ['ACTUAL_TOTAL_LOAD',
				 'DAY_AHEAD_TOTAL_LOAD_FORECAST']
list_exportType= ['XML',
				  'CSV']
list_areaType=['CTA',
			   'BZN',
			   'CTY']
list_biddingZone={
						'Brindisi':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A69',
						'Centre-North':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A70O',
						'Centre-South':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A71M',
						'Foggia':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A72K',
						'GR':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A66F',
						'Malta':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A877',
						'North':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A73I',   #there are 8 different subregions
						'Sardinia':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A74G',
						'Sicily':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A75',
						'South':'CTY%7C10YIT-GRTN-----B!BZN%7C10Y1001A1001A788'
}


