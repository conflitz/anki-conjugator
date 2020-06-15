
import random
import mlconjug3
from deck_generator import DeckCreator
from spa_verb_metadata import *

class SpanishDeckCreator(DeckCreator):

    def __init__(self, ignore_vosotros=False):
        super().__init__(language='es')
        self.ignore_vosotros = ignore_vosotros
        self.conjugator = mlconjug3.Conjugator(language='es')

    def get_conjugations(self, verb):
        if verb in INCORRECTLY_CONJUGATED:
            raise ValueError

        conjugations = {}
        for tense in TENSES:
            if tense == 'infinitive':
                continue
            if verb == 'haber' and tense == 'imperative':
                continue

            first, second = TENSES[tense]
            conj_info = self.conjugator.conjugate(verb).conjug_info[first][second]

            # mlconjug3 returns a string for present perfect and
            # returns a dict of the form {'': `gerund`} for gerund
            if tense == 'present perfect':
                conjugations[None, tense] = conj_info
            elif tense == 'gerund':
                conjugations[None, tense] = conj_info['']
            else:
                for person in conj_info:
                    if person == '2p' and self.ignore_vosotros:
                        continue
                    conjugation = conj_info[person]
                    if verb == 'haber' and conjugation == 'hay':
                        conjugation = 'ha'
                    conjugations[person, tense] = conjugation
        
        return conjugations

    def get_auxiliary(self, person, tense):
        if tense == 'present perfect':
            auxiliary_word = 'haber'
        else:
            auxiliary_word = 'estar'
        
        first, second = TENSES['present']
        aux_conj = self.conjugator.conjugate(auxiliary_word)
        auxiliary = aux_conj.conjug_info[first][second][person]

        if auxiliary == 'hay':
            auxiliary = 'ha'

        return auxiliary

    def get_subject(self, person, tense):
        # Imperative tense only uses one subject
        if tense == 'imperative':
            return IMPERATIVE_SUBJECTS[person]

        # Present perfect and gerund tenses don't have inherent perspectives
        if tense == 'present perfect' or tense == 'gerund':
            person = random.choice(list(PERSPECTIVES.keys()))
            while person == '2p' and self.ignore_vosotros:
                person = random.choice(list(PERSPECTIVES.keys()))
            auxiliary = self.get_auxiliary(person, tense)

        subject = random.choice(list(SUBJECTS[person]))
        try:
            return f'{subject} {auxiliary}'
        except NameError:
            return subject

    def get_sentence(self, tense):
        return SENTENCES[tense]

    def get_symbol(self, tense):
        return SYMBOLS[tense]

    def get_tag(self, person, tense):
        tag = ''
        if person:
            tag += f'{PERSPECTIVES[person]} '
        tag += tense.replace(' ', '_')
        return tag


s = SpanishDeckCreator(ignore_vosotros=True)
s.create_deck('spa_verb_groups.csv', 'deck.txt')