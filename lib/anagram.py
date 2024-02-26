class Anagram:
    '''Class Anagram in anagram.py'''

    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        return [candidate
                for candidate in candidates
                if self.word.lower() != candidate.lower()
                and sorted(self.word.lower()) == sorted(candidate.lower())]