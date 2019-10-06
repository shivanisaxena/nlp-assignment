import nltk
IGNORED = ['"', '\'']
    
    NO_SPACE_BEFORE = [',', '.', '?', ':', ';', ')', '!', "n't", "''", "'t"]
    NO_SPACE_BEFORE_PREFIX = ['.', '\'']
    NO_SPACE_AFTER = ['(', '``']
    begin = '<s>'
    end = '</s>'


def read_sentences_from_file(file_path):
        fileObj = open(file_path, 'r',encoding="utf8")
        text = fileObj.read()
        tokens = nltk.sent_tokenize(text.lower())
        return clean_sentences(tokens)

def clean_sentences(sents):
       
        result = []
        for sent in sents:
            result.append(Generator.begin)
            result.extend([word for word in sent if word not in \
                Generator.IGNORED])
            result.append(Generator.end)
        return result



def generate_text(model, length):
    ix = [np.random.randint(VOCAB_SIZE)]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, VOCAB_SIZE))
    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end="")
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)


if __name__ == '__main__':
    tokens = read_sentences_from_file("speeches.txt")

 model = Sequential()
model.add(LSTM(HIDDEN_DIM, input_shape=(None, VOCAB_SIZE), return_sequences=True))
for i in range(LAYER_NUM - 1):
    model.add(LSTM(HIDDEN_DIM, return_sequences=True))
model.add(TimeDistributed(Dense(VOCAB_SIZE)))
model.add(Activation('softmax'))
model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

nb_epoch = 0
while True:
    print('\n\n')
    model.fit(X, y, batch_size=BATCH_SIZE, verbose=1, nb_epoch=1)
    nb_epoch += 1
    generate_text(model, GENERATE_LENGTH)
    if nb_epoch % 10 == 0:
        model.save_weights('checkpoint_{}_epoch_{}.hdf5'.format(HIDDEN_DIM, nb_epoch))
