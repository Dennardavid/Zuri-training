# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here

    with open("./story.txt","r") as openfile:
        read_file = openfile.read()
    return read_file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split(" ")
    word_count = {}

    for j in split_text:
        if j in word_count:
            word_count[j] +=1
        else:
            word_count[j] = 1
    return word_count    


    #return {"as": 10, "would": 20}

print(count_words())
