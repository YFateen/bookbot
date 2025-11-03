def get_word_count(text):

    words = text.split()
    wordCount = len(words)
    return wordCount

def get_letter_count(text):
    letterDictionary = {}
    for letters in text:
        if not letters.lower() in letterDictionary:
            letterDictionary[letters.lower()] = 0
        letterDictionary[letters.lower()] += 1
    
    return letterDictionary

def sort_on(items):
    return items["num"]

def sort_list(dictionary):
  
    newlist = []

    for items in dictionary:
        if(items in dictionary):
            if(items.isalpha() == False):
                continue
            newDictionary = {}
            newDictionary["char"] = items
            newDictionary["num"] = int(dictionary[items])
            newlist.append(newDictionary)
    
    newlist.sort(reverse=True, key=sort_on)
        
    return newlist

