# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 12:36:09 2018

@author: zabiulla.khan

Implement a function longestWord() that takes a list of words and returns the longest
one.

"""
# Create/define a new function named longestWord which accepts list of words and returns longest one 
def longestWord(words_list):
    # Instantiate an empty list
    word_len = []
    #loop through the list of words recieved as inpput argument
    for n in words_list:
        #Append length of the word and word itself in word_len list
        word_len.append((len(n), n))
    #Sort the input list to return in ascending order    
    word_len.sort()
    #return the last word in the list "word_len" which is longest word
    return word_len[-1][1]

#Test the function longestword by passing the list of words
print(longestWord(["Apple", "Banana", "Pineapple","Mango"]))