#import modules we need
# library to convert from json to a dictionary/list complex data structure
import json
# for plot a histogram at the end of the script.
import matplotlib.pyplot as plt
# %matplotlib inline

# creat functions for writing the KML file
# Write required first line
def write_kml_start(kmlfh):
    # mandatory start of KML
    kmlfh.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    kmlfh.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    kmlfh.write('<Document>\n')
    
# Write the required last lines of the KML, and close filehandle
def write_kml_end(kmlfh):
    # mandatory end of KML
    kmlfh.write('</Document>\n</kml>')

# This little subroutine writes one 'placemark' in a KML file 
def write_placemark_in_kml(kmlfh, dinoname,counter,species,age,latitude, longitude):
    # written for each placemark; Point data added dynamically.
    kmlfh.write('  <Placemark>\n')
    kmlfh.write('    <name>%s</name>\n' % (dinoname+'_'+str(counter)))
    kmlfh.write('    <description>%s</description>\n' % (species+', '+str(age)+' MA'))
    kmlfh.write('    <Point>\n')
    kmlfh.write('       <coordinates>%s,%s</coordinates>\n' % (str(longitude),str(latitude)))
    kmlfh.write('    </Point>\n')
    kmlfh.write('  </Placemark>\n')

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

# extract the records from the dictionary
records = din_dict['records']

# creat a kml file as output file
kmlfh = open(myfavoritedino+'new.kml','w')
#write the required first line
write_kml_start(kmlfh)

# First things first; we need a counter to provide a unique index value for each KML placemark
# And we want to plot all the ages of fossils of your favorite dino, which we will keep in a list
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
        # write the data into the kml file
        write_placemark_in_kml(kmlfh, myfavoritedino, counter, species_name, age_max, latitude, longitude)

# Write the required last lines of the KML 
write_kml_end(kmlfh)
# and close filehandle
kmlfh.close()