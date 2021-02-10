import pickle
from rouge import Rouge

rouge = Rouge()

import nltk
import numpy as np
from arXiv_pubMed_reader import get_datapoints as get_data

store = get_data('./arxiv-dataset/')

def make_stats_dict():
    # if more fields are required
    # add fields in thsis block
    
    fields = {'count': 0,
              'lengths': [],
              'rouge_measures': []}
    return fields

def get_text(units):
    
    text = ""
    
    for sent in units:
        if sent == 'PARAGRAPH':
            continue
        tokens = nltk.word_tokenize(sent)
        
        for token in tokens:
            text += token.strip().rstrip("\n") + " "
            
    return text

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

section_stats = {}

# considering only the train-set for experiments
size = len(store['train'])
index = 0

while(index < size):
    workon = store['train'][index]
    count_sections = len(workon['section_names'])
    abstract = get_text(workon['abstract_text'])
    
    section_id = 0    
    
    while(section_id < count_sections):
        section_name = workon['section_names'][section_id]
        
        if section_name not in section_stats.keys():
            section_stats[section_name] = make_stats_dict()
            
        section = get_text(workon['sections'][section_id])

        try:
            scores = rouge.get_scores(section, abstract)[0]
        except:
            section_id += 1
            continue
            
        section_stats[section_name]['count'] += 1
        section_stats[section_name]['lengths'].append(len(section))
        section_stats[section_name]['rouge_measures'].append(extract_rouge(scores))
        
        section_id += 1
    
    index += 1

# Saving Results
filename = 'stats_ArXiv.pickle'
# dumping summaries into a pickle file for further loading and evaluation
with open(filename, 'wb') as f:
    pickle.dump(section_stats, f)
