# Word Composition Problem
Approach:
A compounded word is a word that can be constructed by combining shorter words found in list.
1)	A set, `word_set`, is created from the list of words. So, the search time can be reduced. Each word in the input and “word_set” is passed into the “is_compound()” function.

2)	The goal of “is_compound()” function is to tell whether a word is compounding word or not. This function splits the word into two parts: - prefix and suffix of varying length.

    i)	If both prefix and suffix parts are present in the “word_set “ then the word is compounding word, so function returns True.  Or,
    
    ii)	If prefix part is in “word_set” and suffix can be further divided into multiple words found in “word_set”, the function returns True.

3)	Else, in all other conditions function will return False.
4)	All the compounding words then are stored in a result list.
5)	Longest and second longest words are picked from the list and returned with the execution time.

