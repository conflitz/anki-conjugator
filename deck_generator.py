
import os
import csv
from wordfreq import zipf_frequency

class DeckCreator:
    
    def __init__(self, language=None):
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.language = language
    
    def create_deck(self, csv_name, outputfile, sep='|'):
        verbs = self.get_verbs(csv_name)
        cards = self.create_cards(verbs, sep)
        self._output(cards, outputfile)

    def get_verbs(self, csv_name):
        """
        Takes in the csv file name for the groups of verbs and returns a 
        list of all the verbs.
        """
        verbs = []
        csvpath = os.path.join(self.dir, csv_name)
        with open(csvpath, encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                for verb in row:
                    if verb != '':
                        verbs.append(verb)
        return verbs

    def create_cards(self, verbs, sep):
        """
        Writes an Anki-importable text file with conjugations of the form
        infinitive|conjugation|tense|symbol|context|tags, or with an
        optionally different delimiter.
        """
        cards = {}
        for verb in verbs:
            try:
                conjugations = self.get_conjugations(verb)
            except ValueError:
                print(f'{verb} cannot be conjugated correctly, so it was skipped')
                continue

            for person, tense in conjugations:
                conjugation = conjugations[person, tense]
                if conjugation not in cards:
                    cards[conjugation] = []

                subject = self.get_subject(person, tense)
                sentence = self.get_sentence(tense)
                symbol = self.get_symbol(tense)
                tag = self.get_tag(person, tense)

                if sentence:
                    card = (f'{verb}{sep}{conjugation}{sep}{tense}{sep}'
                        + f'{symbol}{sep}{sentence} {subject}{sep}{tag}')
                else:
                    card = (f'{verb}{sep}{conjugation}{sep}{tense}{sep}'
                        + f'{symbol}{sep}{subject}{sep}{tag}')
                cards[conjugation].append(card)
        return cards

    def get_conjugations(self, verb):
        """
        Returns a dictionary with (person, tense) as keys and conjugations
        as values.
        """
        raise NotImplementedError

    def get_subject(self, person, tense):
        raise NotImplementedError

    def get_sentence(self, tense):
        raise NotImplementedError

    def get_symbol(self, tense):
        raise NotImplementedError

    def get_tag(self, person, tense):
        raise NotImplementedError

    def sort(self, conjugations):
        return sorted(
            conjugations,
            key=lambda w : zipf_frequency(w, self.language),
            reverse=True
        )

    def _output(self, cards, outputfile):
        outputpath = os.path.join(self.dir, outputfile)
        with open(outputpath, 'w+', encoding='utf8') as f:
            for conjugation in self.sort(cards):
                for card in cards[conjugation]:
                    f.write(f'{card}\n')
