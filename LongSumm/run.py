import os

def get_command(file):

    return "python main2.py -batch_size 1 -device 0 -predict -filename " + file + " -topk 2 -load_dir checkpoints/XXX_pubmed.ptCNN_RNN_seed_1.pt"


for direc in os.listdir('../data_break_laysumm'):
    print('Processing file ',direc)
    print('data_break_laysumm/' + str(direc))
    try:
        if len(os.listdir('../data_break_laysumm/' + str(direc))) == 0 : continue
        for section in os.listdir('../data_break_laysumm/' + str(direc)):
            if len(section.split('.txt'))!=1:
                continue
            os.system(get_command('../data_break_laysumm/' + str(direc) + '/' + str(section)))
    except:
        pass
    break
