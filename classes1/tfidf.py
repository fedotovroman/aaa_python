import typing as t, math
from collections import Counter

class TfidfTransformer():
    """
    A class for transforming a bag of words to tf-idf vectors.
    ...
    Attributes
    ----------
    -
    Methods
    -------
    fit_transform(self, matrix: t.List) -> t.List[t.List[int]]:
        Trains a tf-idf on a set of bag of words.
    tf_transform(self, count_matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
        Returns tf vector of bag of documents corpus.
    idf_transform(self, count_matrix: t.List[t.List[float]]) -> t.List[float]:
        Returns idf vector of bag of documents corpus.
    """
    def fit_transform(self, matrix: t.List) -> t.List[t.List[int]]:
        """
        param:
        - matrix (List): bow matrix
        return:
        - tf_idf (list): tf-idf matrix from bow matrix
        """
        tf = self.tf_transform(matrix)
        idf = self.idf_transform(matrix)

        tf_idf = []
        for text in tf:
            tf_idf.append([round(a * b, 3) for a,b in zip(text,idf)])

        return tf_idf

    def idf_transform(self, count_matrix: t.List[t.List[float]]) -> t.List[float]:
        """
        param:
        - count_matrix (list): bow matrix
        return:
        - idf_matrix (list): idf matrix
        """
        result = list()
        document_count = len(count_matrix)
        len_vector = len(count_matrix[0])

        for col in range(len_vector):
            cur_sum = 0
            for row in range(document_count):
                cur_sum += bool(count_matrix[row][col])
            result.append(cur_sum)

        for i in range(len_vector):
            result[i] = round(math.log((document_count + 1)/(result[i] + 1)), 3) + 1

        return result

    def tf_transform(self, count_matrix: t.List[t.List[int]]) -> t.List[t.List[int]]:
        """
        param:
        - count_matrix: bow matrix
        return:
        - tf_matrix: tf-idf matrix
        """
        tf_matrix = []

        for vec in count_matrix:
            number_of_word = sum(vec)
            tf_matrix_row = [round(i/number_of_word,3) for i in vec]
            tf_matrix.append(tf_matrix_row)

        return tf_matrix

class CountVectorizer:
    """
    A class for representing a corpus of texts in the format of a bag of words.
    ...
    Attributes
    ----------
    _corp_vocab : str
        vocabulary of text features
    Methods
    -------
    fit_transform(self, corpus: list) -> List[List[int]]:
        Trains a bag of words on a set of texts and returns a matrix representation of the corpus.
    get_feature_name(self) -> list:
        Returns vocabulary of bag of words' features.
    """

    def __init__(self):
        self._corp_vocab = []


    def fit_transform(self, corpus: list) -> list:
        """
        param:
        - corpus (list): text data list
        return:
        - term_matrix (list): term-document matrix, based on input corpus of text data
        """

        total_text_counters = []

        for text in corpus:
            text_counter = Counter(text.lower().split())
            total_text_counters.append(text_counter)

            for word in text_counter.keys():
                if word not in self._corp_vocab:
                    self._corp_vocab.append(word)


        term_matrix = [
            [text_counter.get(word_from_vocab,0) for word_from_vocab in self._corp_vocab]
                for text_counter in total_text_counters
        ]

        return term_matrix

    def get_feature_names(self) -> list:
        """
        return:
            get_feature_name(list): vocabulary of features
        """
        return self._corp_vocab

class TfidfVectorizer(CountVectorizer):
    """
    A class for getting tf-idf representation of bag-of-words.
    ...
    Attributes
    ----------
    -
    Methods
    -------
    fit_transform(self, corpus: list) -> List[List[int]]:
        Trains a tf-idf representation on a corpus of texts.
    """
    def __init__(self):
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        """
        param:
        - corpus (list): text data list
        return:
        - tfidf_matrix (list): tf-idf matrix, based on input corpus of text data
        """
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


corpus = [
'Crock Pot Pasta Never boil pasta again',
'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
assert tfidf_matrix == [[0.201, 0.201, 0.286, 0.201, 0.201, 0.201, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.143, 0.0, 0.0, 0.0, 0.201, 0.201, 0.201, 0.201, 0.201, 0.201]]