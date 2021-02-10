import pickle
import nltk
import numpy as np
import os

# Updated code to use the pickled store for testing data

# from make_data import get_datapoints as get_data

# store = get_data("./LaySumm_Test_Use/")
# print("Number of Datapoints:", len(store))

filename = "./test_data_pickled.pkl"

# To create the pickled test-set
# handler = open(filename, 'wb')
# pickle.dump(store, handler)
# handler.close()

# Using the pickled test-set directly
handler = open(filename, 'rb')
store = pickle.load(handler)
handler.close()

def get_text(units):
    text = ""
    
    for sent in units:
        if sent == 'PARAGRAPH':
            continue
        tokens = nltk.word_tokenize(sent)
        
        for token in tokens:
            text += token.strip().rstrip("\n") + " "
            
    return text

def get_tops(units):
    text = ""
    count = 0
    word_count = 0
    
    for sent in units:
        if sent == 'PARAGRAPH':
            continue

        text += sent + "\n\n"
        count += 1
        word_count += len(sent.split(" "))
        if word_count > 150:
        	break
    
    return text

count = 0

# define model name, a directory with this name will be created
model_name = "tops"
if os.path.isdir(model_name):
    os.rmdir(model_name)
os.mkdir(model_name)

for paper in store:
    count += 1

    if count % 25 == 0:
    	print(str(count) + " Completed.")

    abstract = get_text(paper['abstract']['abstract'])
    
    for key in paper['fulltext'].keys():
    	# retrieves sections one by one
        if key == 'title':
            continue
        
        section = get_text(paper['fulltext'][key])

    # use saved models to generate model output here
    # section-wise summarizers on selected sections
    # use-budget concat code
    # use the abstractor model
    # separate into sentences with blank line in between, refer: get_top_3()
    
    # example: First few sentences from abstract
    model_laySumm = get_tops(paper['abstract']['abstract'])

    output = "https://doi.org/" + paper['abstract']['url']
    output += "\n\nLAYSUMM\n\nTITLE\n\n" + paper['abstract']['title']
    output += "\n\nPARAGRAPH\n\n"
    output += model_laySumm
    output += "\n"

    file_out = open("./" + model_name + "/" + paper['abstract']['id'] + "_LAYSUMM.TXT", "w+")
    file_out.write(output)
    file_out.close()
