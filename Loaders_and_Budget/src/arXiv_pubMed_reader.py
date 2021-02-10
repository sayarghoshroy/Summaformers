import os
import json
import pickle

def get_datapoints(location):
    # location of ArXiv or PubMed directory with train, val, test splits
    if location.endswith('/') == False:
        location = location + "/"
    
    datapoints = {'train': [], 'test': [], 'val': []}
    
    for unit in datapoints.keys():
        file_name = location + unit + "_sample.txt"
        lines = open(file_name).read().split("\n")
        
        datalines = []
        
        for line in lines:
            try:
                line.replace("'", "\"")
                datalines.append(json.loads(line))
            except:
                pass
        
        datapoints[unit] = datalines
        
    return datapoints

# To test:
# store = get_datapoints('./ArXiv_Sample/')
