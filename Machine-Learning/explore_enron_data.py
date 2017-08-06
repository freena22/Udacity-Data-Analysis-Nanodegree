""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
    Enron Case involved in:
    1. Selling assets to shell companies a the end of each month, and buying them back at the
       beginning of the next month to hide accounting losses
    2. Causing electrical grid failures in California
    3. A plan in collaboration with Blockbuster movies to stream movies over the Internet
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print(len(enron_data)) # -》 146

# for each person, 21 features are available

for keys, values in enron_data.items():
	if values["salary"] == 10529459:
		print(keys)

# -> 18 (18 POIs are in the dataset, but 35 POIs were in total)
'''
print(enron_data["PRENTICE JAMES"]["total_stock_value"]) # -> 1095040
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]) # -> 11
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options']) # -> 19250000

print(enron_data['LAY KENNETH L']['total_payments'])
# -> Founder, Chairman 103559793
print(enron_data['SKILLING JEFFREY K']['total_payments'])
# -> CEO 8682716
print(enron_data['FASTOW ANDREW S']['total_payments'])
# -> CFO 2424083
num = 0
for keys, values in enron_data.items():
    if values["salary"] != "NaN":
        num += 1
print(num) # -> 98
'''
