# Create a function named createPalindrome() following your current language's style guide.
# It should take a string, create a palindrome from it and then return it.

def createPalindrome(my_str):
    a = ""
    for i in my_str:
        a = i + a
    print("The palindrome is : ", my_str + a)


createPalindrome("greenfox")
createPalindrome('123')


# or :

def createPalindrome1(my_str1):
    my_str2 = my_str1[::-1]
    print("The palindrome is : ", my_str1 + my_str2)


createPalindrome1("greenfox")
createPalindrome('123')
