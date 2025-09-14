from wordfreq import top_n_list, random_words

class WordGenerator:
    def __init__(self):
        self.word_list = self.generate_list()


    def generate_list(self):
        word = random_words(lang='en', wordlist='best', nwords=50, bits_per_word=12)

        return word.split()

