import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
nlp = English()

import pickle
import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize

import numpy as np
import os
import pandas as pd
from tqdm import tqdm

# Other imports, torch and all

filename = open("drive/My Drive/Scientific_Doc_Summarization_Raw_Data/Pickled Datasets/laySumm_Test.pkl", "rb")
# Modify path to pickle file above
# To download: https://drive.google.com/file/d/1Ets57PCze5mw5dStEPJ2Tmb_IeFYZodb/view?usp=sharing

store = pkl.load(filename)
print("Number of Datapoints:", len(store))

def get_text(units):
    text = ""
    
    for sent in units:
        if sent == 'PARAGRAPH':
            continue
        tokens = nltk.word_tokenize(sent)
        
        for token in tokens:
            text += token.strip().rstrip("\n") + " "
            
    return text

# define model name, a directory with this name will be created
model_name = "LaySumm_Trained"

if os.path.isdir(model_name):
    os.rmdir(model_name)
os.mkdir(model_name)

all_summaries = {}

for paper in tqdm(store):

    abstract = get_text(paper['abstract']['abstract'])

    ### Just in case you're using conclusion as well
    if 'conclusion' in paper['fulltext'].keys():
      doc_conc = get_text(paper['fulltext']['conclusion']).replace("\n"," ")
    
    elif 'conclusions' in paper['fulltext'].keys():
      doc_conc = get_text(paper['fulltext']['conclusions']).replace("\n"," ")
    
    else:
      no_conc += 1
      doc_conc = ""

    # To use other sections
    for key in paper['fulltext'].keys():
    	# retrieves sections one by one
        if key == 'title':
            continue
        
        section = get_text(paper['fulltext'][key])

    # The `abstract` is what you need
    # use saved models to generate model output here
    # & store in `model_laySumm` variable
    
    model_laySumm = your_model(abstract)

    model_laySumm = '.\n\n'.join(model_laySumm.split('.'))
    # To ensure new sentences are separated by 2 lines.

    # Autogenerate submission
    output = "https://doi.org/" + paper['abstract']['url']
    output += "\n\nLAYSUMM\n\nTITLE\n\n" + paper['abstract']['title']
    output += "\n\nPARAGRAPH\n\n"
    output += model_laySumm
    output += "\n"

    all_summaries[paper['abstract']['id']] = model_laySumm

   	file_out = open("./" + model_name + "/" + paper['abstract']['id'] + "_LAYSUMM.TXT", "w+")
    file_out.write(output)
    file_out.close()

# to store summaries for viewing
filename = open("results.pkl", "wb")
pickle.dump(all_summaries, filename)
