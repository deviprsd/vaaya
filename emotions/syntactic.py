from spacy.symbols import neg, acomp, amod


class Syntactic:
    def __init__(self, preprocessor):
        self.__prep = preprocessor
        self.__chunks = self.__prep.verbs + self.__prep.nouns + self.__prep.adverbs + self.__prep.adjectives

    def __getattr__(self, item):
        __avl_deps = {'neg': neg, 'acomp': acomp, 'amod': amod}

        if item in __avl_deps:
            return [[(tkn.head, tkn) for tkn in tkns if tkn.dep == __avl_deps[item]] for tkns in self.__chunks]
        return getattr(self.__prep, item)
