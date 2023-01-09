def palindrome(word, index):

    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[-index - 1]:
        return palindrome(word, index + 1)

    else:
        return f"{word} is not a palindrome"


''' TESTS '''
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
