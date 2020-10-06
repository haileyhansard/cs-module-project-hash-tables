#The keys are the words
#The values will be how many times each word appears
#Need to split the string input into words - can use split()

#INPUT: string of words
#OUTPUT: dictionary with key:value pairs as word: count

def word_count(s): #s is the original INPUT string
    # Your code here
    cache = {}
    # count = 0
    splitUpWords = s.split() #this is splitting up the words into separate indexes, creating a new string called splitUpWords
    #print(splitUpWords)

    for word in splitUpWords:
        word = word.lower()
        if word.isspace():
            continue
        
        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1

        word = word.isalpha()
    return cache

    # for word in splitUpWords:
    #     word = word.lower()
    #     cache[word] = splitUpWords.count(word)




    # if word not in dic:
    #     return dic
    # for word in s:
    #     if 


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))