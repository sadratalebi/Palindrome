s = input().lower()


def isPalindrome(s):
    return s == s[::-1]


answer = isPalindrome(s)
if answer:
    print("palindrome")
else:
    print("not palindrome")
