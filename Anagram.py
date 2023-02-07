# Create a function named isAnagram() following your current language's style guide.
# It should take two strings and return a boolean value depending on whether it's an anagram or not.

def anagram(string1, string2):
    reverse = ''
    for i in string2:
        reverse = i + reverse
    return string1 == reverse


print(anagram('god','dog'))
print(anagram('green','fox'))