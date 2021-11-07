import classla


# inpit - list of strings
# output - list of strings
def add_special_symbol_at_start_of_each_sentence(data):
    return ['^{0}'.format(sentence) for sentence in data]


# input - list of sentences (strings) and a classla pipeline (POS tokenize or tokenize)
# output - list of dictionaries ((POS) tokenized sentences) 
def run_through_classla_pipeline(list_of_sentences, pipeline):
    return [pipeline(sentence).to_dict()[0][0] for sentence in list_of_sentences]


# input - list of dictionaries (a dictionary for each word - the tokenized version of the sentence)
# output - new sentence (string) with the punctuation removed
def remove_punctuation(sentence):
    new_sentence = ''

    for i in range(len(sentence)):
        if all(character in ',()";.?!:-' for character in sentence[i]['text']):
            pass
        else:
            new_sentence = new_sentence + sentence[i]['text'] + ' '
    
    return new_sentence


# input - sentence (list of dictionaries)
# output - True/False depending on whether the sentence contains interrogative word or not
def contains_interrogative_word(sentence):
    for i in range(len(sentence)):
        if sentence[i]['xpos'].startswith('Pi'):
            return True
    
    return False


# input - sentence (list of dictionaries)
# output - True/False depending on whether the sentence contains interrogative particle or not
def contains_interrogative_particle(sentence):
    for i in range(len(sentence)):
        if sentence[i]['xpos'] == 'Ti':
            return True
    
    return False


# input - sentence (list of dictionaries)
# output - True/False depending on whether the sentence contains imperative verb or not
def contains_imperative_verb(sentence):
    for i in range(len(sentence)):
        if sentence[i]['xpos'][0] == 'V' and sentence[i]['xpos'][4] == 'z':
            return True
    
    return False


# input - sentence (list of dictionaries) and index of a word (dictionary)
# output - True/False depending on whether the sentence contains repetitive conjunction before
def contains_rep_conj_before(sentence, i):
    if i < len(sentence)-1 and sentence[i+1]['xpos'] in ('Cr', 'Cp'):
        for word_i in reversed(range(len(sentence[:i]))):
            if sentence[word_i]['xpos'] == sentence[i+1]['xpos']:
                return True
    
    return False


# input - sentence (list of dictionaries)
# output - True/False depending on whether the sentence contains publicistic word
def contains_publicistic_word(sentence):
    publicistic_words_list = ['казва', 'каза', 'заяви', 'заявява', 'отбеляза', 'добави', 'добавя',
                              'цитира', 'твърди', 'обясни', 'посочи', 'допълни', 'подчерта', 'писа',
                              'изтъкна', 'посочва', 'пише', 'заключи', 'сподели', 'обяснява', 'предупреди',
                              'отбелязва', 'предупреждава', 'призова', 'допълва', 'съобщи', 'заяви', 'обяви',
                              'коментира']

    for i in range(len(sentence)):
        if sentence[i]['text'] in publicistic_words_list:
            return True
    
    return False


# input - sentence (list of dictionaries) and index of a word (dictionary)
# output - the count of the verbs before the word
def between_two_verbs(sentence, i):
    verb_before = False
    verb_after = False

    for word_i in reversed(range(len(sentence[:(i+1)]))):
        if sentence[word_i]['upos'] == 'VERB':
            verb_before = True
    
    for word in sentence[(i+1):]:
        if word['upos'] == 'VERB':
            verb_after = True
    
    return verb_before and verb_after


