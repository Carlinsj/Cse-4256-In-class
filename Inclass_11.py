# Question 1
def vowels(sentence):
    vowels_set = "aeiouyAEIOUY"
    words = sentence.split()
    max_vowel_count = 0
    word_with_most_vowels = ""
    for word in words:
        count = sum(1 for char in word if char in vowels_set)
        if count > max_vowel_count:
            max_vowel_count = count
            word_with_most_vowels = word
            
    return word_with_most_vowels

# Question 2
def shift_encipher(text, shift):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(shifted + ord('A'))
    return result

# Question 3
def shift_decipher(text, shift):
    result = ""
    for char in text:
        if char == " ":
            result += " "
        else:
            shifted = (ord(char) - ord('A') - shift) % 26
            result += chr(shifted + ord('A'))
    return result

# Question 4
def rail_encipher(text):
    rail1 = text[::2]
    rail2 = text[1::2]
    
    return rail1 + rail2

# Question 5
def rail_decipher(text):
    n = len(text)
    rail1_length = (n + 1) // 2
    rail1 = text[:rail1_length]
    rail2 = text[rail1_length:]
    result = ""
    i1, i2 = 0, 0
    for i in range(n):
        if i % 2 == 0:       
            result += rail1[i1]
            i1 += 1
        else:               
            result += rail2[i2]
            i2 += 1
    return result
