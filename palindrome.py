#Find palindrome
def palindromes(s):
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]

string = "A man, a plan, a canal: Panama"
print(palindromes(string))  # Output: True
