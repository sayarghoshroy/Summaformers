import os
from datetime import datetime

def get_command(file):
    topk = file.split('_')[-1]
    if topk == '0' : return -1
    return "python main2.py -batch_size 1 -device 0 -predict -filename " + file + " -topk " + topk + " -load_dir checkpoints_arxiv/XXX_pubmed_newpubmed.ptCNN_RNN_seed_1.pt"
direc_path = '../Data_break_long_budget_val/'


for direc in os.listdir(direc_path):
    print('Processing file ',direc,' at time ',datetime.now(),flush = True)
    print(direc_path + str(direc))
    try:
        cnt = 0
        if len(os.listdir(direc_path + str(direc))) == 0 : continue
        for section in os.listdir(direc_path + str(direc)):
            if len(section.split('.txt'))!=1:
                continue
            command = get_command(direc_path + str(direc) + '/' + str(section))
            if command == -1 : continue
            os.system(command)
            # print(get_command(direc_path + str(direc) + '/' + str(section)))
            cnt+=1
        print("Processed {} files in {} ".format(cnt,os.listdir(direc_path + str(direc))))
    except:
        pass
#    break
#   print(cnt)
