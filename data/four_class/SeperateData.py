import numpy as np
import re
import itertools
import csv

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

data_file_name = './train.csv'

class1 = open('class_one.train', 'w')
class2 = open('class_two.train', 'w')
class3 = open('class_thr.train', 'w')
class4 = open('class_fou.train', 'w')

count = 0

with open(data_file_name, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        to_write = clean_str(','.join(row)[2:])
        if row[0] == '1':
            class1.write(to_write+'\n')
        elif row[0] == '2':    
            class2.write(to_write+'\n')
        elif row[0] == '3':
            class3.write(to_write+'\n')
        elif row[0] == '4':
            class4.write(to_write+'\n')
        count += 1
        
print(count)
        
class1.close()
class2.close()
class3.close()
class4.close()


