import glob
import re
import os


import matplotlib.pyplot as plt


def text_in_dir_stats(root_dir='Text',maxfiles=10):
    
        pattern = os.path.join(root_dir, '*.*')
        dictionary = {}
        files = 0
        for filename in glob.iglob('Text/*'):
            files += 1
            if files > maxfiles:
                break
            
            words = regex.findall(open(filename, 'r').read())
            for word in words:
                
                dictionary[word] = dictionary.get(word, 0) + 1
        return dictionary


dictionary = text_in_dir_stats()

root_dir='Text'
print('Working on Heaps\' law...')
files = 7 
words=[]
data=[]
for max_files in range (1, files):
    dictionary = text_in_dir_stats(root_dir, max_files)
    words.append(len(dictionary))
    data.append(sum(dictionary.values()))


plt.plot(data,words,color='orange')
plt.xlabel('total words')
plt.ylabel('unique words')
plt.title("heap's law analysis")
plt.show()


