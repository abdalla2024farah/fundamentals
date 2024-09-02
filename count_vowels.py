import re

def count_vowels(text):
    
    vowels = re.findall(r'[aeiou]', text, re.IGNORECASE)
    
    print(len(vowels))

text = input('Write your text: ')
count_vowels(text)
