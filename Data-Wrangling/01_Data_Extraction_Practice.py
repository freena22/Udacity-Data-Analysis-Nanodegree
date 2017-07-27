## Parsing CSV Files

# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!

import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
    	header = f.readline().split(',')
    	# header use as keys for each one of the data items
    	# readline() reads one entire line from the file
    	counter = 0
    	for line in f:
    		if counter == 10:
    			break

    		fields = line.split(',')
    		entry = {}
    		for i, value in enumerate(fields):
    			entry[header[i].strip()] = value.strip()
    			# strip() will get rid of the extra whitespace 

    		data.append(entry)
    		counter += 1

    	return data

print(parse_file(DATAFILE))

# emumerate()

fields = ['a','b','c','d','e']
entry = {}
for i, value in enumerate(fields):
	entry[i] = value
print(entry)

# -> {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

# ->
#[{'Title': 'Please Please Me', 'Released': '22 March 1963', 'Label': 'Parlophone(UK)'}, 
# {'Title': 'With the Beatles', 'Released': '22 November 1963', 'Label': 'Parlophone(UK)'}
#]


# Whenever you're working with CSV files, it's best to use CSV module to deal with the problems

import os
import pprint
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_csv(datafile):
	data = []
	n = 0
	with open(datafile,'r') as sd:
		r = csv.DictReader(sd)
		for line in r:
			data.append(line)
	return data 

if __name__ == '__main__':  # for print out
	datafile = os.path.join(DATADIR,DATAFILE)
	parse_csv(datafile)
	d = parse_csv(datafile)
	pprint.pprint(d)

''' Output:
[OrderedDict([('Title', 'Please Please Me'),
              ('Released', '22 March 1963'),
              ('Label', 'Parlophone(UK)'),
              ('UK Chart Position', '1'),
              ('US Chart Position', '-'),
              ('BPI Certification', 'Gold'),
              ('RIAA Certification', 'Platinum')]),
 OrderedDict([('Title', 'With the Beatles'),
              ('Released', '22 November 1963'),
              ('Label', 'Parlophone(UK)'),
              ('UK Chart Position', '1'),
              ('US Chart Position', '-'),
              ('BPI Certification', 'Platinum'),
              ('RIAA Certification', 'Gold')]),
'''

