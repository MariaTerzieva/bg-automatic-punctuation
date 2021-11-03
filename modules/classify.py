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


# input - words and y - list of words and labels for each word
# output - text (string; y labels applied to the words)
def punctuate(words, y):
    punctuated_sentences = ''

    for word, label in zip(words, y):
        if word == '^':
            pass
        elif label in ('"', '('):
            punctuated_sentences = punctuated_sentences + word + ' ' + label
        elif label == '-':
            punctuated_sentences = punctuated_sentences + word + ' ' + label + ' '
        elif label == ':"':
            punctuated_sentences = punctuated_sentences + word + label[0] + ' ' + label[1]
        else:
            punctuated_sentences = punctuated_sentences + word + label + ' '
    
    return punctuated_sentences.strip()