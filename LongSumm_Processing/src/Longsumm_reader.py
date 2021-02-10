import json

# Function to load the dictionary

def get_data(path):
    with open(path,'r+') as f:
        data = json.loads(f.read())
    return data

if __name__ == '__main__':
    train_data = get_data('listofdic.json')
    test_data = get_data('listofdic_longsummtest.json')
    print("Keys in the dictionary are ",train_data[0].keys())
    print(len(train_data),len(test_data))