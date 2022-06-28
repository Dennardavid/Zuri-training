# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #creating dictionares to hold word and anagram characters 
    word_dict = {}
    anagram_dict = {}
    
    #using for loop to update dictionary
    for x in word:
        if x not in word_dict.keys():
            counts_word[x] = 1
        
    #using for loop to update dictionary
    for x in anagram:
        if x not in anagram_dict.keys():
            counts_anagram[x] = 1
        
    #comparing dictionaries and returning equivalent results    
    return True if word_dict == anagram_dict else False
    

#collecting user inputs
first_word = input("Enter your first word :")
second_word = input("Enter your second word :")

#passing argument to function
print(find_anagram(first_word,second_word ))