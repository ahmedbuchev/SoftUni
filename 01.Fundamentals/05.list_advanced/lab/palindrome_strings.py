words_list = input().split()
palindrome = input()
words_list_only_with_palindromes = []

for word in words_list:
    if word == word[::-1]:
        words_list_only_with_palindromes.append(word)

count_palindrome_in_words_list = words_list_only_with_palindromes.count(palindrome)
print(words_list_only_with_palindromes)
print(f"Found palindrome {count_palindrome_in_words_list} times")
