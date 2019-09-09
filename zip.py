import re
import matplotlib.pyplot as plt
import numpy as np

def extract_frequencies(filename):
    d = dict()
    with open('text.txt', "r") as f:
        for line in f:
            line = line.lower().rstrip().split(' ')
            for word in line:
                word = re.sub(r'\W+', '', word)
                if word:
                    d[word] = d.get(word, 0) + 1
    return d


def build_histogram(filename, outputfilename=None, limit=20):
    data = []
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            line = line.lower().rstrip().split(',')
            data.append((int(line[1]), line[0]))
    data.sort(key=lambda d: d[0], reverse=True)

    data = data[:limit]
    words = []
    freq = []
    for d in data:
        words.append(d[1])
        freq.append(d[0])

    i = 1
    for data in zip(words, freq):
        print("No.{}\t\"{}\" : {}".format(i, data[0], data[1]))
        i += 1
        
    y_pos = np.arange(len(words))
    plt.plot(y_pos, freq, color='orange')
    plt.xticks(y_pos, words)
    plt.ylabel('Occurence')
    plt.title("Zip's law analysis")
    
    plt.show()
    
frequencies = extract_frequencies("text.txt")

build_histogram("frequencies.csv", "frequencies", 50)

