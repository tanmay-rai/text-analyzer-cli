import string
#This functions cleans up the text, removing punctuation, extra spaces and others..
def clean_text(text): 
    newtext=""
    for x in text:
        if x not in string.punctuation:
            newtext = newtext+x
    newtext=newtext.lower()
    newtext = " ".join(newtext.split())
    return newtext
#This function returns words freqency of the words in the sentence and returncs dict value
def word_frequency(text):
    words = text.split()
    freq = {}
    for x in words:
        if x in freq:
            freq[x]=freq[x]+1
        else:
            freq[x]=1
    return freq
#This function counts the number of characters in the text and returns dict value
#VERY IMPORTANT: THIS FUNCTION REQUIRE THE RAW TEXT
def character_count(text):
    freq={}
    freq["Total Character"]=0
    freq["Characters (no spaces)"]=0
    freq["Alphabetic Character"]=0
    freq["Digits"]=0
    freq["Special Character"]=0
    for x in text:
        freq["Total Character"]=freq["Total Character"]+1
        if x!=" ":
            freq["Characters (no spaces)"]=freq["Characters (no spaces)"]+1
        if x in string.ascii_letters:
            freq["Alphabetic Character"]=freq["Alphabetic Character"]+1
        if x in string.digits:
            freq["Digits"]=freq["Digits"]+1
        if x in string.punctuation:
            freq["Special Character"]=freq["Special Character"]+1
    return freq
#This function counts the number of sentence in the text, further enhancement needed, returns integer value
#VERY IMPORTANT: THIS FUNCTION REQUIRE THE RAW TEXT
def sentence_count(text):
    count=0
    for x in text:
        if x=="." or x=="!" or x=="?":
            count = count+1
    return count
#This function returns the longest word from the whole text, returns string value
def longest_word(text):
    wrds = text.split()
    count = -1
    largest=""
    for x in wrds:
        if len(x)>count:
            count = len(x)
            largest = x
    return largest
#This function accepts dict value as parameter, and returns most frequent word used in the text
def most_frequent_word(freq):
    if not freq:
        return None
    else:
        count = 0
        most_word=""
        for x in freq:
            if freq[x]>count:
                count = freq[x]
                most_word = x
        return most_word