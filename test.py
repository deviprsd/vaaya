from vaaya.contexts import Context
import spacy

Context.nlp = spacy.load('en_core_web_lg')

from vaaya.emotions import Analyzer

a = Analyzer('The drunk kids turned it into a disgusting party')
print(a.analyze())