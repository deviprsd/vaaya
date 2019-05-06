from vaaya.contexts import Context
import numpy as np


class Semantic:
    __emotions_concepts = {
        'happiness': Context.nlp('happy glad joy good love bliss'),
        'sadness': Context.nlp('sad sorrow hurt cry bad die'),
        'anger': Context.nlp('angry irritate stupid annoy frustrate rage'),
        'fear': Context.nlp('fear afraid frighten scare terrify horror'),
        'surprise': Context.nlp('surprise amazing astonish incredible wonder flabbergast'),
        'disgust': Context.nlp('disgust dislike hate sick ill gross'),
    }

    def __init__(self, syntatic):
        self.__sync = syntatic

    def emotion_vector(self, nava):
        """
        creates emotion vector
        :param nava:
        :return:
        """
        _t_pm = np.array([self.__pmi(nava, em) for em in Semantic.__emotions_concepts.keys()])
        return _t_pm

    def __pmi(self, nava, emotion):
        """
        pointwise mutual information
        calculates emotion values
        :param nava:
        :param emotion:
        :return:
        """
        _pmi, _l = 1.0, len(Semantic.__emotions_concepts[emotion])
        if not nava.has_vector:
            return 0.00001

        for e in Semantic.__emotions_concepts[emotion]:
            # print(nava, e, nava.similarity(e))
            _pmi = _pmi * e.similarity(nava)

        return (_pmi ** (1/_l+0j)).real * (0.78 if emotion == 'happiness' else 1.0)

    def __getattr__(self, item):
        return getattr(self.__sync, item)
