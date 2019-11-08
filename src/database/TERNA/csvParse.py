""" The parse has to convert the input CSV into a JSON file in order to load it on a 
     MongoDB DataBase 
"""
import sys
import json
import pandas as pd 
from collections import defaultdict, Counter, OrderedDict

#read csv from a path
df_csv = pd.read_csv("/Users/gianpiodomiziani/Desktop/data.csv",
                     sep=";",
                     skiprows=(lambda x: x in [0]),
                     header=None,
                     index_col=False
                    )
#convert the CSV into a json, then into a dictionary with the structure: 
#orient=‘split’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}

data_json =json.loads(df_csv.to_json(orient='split'))
#takes only the data values, where each value is: (MM/DD/YY H, point), where point is the values 
#of the specific physical quantity
data = data_json['data']

start = data[1][0] #data start
end = data[len(data)-1][0] #data end
#makes a dict with key: DD/MM/YY H, value=point
data_dict = {key: value for key,value in data}

"""
TO DO LIST: data from Terna are all different because them aren't all same physical quantity 
(from MGE we get only price quantity) so each type of physical quantity has to be 
processed separately. For instance, to build the load curve, it takes several point 
for each hour, even worse, the data of Generation are the amount of energy producted with each
different energy source. So, for each hour, here we have six values one for each energy source.

"""

