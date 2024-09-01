#create a function for word count
def word_count(text):
    words=text.split()

    return len(words)

#input from user
text=input("enter your text :")


count_words=word_count(text)

#print no of words
print(f"Number of words are: { count_words}")




