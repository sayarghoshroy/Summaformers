import pickle
from rouge import Rouge

rouge = Rouge()

import nltk
import numpy as np
from make_data import get_datapoints as get_data

store = get_data("./laySumm_train/")
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
    
    for sent in units:
        if sent == 'PARAGRAPH':
            continue
        tokens = nltk.word_tokenize(sent)
        
        for token in tokens:
            text += token.strip().rstrip("\n") + " "
            
    return text

section_stats = {}

count = 0

for paper in store:
    
    count += 1

    if count % 25 == 0:
    	print(str(count) + " Completed.")

    laySumm = get_text(paper['laysumm']['laysumm'])
    abstract = get_text(paper['abstract']['abstract'])

    key = 'abstract'

    if key not in section_stats.keys():
        section_stats[key] = make_stats_dict()

    try:
        scores = rouge.get_scores(abstract, laySumm)[0]
    except:
        continue

    section_stats[key]['count'] += 1
    section_stats[key]['lengths'].append(len(abstract))
    section_stats[key]['rouge_measures'].append(extract_rouge(scores))
    
    for key in paper['fulltext'].keys():
        if key == 'title':
            continue
            
        if key not in section_stats.keys():
            section_stats[key] = make_stats_dict()

        
        section = get_text(paper['fulltext'][key])
            
        try:
            scores = rouge.get_scores(section, laySumm)[0]
        except:
            continue
        
        section_stats[key]['count'] += 1
        section_stats[key]['lengths'].append(len(section))
        section_stats[key]['rouge_measures'].append(extract_rouge(scores))

# Displaying Results
print("Section Head: Count".upper())
for key in section_stats.keys():
    if section_stats[key]['count'] >= 5:
        print(key + ": " + str(section_stats[key]['count']))

# Saving Results
filename = 'stats_LaySumm_lay.pickle'
# dumping summaries into a pickle file for further loading and evaluation
with open(filename, 'wb') as f:
    pickle.dump(section_stats, f)
