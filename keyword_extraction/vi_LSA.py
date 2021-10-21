from underthesea import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

class LSA:
    def __init__(self, texts):
        self.__texts = [word_tokenize(param, format='text') for param in texts.split('\n')]

        with open('stopwords-dashed.txt', mode = 'r+', encoding = 'utf8') as f:
            stopwords = f.read().split('\n')

        self.__vectorizer = TfidfVectorizer(stop_words=stopwords, max_features = 1000, max_df = 0.5, smooth_idf = True)

    def extract(self):
        matrix = self.__vectorizer.fit_transform(self.__texts)

        SVD_model = TruncatedSVD(n_components = 10, algorithm = 'randomized', n_iter = 100, random_state = 122)
        SVD_model.fit(matrix)

        terms = self.__vectorizer.get_feature_names()

        return (terms, SVD_model.components_)
