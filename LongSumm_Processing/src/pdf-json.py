import os 
from datetime import datetime

# Path for the pdfs
pdf_path = '/home/risubaba/LongSumm/pdf/'
output_path = '/home/risubaba/Longsumm/json'
science_parse_jar_path = '/home/risubaba/science-parse/cli/target/scala-2.12/science-parse-cli-assembly-3.0.1.jar'

def get_command(file):
   return 'java -Xmx6g -jar ' + science_parse_jar_path ' + pdf_path + file + ' > ' + output_path '/' + (file.replace('.pdf','.json'))

def get_file_list():
    return os.listdir(pdf_path)

files = get_file_list()

# Number of files processed at once
batch = 20

print("Files remaining " , len(files))
for ind,file in enumerate(files):
    print("File {} - {} started at {}".format(ind,file,datetime.now()))
    os.system(get_command(file))
    print("File {} - {} finished at {}".format(ind,file,datetime.now()))     
    if ind > batch:
        break
