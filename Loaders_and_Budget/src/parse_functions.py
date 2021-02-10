# Functions to Parse LAYSUMM, ABSTRACT, and FULLTEXT

def summ_parser(file):
    f = open(file)
    f_str = f.read().split('\n')
    
    f_tokens = [unit for unit in f_str if unit != '']
    
    f_tokens = f_tokens[2:]
    # removing index and LAYSUMM tags
    
    info_dict = {}

    info_dict['title'] = f_tokens[1]
    info_dict['laysumm'] = f_tokens[2: ]
    # retaining paragraph tags for the time being
    
    return info_dict

def abstract_parser(file):
    f = open(file)
    f_str = f.read().split('\n')
    
    f_tokens = [unit for unit in f_str if unit != '']
    
    f_tokens = f_tokens[2:]
    # removing index and ABSTRACT tags
    
    info_dict = {}

    info_dict['title'] = f_tokens[1]
    info_dict['abstract'] = f_tokens[2: ]
    # retaining paragraph tags for the time being
    
    return info_dict

def fulltext_parser(file):
    f = open(file)
    f_str = f.read().split('\n')
    
    f_tokens = [unit for unit in f_str if unit != '']
    
    f_tokens = f_tokens[2:]
    # removing index and FULLTEXT tags
    
    info_dict = {}

    info_dict['title'] = f_tokens[1]
    
    index = 2
    size = len(f_tokens)
    
    # NOTE: There is no way to accurately identify nested sections
    while (index < size):
        if f_tokens[index] == 'SECTION':
            try:
                next_location = f_tokens.index('SECTION', index + 3)
            except:
                next_location = size
            
            info_dict [f_tokens[index + 1].lower()] = f_tokens[index + 2: next_location]
            index = next_location
    
    # Displaying section headers
    #     for key in info_dict.keys():
    #         print(key)
        
    return info_dict

