from functools import partial
from .preprocessor import Preprocessor
from .semantic import Semantic
from .syntactic import Syntactic
import numpy as np


class Analyzer:
    def __init__(self, journal_entry):
        self.__analyzer = Semantic(Syntactic(Preprocessor(journal_entry)))
        self.POS = ['VERB', 'ADJ', 'ADV', 'NOUN']
        self._ve = [[self.__analyzer.emotion_vector(nava) for nava in pos] for pos in self.__analyzer.verbs]
        self._ae = [[self.__analyzer.emotion_vector(nava) for nava in pos] for pos in self.__analyzer.adjectives]
        self._ade = [[self.__analyzer.emotion_vector(nava) for nava in pos] for pos in self.__analyzer.adverbs]
        self._ne = [[self.__analyzer.emotion_vector(nava) for nava in pos] for pos in self.__analyzer.nouns]
        self._sent_em, self._doc_em = None, None

    def analyze(self):
        self.__analyze_syntactic(
            VERBE=self._ve, ADJE=self._ae, ADVE=self._ade, NOUNE=self._ne,
            VERB=self.__analyzer.verbs, ADJ=self.__analyzer.adjectives,
            ADV=self.__analyzer.adverbs, NOUN=self.__analyzer.nouns
        )

        self._sent_em = [
            self.__sentence_emotion(i) for i in range(len(self._ve))]
        self._doc_em = self.__doc_emotion()
        return self._sent_em, self._doc_em

    def __analyze_syntactic(self, **kwargs):
        _ng = self.__analyzer.neg
        _ac = self.__analyzer.acomp
        _am = self.__analyzer.amod

        for idx in range(len(_ac)):
            map(partial(self.__context_modifiers, i=idx, **kwargs), _ac[idx])
            map(partial(self.__context_modifiers, i=idx, **kwargs), _am[idx])
            map(partial(self.__context_modifiers, i=idx, neg=True, **kwargs), _ng[idx])

    def __context_modifiers(self, deps, i, neg=False, **kwargs):
        for dep in deps:
            if dep[0].pos_ not in self.POS: continue
            idxd, idxi = kwargs[dep[0].pos_][i].index(dep[0]), kwargs[dep[1].pos_][i].index(dep[1])
            vecd, veci = kwargs[dep[0].pos_ + 'E'][i][idxd], kwargs[dep[1].pos_ + 'E'][i][idxi]
            rvec = np.multiply(kwargs[dep[0].pos_ + 'E'][i][idxd], 0) if neg else np.divide(np.add(vecd, veci), 2)
            kwargs[dep[0].pos_ + 'E'][i][idxd] = rvec

    def __sentence_emotion(self, i):
        _s, _len = np.zeros((1, 6)), 0
        for arg in [self._ve[i], self._ae[i], self._ade[i], self._ne[i]]:
            _len += len(arg)
            _s = np.add(_s, sum(arg))
        return np.divide(_s, _len if _len else 1)

    def __doc_emotion(self):
        return np.divide(sum(self._sent_em), len(self._sent_em))