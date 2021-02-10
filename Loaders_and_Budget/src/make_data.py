from parse_functions import *
import os

def get_datapoints(location):
    # location of LAYSUMM, directory with all the triplet files
    # returns list of {'fulltext': _, 'abstract': _, 'laysumm': _}
    datapoints = []
    
    for dir_name in os.listdir(location):
        triplet_loc = location + dir_name
        
        datapoint = {}
        
        datapoint['fulltext'] = fulltext_parser(triplet_loc + "/" + "FULLTEXT")
        datapoint['abstract'] = abstract_parser(triplet_loc + "/" + "ABSTRACT")
        datapoint['laysumm'] = summ_parser(triplet_loc + "/" + "LAYSUMM")
        
        datapoints.append(datapoint)
    return datapoints


# To test:
data = get_datapoints("./LaySumm_Sample/")
print("Number of Datapoints:", len(data))
print(data[0])