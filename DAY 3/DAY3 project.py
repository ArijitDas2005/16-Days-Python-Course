text=input("Enter a text: ")
letters=[]

text=text.lower()
letters.append(input("Enter 1st letter: ").lower())
letters.append(input("Enter 2nd letter: ").lower())
letters.append(input("Enter 3rd letter: ").lower())

print("\n")
print("LETTER REPETITIONS")

letter_repetition1= text.count(letters[0])
letter_repetition2= text.count(letters[1])
letter_repetition3= text.count(letters[2])

print(f"We have found the letter '{letters[0]}' repeated {letter_repetition1} times")
print(f"We have found the letter '{letters[1]}' repeated {letter_repetition2} times")
print(f"We have found the letter '{letters[2]}' repeated {letter_repetition3} times")

print("\n")
print("NUMBER OF WORDS")

words=text.split()
print(f"We have found the {len(words)} words in your text")

print("\n")
print("FIRST AND LAST LETTER")

first_letter= text[0]
last_letter= text[-1]
print(f"The initial letter is '{first_letter}', the final letter is '{last_letter}'")

print("\n")
print("INVERTED TEXT")

words.reverse()
inverted_text= ''.join(words)
print(f"If we order your text backwards it will say '{inverted_text}'")

print("\n")
print("LOOKING FOR THE WORD PYTHON")

is_python= 'Python' in text
dic={True: "was", False: "was not"}

print(f"The word 'Python' {dic[is_python]} found in the text")
