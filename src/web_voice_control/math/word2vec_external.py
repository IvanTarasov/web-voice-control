from gensim.models import Word2Vec
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import numpy as np
from scipy import spatial
import nltk
import re
from pymorphy3 import MorphAnalyzer
from nltk.corpus import stopwords

patterns = "[A-Za-z0-9!#$%&'()*+,./:;<=>?@[\]^_`{|}~—\\\"\-]+"
NUM_FEATURES = 300
stopwords_ru = stopwords.words("russian")
morph = MorphAnalyzer()


def lemmatize(doc):
    doc = re.sub(patterns, ' ', doc)
    tokens = []
    for token in doc.split():
        if token and token not in stopwords_ru:
            token = token.strip()
            token = morph.normal_forms(token)[0]

            tokens.append(token)
    return tokens


def avg_feature_vector(words, model):
    feature_vec = np.zeros((NUM_FEATURES), dtype="float32")
    for word in words:
        feature_vec = np.add(feature_vec, model.wv.get_vector(word))
    if len(words) > 0:
        feature_vec = np.divide(feature_vec, len(words))
    return feature_vec


def add_pos_tags(tokens):
    pos_tags = pos_tag(tokens, lang="rus")

    result = [f'{key}_{value}' for (key, value) in pos_tags]
    print(result)
    return result


def sentence_similarity(sentence_1, sentence_2, model):
    sentence_1_avg_vector = avg_feature_vector(sentence_1, model)
    sentence_2_avg_vector = avg_feature_vector(sentence_2, model)
    return 1 - spatial.distance.cosine(sentence_1_avg_vector, sentence_2_avg_vector)


if __name__ == "__main__":
    MODEL_PATH = "Z:\model.model"
    model = Word2Vec.load(MODEL_PATH)

    sentence1 = add_pos_tags(lemmatize('оформить заказ'))
    sentence2 = add_pos_tags(lemmatize('завершить оформление заказа'))

    print(sentence_similarity(sentence1, sentence2, model))