#open text file and read the file 
f = open("birds.txt","r")
data = f.read()
f.close()

#count words function
def count_words(data):
    words = data.split(" ")
    num_words = len(words)
    return num_words


# count lines functions 
def count_lines(data):
    lines = data.split("\n")
 # remove empty lines   
    for l in lines:
        if not l:
            lines.remove(l)
    return len(lines)        


num_words = count_words(data)
num_lines = count_lines(data)
print("The number of words: ", num_words)
print("The number of lines: ", num_lines)

