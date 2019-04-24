from spacy.symbols import neg, acomp, amod


class Syntactic:
    def __init__(self, preprocessor):
        self.__prep = preprocessor
        self.__chunks = [
            self.__prep.verbs[i] + self.__prep.nouns[i] + self.__prep.adverbs[i] + self.__prep.adjectives[i]
            for i, x in enumerate(self.__prep.doc.sents)
        ]

    def __getattr__(self, item):
        __avl_deps = {'neg': neg, 'acomp': acomp, 'amod': amod}

        if item in __avl_deps:
            return [[(tkn.head, tkn) for tkn in tkns if tkn.dep == __avl_deps[item]] for tkns in self.__chunks]
        return getattr(self.__prep, item)
