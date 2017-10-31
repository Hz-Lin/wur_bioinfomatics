#import modules we need
# library to convert from json to a dictionary/list complex data structure
import json
# for plot a histogram at the end of the script.
import matplotlib.pyplot as plt
# %matplotlib inline

# This subroutine can plot a histogram of all ages found for your favorite Dino
def plot_age_histogram(list_of_ages,favoritedino,numbins=100,youngest=65,oldest=220,histcolor='green'):
    # set up the plot
    plt.figure(figsize = (4,3))
    # plot histogram elements
    plt.hist(list_of_ages,bins=numbins,range=(youngest,oldest),color=histcolor)
    # add a title
    plt.title(favoritedino)
    # plot x and y axis labels
    plt.xlabel("Age, millions of years")
    plt.ylabel("Number of finds")
    # some customization
    plt.tight_layout() # supply as default - will prevent axis labels to fall off
    # We also want something more durable than a print on screen: print to jpg!
    plt.savefig(favoritedino+'.jpg',dpi=300) 
    # This you will always need to plot to screen
    plt.show()

# choose your favorite dinosaur
myfavoritedino = 'Stegosaurus'

# read file and creat a nesting data stucture called din_dict
filename = 'Dinosaurs.json'
fh = open(filename,'r')
din_json = fh.read()
fh.close()
din_dict = json.loads(din_json)

import argparse
parser = argparse.ArgumentParser(description='Simple analysis of PaleoDB and JSON formats')
parser.add_argument("-f", "--filename", help="PaleoDB file in JSON", type = str, required = True)
parser.add_argument("-d", "--dino", help="favorite dinosaur genus - case sensitive!", type = str, required = True)

args = parser.parse_args()

filename = args.filename
myfavoritedino = args.dino


# extract the records from the dictionary
records = din_dict['records']
counter = 0
list_of_ages = list()
for record in records:
    if 'gnl' in record.keys() and myfavoritedino == record['gnl']:
        # (max) age of fossil
        age_max = record['eag']
        # latitude 
        latitude = record['lat']
        # longitude 
        longitude = record['lng']
        # species name
        species_name = record['tna']
        # in this list we keep all the ages of finds of your favorite dinosaur.
        list_of_ages.append(age_max)   
        # the counter keeps track of the number of finds of your favorite dinosaur
        # This is necessary because the placemarks in the KML need to have a uniqe id!
        counter +=1
# plot the histogram. Pass on list_of_age and myfavoritedinosaur to the function, in the correct order.
plot_age_histogram(list_of_ages,myfavoritedino,numbins=100,youngest=65,oldest=220,histcolor='green')