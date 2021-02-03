import torch
from nltk import sent_tokenize

class Vocab():
    def __init__(self,embed,word2id):
        self.embed = embed
        self.word2id = word2id
        self.id2word = {v:k for k,v in word2id.items()}
        assert len(self.word2id) == len(self.id2word)
        self.PAD_IDX = 0
        self.UNK_IDX = 1
        self.PAD_TOKEN = 'PAD_TOKEN'
        self.UNK_TOKEN = 'UNK_TOKEN'
    
    def __len__(self):
        return len(word2id)

    def i2w(self,idx):
        return self.id2word[idx]
    def w2i(self,w):
        if w in self.word2id:
            return self.word2id[w]
        else:
            return self.UNK_IDX
    
    def make_features(self,batch,sent_trunc=50,doc_trunc=100,split_token='\n'):
        sents_list,targets,doc_lens = [],[],[]
        # trunc document
        # print("Batch len is {}".format(len(batch['doc'])))
        for doc,label in zip(batch['doc'],batch['labels']):
            if doc == "" : continue
            sents = doc.split(split_token)
            # sents = [ sent for sent in sents if len(sent) > 10]
            labels = label.split(split_token)
            assert len(sents) == len(labels)
            # print(len(sents) , len(labels) , labels)
            labels = [float(l) for l in labels if l != '']
            max_sent_num = min(doc_trunc,len(sents))
            sents = sents[:max_sent_num]
            labels = labels[:max_sent_num]
            sents_list += sents
            targets += labels
            doc_lens.append(len(sents))
        # trunc or pad sent
        max_sent_len = 0
        batch_sents = []
        for sent in sents_list:
            words = sent.split()
            if len(words) > sent_trunc:
                words = words[:sent_trunc]
            max_sent_len = len(words) if len(words) > max_sent_len else max_sent_len
            batch_sents.append(words)
        
        features = []
        for sent in batch_sents:
            feature = [self.w2i(w) for w in sent] + [self.PAD_IDX for _ in range(max_sent_len-len(sent))]
            features.append(feature)
        
        features = torch.LongTensor(features)
        # print(targets)
        targets = torch.LongTensor(targets)
        summaries = ""

        return features,targets,summaries,doc_lens

    def make_predict_features(self, batch, sent_trunc=150, doc_trunc=100, split_token='. '):
        # sents_list, doc_lens = [],[]
        # for doc in batch:
        #     doc = doc.replace("\n"," ")
        #     sents = doc.split(split_token)
        #     sents = [ sent for sent in sents if len(sent) > 10 ]
        #     max_sent_num = min(doc_trunc,len(sents))
        #     sents = sents[:max_sent_num]
        #     sents_list += sents
        #     if doc == "" : doc_lens.append(0)
        #     else : doc_lens.append(len(sents))
        # # trunc or pad sent
        # max_sent_len = 0
        # batch_sents = []
        # for sent in sents_list:
        #     words = sent.split()
        #     if len(words) > sent_trunc:
        #         words = words[:sent_trunc]
        #     max_sent_len = len(words) if len(words) > max_sent_len else max_sent_len
        #     batch_sents.append(words)

        # features = []
        # for sent in batch_sents:
        #     feature = [self.w2i(w) for w in sent] + [self.PAD_IDX for _ in range(max_sent_len-len(sent))]
        #     features.append(feature)

        # features = torch.LongTensor(features)

        # return features, doc_lens

        sents_list, doc_lens = [],[]
        sents = [ list(sent[0])[0] for sent in batch['sent_labels']]
        # sents = [ sent for sent in sents if len(sent) > 10 ]
        # max_sent_num = len(sents)
        max_sent_num =  min(doc_trunc,len(sents))
        sents = sents[:max_sent_num]
        sents_list += sents
        doc_lens.append(len(sents))
        # trunc or pad sent
        # print(sents_list)
        max_sent_len = 0
        batch_sents = []
        for sent in sents_list:
            words = sent.split()
            # print(words)
            if len(words) > sent_trunc:
                words = words[:sent_trunc]
            max_sent_len = len(words) if len(words) > max_sent_len else max_sent_len
            batch_sents.append(words)

        features = []
        # print(batch_sents)
        for sent in batch_sents:
            feature = [self.w2i(w) for w in sent] + [self.PAD_IDX for _ in range(max_sent_len-len(sent))]
            features.append(feature)
            # print(feature)

        features = torch.LongTensor(features)

        return features, doc_lens
