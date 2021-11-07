import pickle


# input - X - features (list of lists (sentences) of dictionaries (tokenized words))
# output - list of strings (labels)
def predict_punctuation(X):
    pretrained_punctuation_model_path = 'resources/random_forest_v10_model.pkl'
    prefitted_dict_vectorizer_path = 'resources/dict_vectorizer.pkl'
    prefitted_label_encoder_path = 'resources/label_encoder.pkl'

    with open(pretrained_punctuation_model_path, 'rb') as file:
        pretrained_punctuation_model = pickle.load(file)

    with open(prefitted_dict_vectorizer_path, 'rb') as file:
        prefitted_dict_vectorizer = pickle.load(file)

    with open(prefitted_label_encoder_path, 'rb') as file:
        prefitted_label_encoder = pickle.load(file)

    X_flattened = [word for sentence in X for word in sentence]
    vectorized_X = prefitted_dict_vectorizer.transform(X_flattened)
    y = pretrained_punctuation_model.predict(vectorized_X)
    decoded_y = prefitted_label_encoder.inverse_transform(y)

    return decoded_y


# input - sentences and y - list of sentences (lists) and labels for each word
# output - the labels as list of lists matching sentences structure
def restructure_y_to_list_of_lists(sentences, y):
    sentence_lengths = [len(sentence) for sentence in sentences]
    y_restructured = []
    for i, sentence_length in enumerate(sentence_lengths):
        start = sum(sentence_lengths[:i])
        end = sum(sentence_lengths[:(i+1)])
        sentence_y = y[start:end]
        y_restructured.append(sentence_y)
    return y_restructured


# input - sentences and y - list of sentences (lists) and labels for each word
# output - list of punctuated sentences (lis of string; y labels applied to the words)
def punctuate(sentences, y):
    y_restructured = restructure_y_to_list_of_lists(sentences, y)
    punctuated_sentences = []

    for sentence, sentence_labels in zip(sentences, y_restructured):
        punctuated_sentence = ''

        for i in range(len(sentence)):
            if sentence[i] == '^':
                pass
            elif sentence_labels[i] in ('"', '('):
                punctuated_sentence = punctuated_sentence + sentence[i] + ' ' + sentence_labels[i]
            elif sentence_labels[i] == '-':
                punctuated_sentence = punctuated_sentence + sentence[i] + ' ' + sentence_labels[i] + ' '
            elif sentence_labels[i] == ':"':
                punctuated_sentence = punctuated_sentence + sentence[i] + sentence_labels[i][0] + ' ' + sentence_labels[i][1]
            else:
                punctuated_sentence = punctuated_sentence + sentence[i] + sentence_labels[i] + ' '
    
        punctuated_sentences.append(punctuated_sentence.strip())

    return punctuated_sentences
