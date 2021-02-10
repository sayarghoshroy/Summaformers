from parse_functions import *
import os

def get_datapoints(location):
    # location of LAYSUMM, directory with all the triplet files
    # returns list of {'fulltext': _, 'abstract': _, 'laysumm': _}
    datapoints = []
    
    for dir_name in os.listdir(location):
        triplet_loc = location + dir_name
        
        datapoint = {}
        
        datapoint['fulltext'] = fulltext_parser(triplet_loc + "/" + dir_name + "_FULLTEXT")
        datapoint['abstract'] = abstract_parser(triplet_loc + "/" + dir_name + "_ABSTRACT")
        # datapoint['laysumm'] = summ_parser(triplet_loc + "/" + dir_name + "_LAYSUMM")
        
        datapoints.append(datapoint)
    return datapoints


# To test:
# data = get_datapoints("./LaySumm/")
# print("Number of Datapoints:", len(data))
