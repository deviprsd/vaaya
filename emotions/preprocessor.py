from vaaya.contexts import Context


class Preprocessor:
    def __init__(self, journal_entry):
        self.__je = Context.nlp(u'{}'.format(journal_entry))

    def __getattr__(self, item):
        __avl_pos = {'verbs': 'VERB', 'nouns': 'NOUN', 'adjectives': 'ADJ', 'adverbs': 'ADV'}

        if item in __avl_pos:
            return [[tkn for tkn in _s if tkn.pos_ == __avl_pos[item]] for _s in self.__je.sents]
        elif item == 'doc':
            return self.__je
        return None