# input - a full xpos tag as defined in BulTreeBank tagset (string) and a prefix word for the output dictionary keys (string)
# output - a dictionary with subtags generated from the full xpos tag with prefix word and their corresponding values
def split_xpos(xpos, word='word'):
    def gender_number_article(number, gender, article):
        gender_number_article = ''
        
        for feature in (gender, number, article):
            if feature:
                gender_number_article += feature
            else:
                gender_number_article += '-'
        
        return gender_number_article

    pos2features = {'N': {'xpos_type': xpos[:2], 'xpos_gender_number_article': xpos[2:5]},
                    'A': {'xpos_type': xpos[:1], 'xpos_gender_number_article': xpos[1:4]},
                    'H': {'xpos_type': xpos[:1], 'xpos_gender_number_article': xpos[1:4]},
                    'M': {'xpos_type': xpos[:2], 'xpos_gender_number_article': xpos[2:5]},
                    'V': {'xpos_type': xpos[:2],
                          'xpos_gender_number_article': gender_number_article(xpos[8:9], xpos[9:10], xpos[10:11])},
                    'P': {'xpos_type': xpos[:2],
                          'xpos_gender_number_article': gender_number_article(xpos[5:6], xpos[7:8], xpos[8:9])},
                    'D': {'xpos_type': xpos},
                    'C': {'xpos_type': xpos},
                    'T': {'xpos_type': xpos},
                    'R': {'xpos_type': xpos},
                    'I': {'xpos_type': xpos}}
    
    result_pos2features = pos2features.get(xpos[0], {'xpos_type': xpos})
    
    if xpos[0] == 'V' and xpos[4:5] in ('z', 'c', 'g'):
        result_pos2features.update({'xpos_mood': xpos[4:5]})
    elif xpos[0] == 'P' and xpos[2:3] in ('e', 'a', 'l', 'm', 'q', 't'):
        result_pos2features.update({'xpos_ref_type': xpos[2:3]})
    elif xpos[0] == 'A' and xpos[4:5] == 'e':
        result_pos2features.update({'xpos_extended': xpos[4:5]})
    
    return {(word + '_' + key): value.rstrip('-') for key, value in result_pos2features.items()}


# input - sentence (list of dictionaries) and an index of a word (dictionary)
# output - list of dictionaries (features, for each word)
def word2features(sentence, i):
    sentence_contains_interrogative_word = contains_interrogative_word(sentence)
    sentence_contains_interrogative_particle = contains_interrogative_particle(sentence)
    sentence_contains_imperative_verb = contains_imperative_verb(sentence)

    features = {
        'word': sentence[i]['text'].lower(),
        'sent_len': len(sentence),
        'upos': sentence[i]['upos'],
        'first_word_in_sent': sentence[1]['text'].lower(),
        'contains_interrogative_word': sentence_contains_interrogative_word,
        'contains_interrogative_particle': sentence_contains_interrogative_particle,
        'contains_imperative_verb': sentence_contains_imperative_verb,
        'contains_repetitive_conj_before': contains_rep_conj_before(sentence, i),
        'between_two_verbs': between_two_verbs(sentence, i),
        'contains_publicistic_word': contains_publicistic_word(sentence)
    }

    features.update(split_xpos(sentence[i]['xpos']))

    if i > 0:
        features.update({
            'prev_word': sentence[i-1]['text'].lower(),
            'prev_word_upos': sentence[i-1]['upos']
        })

        features.update(split_xpos(sentence[i-1]['xpos'], 'prev_word'))
    else:
        features.update({
            'BOS': True
        })

    if i > 1:
        features.update({
            'word_before_prev_word': sentence[i-2]['text'].lower(),
            'word_before_prev_word_upos': sentence[i-2]['upos']
        })
        
        features.update(split_xpos(sentence[i-2]['xpos'], 'word_before_prev_word'))

    if i < len(sentence)-1:
        features.update({
            'next_word': sentence[i+1]['text'].lower(),
            'next_word_upos': sentence[i+1]['upos']
        })
        
        features.update(split_xpos(sentence[i+1]['xpos'], 'next_word'))
    else:
        features.update({
            'EOS': True
        })
        
    if i < len(sentence)-2:
        features.update({
            'word_after_next_word': sentence [i+2]['text'].lower(),
            'word_after_next_word_upos': sentence[i+2]['upos']
        })
        
        features.update(split_xpos(sentence[i+2]['xpos'], 'word_after_next_word'))

    return features


# input - input_sentences - list of sentences (strings)
# output - X, sentences - features and list of sentences in orginal text format 
def data_prep(input_sentences):
    data = add_special_symbol_at_start_of_each_sentence(input_sentences)

    nlp_tokenize = classla.Pipeline('bg', processors='tokenize', logging_level='ERROR')
    tokenized_data = run_through_classla_pipeline(data, nlp_tokenize)
    data_without_punctuation = [remove_punctuation(sentence) for sentence in tokenized_data]
    
    nlp_pos_tokenize = classla.Pipeline('bg', processors='tokenize,pos', logging_level='ERROR')   
    pos_tokenized_data = run_through_classla_pipeline(data_without_punctuation, nlp_pos_tokenize)

    X = []
    sentences = []

    for sentence in pos_tokenized_data:
        sent2features = []
        sentence_words = []

        for i in range(len(sentence)):
            sentence_words.append(sentence[i]['text'])
            sent2features.append(word2features(sentence, i))

        X.append(sent2features)
        sentences.append(sentence_words)
        
    return X, sentences