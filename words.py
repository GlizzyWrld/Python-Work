def print_upper_words(words):
    """Given a list of words, return the words capitalized"""

    for word in words:
        print (word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words2(words):
    """Print each word uppercased, if starts with E or e.

         print_upper_words2(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

print_upper_words2(["eagle", "Edward", "Alfred"])


def print_upper_words3(words, must_start_with):
    """Print each word uppercased, if starts with given

     print_upper_words3(["eagleeys", "Edwardo", "Ana", "zope"],
        
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                

print_upper_words3(["Eagleeys", "Edwardo", "Ana", "zope",], ["E"])