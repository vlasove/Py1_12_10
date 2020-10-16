# D5:I solution

first_word = input()
while True:
    current_word = input()
    
    if first_word[-1] != current_word[0]:
        print(current_word)
        break
    else:
        first_word = current_word
