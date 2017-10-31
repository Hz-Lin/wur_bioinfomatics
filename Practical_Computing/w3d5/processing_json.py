#file Trex_reduced.json should be in the same folder as this script
INFILENAME = 'Trex_reduced.json'

#inport module json
import json

#get the json file into memory
infile = open(INFILENAME, 'r')
#read the entire file into one string
trex_json = infile.read()
infile.close()

#use module json do the parsing
#it produces a python object that contains all data as found in the string from of the Json file
trex = json.loads(trex_json)
del trex_json

#extract the real data
data = trex['records']

for i in range(len(data)):
    record = data[i]
    print 'latitude = %8.3f   longitude = %8.3f' % (record['lat'], record['lng'])