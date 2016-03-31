#palindrome.py
import re


def user_input():
    print('Please enter text, and I will tell you if it is a palindrome.')
    user_text=input('Text:')
    return user_text

def is_palindrome(text):
    pattern= r'[^A-Za-z]'
    stripped_text=re.sub(pattern,'',text)
    stripped_text=stripped_text.lower()

    #test with recursion
    if len(stripped_text) <2:
        return True
    if stripped_text[0] != stripped_text[-1]:
        return False
    return is_palindrome(stripped_text[1:-1])

def main():
    saved=user_input()
    other_saved=is_palindrome(saved)
    if other_saved==True:
        print('YES!!!')
    elif other_saved==False:
        print('NO!!!')


if __name__=='__main__':
    main()
