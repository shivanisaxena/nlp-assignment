import nltk


    
def bigram_mle_model(words):
        cfdist = nltk.ConditionalFreqDist(nltk.bigrams(words))
        return nltk.ConditionalProbDist(cfdist, nltk.MLEProbDist).perplexity(words)

def ngram_mle_model(words, n):
        ngrams = nltk.ngrams(words, n)
        cfdist = nltk.ConditionalFreqDist((tuple(x[:(n - 1)]), x[n - 1]) for x in \
                ngrams)
        return nltk.ConditionalProbDist(cfdist, nltk.MLEProbDist)


def read_sentences_from_file(file_path):
        fileObj = open(file_path, 'r',encoding="utf8")
        text = fileObj.read()
        tokens = nltk.sent_tokenize(text.lower())
        return tokens

def perplexity(testset, model):
    testset = testset.split()
    perplexity = 1
    N = 0
    for word in testset:
        N += 1
        perplexity = perplexity * (1/model[word])
    perplexity = pow(perplexity, 1/float(N)) 
    return perplexity

if __name__ == '__main__':
    tokens = read_sentences_from_file("shivi.txt")
    # ans=perplexity(tokens,bigram_mle_model(tokens))
    print(bigram_mle_model(tokens))
