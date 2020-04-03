def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n-1)
print(recursive_sum(5))

# 12345
def digit_sum(n):
    if n == 0:
        return n
    return n % 10 + digit_sum(n//10)
print(digit_sum(333))

def word_split(phrase,list_of_words, output = None):
    '''
    Note: This is a very "python-y" solution.
    ''' 
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))