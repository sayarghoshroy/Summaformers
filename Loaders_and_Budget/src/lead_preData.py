from arXiv_pubMed_reader import get_datapoints as get_data

lead_count = 3

store = get_data('./ArXiv_Sample/')

units = {'train': [], 'test': [], 'val': []}
for unit in units.keys():
    size = len(store[unit])
    index = 0
    
    while(index < size):
        workon = store[unit][index]
        summary = {}
        
        count_sections = len(workon['section_names'])
        section_id = 0
        
        while(section_id < count_sections):
            summary[workon['section_names'][section_id]] = workon['sections'][section_id][0: lead_count]
            section_id += 1
        
        units[unit].append(summary)
        index += 1
