# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
import string


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = ''.join(word.split(' '))
    anagram = ''.join(anagram.split(' '))


    word = word.translate(str.maketrans('', '', string.punctuation))
    anagram = anagram.translate(str.maketrans('', '', string.punctuation))

    if sorted(word) == sorted(anagram):
        return True

    else:
        return False

print(find_anagram('note', 'tone'))
print(find_anagram('surd', 'sword'))
