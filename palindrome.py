def palindrome_checker (word):
    word_length = len(word)
    counter = 1
    half = word_length // 2

    for letter in word[:half]: 
        if letter != word[word_length - counter]:
            return False
        counter += 1
  
    return True

if palindrome_checker("pottop"):
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")



