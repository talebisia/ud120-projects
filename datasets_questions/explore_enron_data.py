#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# for key in enron_data:
#     print(key)
#
# var = len({k: v for k, v in enron_data.items() if v["poi"] == 1})
# print (var)

# print (enron_data["PRENTICE JAMES"]["total_stock_value"])

# print (enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# print (enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
# print (enron_data["LAY KENNETH L"]["total_payments"])
# print (enron_data["FASTOW ANDREW S"]["exercised_stock_options"])

# var = len({k: v for k, v in enron_data.items() if v["salary"] != "NaN"})
# var = len({k: v for k, v in enron_data.items() if v["salary"] != "NaN"})
# print (var)

# var = len({k: v for k, v in enron_data.items() if v["total_payments"] == "NaN"})
# var1 = {k: v for k, v in enron_data.items() if v["total_payments"] == "NaN"}
# print (var)
# print (var1)
# print ("people in the entire datset = " + str(len(enron_data.items())))

# var = {k: v for k, v in enron_data.items() if v["total_payments"] == "NaN" and v["poi"] == True}
# var1 = len({k: v for k, v in enron_data.items() if v["total_payments"] == "NaN" and v["poi"] == True})
# print (var)
# print (var1)


var = len({k: v for k, v in enron_data.items() if v["poi"] == True})
var1 = {k: v for k, v in enron_data.items() if v["poi"] == True}
print (var)
print (var1)
print ("people in the entire datset = " + str(len(enron_data.items())))



