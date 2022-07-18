
f = open("birds.txt","r")
data = f.read()
f.close()

def count_words(data):
    words = data.split(" ")
    num_words = len(words)
    return num_words


num_words = count_words(data)
print("The number of words: ", num_words)
