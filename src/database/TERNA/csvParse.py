""" The parse has to convert the input CSV into a JSON file in order to load it on a 
     MongoDB DataBase 
"""
import json
import pandas as pd
import logging


class ParseCsv:
    """A Parse class used to parse CSV file into json file for processing them on a MongoDB.

    Attributes
    ----------
        target : str
            the type of files to process ('history' or 'daily')
        log : logging.logger
            logger instance to display and save logs
        db : pymongo.database.Database
            the database to use

    Methods
    -------

        read_csv()
        to_list()
        to_dict()


    """

    @staticmethod
    def read_csv(path, sep=';', header=None, index_col=None, skiprows=None):

        """
        reads a csv, located in a specific path, transforming it into a pandas.Dataframe

         :param path: str, path csv path
         :param skiprows: list-like, int or callable, optional. Line numbers to skip (0-indexed) or number of lines
                    to skip (int) at the start of the file.
         :param index_col: int, str, list of int/str; default None, Column(s) to use as the row labels of the
                    DataFrame, either given as string name or column index.
         :param sep: str, default ';'
         :param header: nt, list of int, Row number(s) to use as the column names, and the start of the data

        """
        # read csv from a path
        try:
            df_csv = pd.read_csv(filepath_or_buffer=path, sep=sep, header=header, index_col=index_col, skiprows=skiprows)
            return df_csv
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)



    @staticmethod
    def to_list(df_csv):
        """ Converts a CSV DataFrame into a list: useful for doing some operation before to build the JSON file
        :parameter df_csv = a CSV DataFrame

        :return data = list
        """

        # orient=‘split’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}
        try:
            data_json = json.loads(df_csv.to_json(orient='split'))
            # takes only the data values of the specific physical quantity
            data = data_json['data']
            if data[0] == (None, None):
                del data[0]
            return data
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)



    @staticmethod
    def to_dict(data):
        """ Converts a list of data into a dictionary """

        data_dict = {key: value for key, value in data}
        return data_dict



"""
TO DO LIST: data from Terna are all different because them aren't all same physical quantity 
(from MGE we get only price quantity) so each type of physical quantity has to be 
processed separately. For instance, to build the load curve, it takes several point 
for each hour, even worse, the data of Generation are the amount of energy producted with each
different energy source. So, for each hour, here we have six values one for each energy source.

"""

