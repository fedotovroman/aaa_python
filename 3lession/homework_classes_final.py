from collections import Counter

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

    def get_feature_name(self) -> list:
        """
        return:
            get_feature_name(list): vocabulary of features
        """
        return self._corp_vocab



def main():
    vectorizer = CountVectorizer()
    corpus = [
   'Crock Pot Pasta Never boil pasta again',
   'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    X = vectorizer.fit_transform(corpus)
    # assert X = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    # assert vectorizer.get_feature_name() = ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    print(X)
    print(vectorizer.get_feature_name())

if __name__ == '__main__':
    main()
