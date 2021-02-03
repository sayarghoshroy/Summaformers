import json , os , pickle
from rouge_score import rouge_scorer
from nltk import tokenize
scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)

def get_datapoints():

    location = 'laysumm_train.json'
    with open(location,'r+') as f:
        data = json.loads(f.read())
    print(len(data))

    updated_data = []
    for ind,file in enumerate(data):
        print('Processing file number, ',ind + 1)
        updated_data.append(update_format(file))
    with open('laysumm_train_withlabels.json','w+') as f:
        json.dump(updated_data,f)

def get_labels(doc,abstract):
    doc = tokenize.sent_tokenize(doc)
    print(len(doc))
    summ = ''
    cur_score = 0
    labels = [ 0 for x in range(len(doc))]
    while True:
        for ind,x in enumerate(doc):
            if labels[ind] == 1 : continue
            cur_summ = summ + ' ' + doc[ind]
            score = scorer.score(cur_summ,abstract)['rouge1'].fmeasure
            if score > cur_score :
                cur_score = score
                summ = cur_summ
                labels[ind] = 1
                break
        else : break
    labels = [str(i) for i in labels]
    return '\n'.join(labels)

def update_format(paper):
    updated_batch = {}
    print(paper.keys())
    updated_batch['doc'] = ''
    for section in paper['sections']:
        updated_batch['doc']+= ' ' + paper['sections'][section]
    updated_batch['summaries'] = ''.join(paper['laysumm']).replace('<S>','').replace('</S>','')
    updated_batch['labels'] = get_labels(updated_batch['doc'],updated_batch['summaries'])
    return updated_batch
    

get_datapoints()
# with open('pubmed_dataset_new/train_sample.txt','w+') as f:
#     for doc in updated_data['train']:
#         f.write(json.dumps(doc))
#         f.write('\n')

# with open('pubmed_dataset_new/test_sample.txt','w+') as f:
#     for doc in updated_data['test']:
#         f.write(json.dumps(doc))
#         f.write('\n')

# with open('pubmed_dataset_new/val_sample.txt','w+') as f:
#     for doc in updated_data['val']:
#         f.write(json.dumps(doc))
#         f.write('\n')

# print('Done :)')
