from __future__ import print_function

import collections
import os
import sys
import string

import matplotlib.pyplot as plt


with open('tweets-dataset.csv') as f:
        flines = f.readlines()
        totallines = len(flines)
        words = []
        for line in flines:
            new_words = line.split()
            words += [word.lower() for word in new_words]

totalwords = len(words)

   
for i in range(n_words):
        for c in string.punctuation:
            words[i] = words[i].replace(c,'')

    
words = list(filter(None, words))
totalwords = len(words)

   
word_count = collections.Counter(words)

    
unique_words = list(word_count.keys())
unique_words.sort()

totalunique = len(unique_words)
ttr = len(word_count)/float(len(words))


out_fname = '{}_out.txt'.format(os.path.splitext('tweets-dataset.csv')[0])

out_lines = []

out_lines.append('Number of occurences:             {}\n'.format(totallines))
out_lines.append('Total Numberof Words (T):        {}\n'.format(totalwords))
out_lines.append('Total Number of Unique Words (U): {}\n'.format(totalunique))
out_lines.append('Type-Token Ratio (U/T):           {:0.4f}\n'.format(ttr))

out_lines.append('\nUnique Words (frequency):\n')
for word, count in word_count.most_common():
        out_lines.append('{}\t{}\n'.format(count, word))

out_lines.append('\nUnique Words (alphabetical):\n')
for word in unique_words:
        out_lines.append('{}\t{}\n'.format(word_count[word], word))
        

with open(out_fname, 'w') as out_file:
        for line in out_lines:
            out_file.write(line)



    
output = ''.join(out_lines)

print(output)


