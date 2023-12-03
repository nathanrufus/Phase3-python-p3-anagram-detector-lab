# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Initialize an empty list to store matching words
        matching_words = []

        # Iterate through the word_list and check for matches
        for word in word_list:
            if sorted(self.word) == sorted(word):
                matching_words.append(word)

        return matching_words