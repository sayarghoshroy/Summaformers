import pickle
from rouge import Rouge

rouge = Rouge()

import nltk
import numpy as np
import json

def get_data(path):
    with open(path,'r+') as f:
        data = json.loads(f.read())
    return data

store = get_data("../LongSumm/listofdic.json")
print("Number of Datapoints:", len(store))

# Displaying All Fields
# Checking Correctness of Loader
# for key in store[0]['fulltext'].keys():
#     print(key)

def make_stats_dict():
    # if more fields are required
    # add fields in thsis block
    
    fields = {'count': 0,
              'lengths': [],
              'rouge_measures': []}
    return fields

def extract_rouge(rouge_dict):
    # extracts all rouge metrics
    # returns a numpy array
    # s.t additive properties can be used directly
    
    scores = []

    scores.append(100 * rouge_dict["rouge-1"]['f'])
    scores.append(100 * rouge_dict["rouge-1"]['p'])
    scores.append(100 * rouge_dict["rouge-1"]['r'])

    scores.append(100 * rouge_dict["rouge-2"]['f'])
    scores.append(100 * rouge_dict["rouge-2"]['p'])
    scores.append(100 * rouge_dict["rouge-2"]['r'])

    scores.append(100 * rouge_dict["rouge-l"]['f'])
    scores.append(100 * rouge_dict["rouge-l"]['p'])
    scores.append(100 * rouge_dict["rouge-l"]['r'])

    return np.asarray(scores)

def get_text(units):
    
    text = ""

    return text

section_stats = {}

count = 0

for paper in store:
    count += 1

    if count % 25 == 0:
    	print(str(count) + " Completed.")

    abstract = paper['abstractText']
    
    if not paper['sections'] or not abstract:
        continue

    for section in paper['sections']:
        if not section['heading']:
            continue
            
        if section['heading'] not in section_stats.keys():
            section_stats[section['heading']] = make_stats_dict()

        try:
            scores = rouge.get_scores(section['text'], abstract)[0]
        except:
            continue
        
        section_stats[section['heading']]['count'] += 1
        section_stats[section['heading']]['lengths'].append(len(section['text']))
        section_stats[section['heading']]['rouge_measures'].append(extract_rouge(scores))

# Displaying Results
print("Section Head: Count".upper())
for key in section_stats.keys():
    if section_stats[key]['count'] >= 5:
        print(key + ": " + str(section_stats[key]['count']))

# Saving Results
filename = 'Longsumm_stats.pickle'
# dumping summaries into a pickle file for further loading and evaluation
with open(filename, 'wb') as f:
    pickle.dump(section_stats, f)
