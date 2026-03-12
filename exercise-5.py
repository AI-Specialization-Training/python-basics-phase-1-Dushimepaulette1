# ============================================================================
# TODO: Use a For Loop with a Range 

#Create a function called repeat. 
# It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# ============================================================================
def repeat(words, count):
    newWord = ""
    for word in range(count):
         newWord += words
    return newWord
print(repeat("paulette\n", 5))