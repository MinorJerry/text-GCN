# coding: utf-8

import sys
from collections import Counter
import numpy as np

prefix = '../data/corpus/'
f_train = open(prefix + 'cnews.train.txt', 'r', encoding='utf-8')
f_test = open(prefix + 'cnews.test.txt', 'r', encoding='utf-8')

contents = []
labels = []
for line in f_train:
    try:
        label, content = line.strip().split('\t')
        if content:
            contents.append(' '.join(list(content)))
            labels.append('train' + '\t' + label)
    except:
        pass

for line in f_test:
    try:
        label, content = line.strip().split('\t')
        if content:
            contents.append(' '.join(list(content)))
            labels.append('test' + '\t' + label)
    except:
        pass
f_train.close()
f_test.close()

all_data = '\n'.join(contents)
f_all_data = open(prefix + 'cnews.txt', 'w', encoding='utf-8')
f_all_data.write(all_data)
f_all_data.close()

informations = []
for i in range(len(labels)):
    information = str(i) + '\t' + labels[i]
    informations.append(information)

all_info = '\n'.join(informations)
f_info = open('../data/cnews.txt', 'w', encoding='utf-8')
f_info.write(all_info)
f_info.close()


