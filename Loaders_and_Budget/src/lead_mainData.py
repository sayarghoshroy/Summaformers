from make_data import get_datapoints as get_data

# Number of Sentences from each Section
lead_count = 3

store = get_data("./LaySumm_Sample/")
print("Number of Datapoints:", len(store))

# Displaying the fields
for key in store[0].keys():
    print(key)

size = len(store)
index = 0
section_summs = []

while(index < size):
    workon = store[index]
    summary = {}
    
    count_sections = len(workon['fulltext'].keys()) - 1
    # 'fulltext' contains the 'title' block as well
    
    for key in workon['fulltext'].keys():
        if key == 'title':
            continue
        
        summary[key] = workon['fulltext'][key][0: lead_count]
    
    section_summs.append(summary)
    index += 1

# Testing creation:
# print(section_summs[0])

