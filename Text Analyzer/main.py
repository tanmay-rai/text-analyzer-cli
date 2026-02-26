import analyzer
def main():
    inputstring= str(input("Enter the whole text: "))
    inputstring= " ".join(inputstring.split())
    if not inputstring:
        print("No text provided. Please enter some text.")
        return 
    cleaned=analyzer.clean_text(inputstring)
    print("Text analysis result: ")
    
    #Character and Sentences
    sentencecount = analyzer.sentence_count(inputstring)
    characterdict= analyzer.character_count(inputstring)
    print(f"{'Sentences: ':<35}{sentencecount:^10} ")
    print(f"{'Total Character: ':<35}{characterdict['Total Character']:^10} ")
    print(f"{'Characters (no spaces): ':<35}{characterdict['Characters (no spaces)']:^10} ")
    print(f"{'Alphabetic Character: ':<35}{characterdict['Alphabetic Character']:^10} ")
    print(f"{'Digits: ':<35}{characterdict['Digits']:^10} ")
    print(f"{'Special Character: ':<35}{characterdict['Special Character']:^10} ")
    
    #Words
    worddict = analyzer.word_frequency(cleaned)
    longestwrd= analyzer.longest_word(cleaned)
    frequentwrd = analyzer.most_frequent_word(worddict)
    print(f"\n{'Total Words: ':<35}{sum(worddict.values()):^20} ")
    if longestwrd!="":
        print(f"{'Longest Word: ':<35}{longestwrd:^20} ")
    else: 
        print(f"{'Longest Word: ':<35}{'N/A':^20} ")
    if frequentwrd!=None:
        print(f"{'Most Frequent Word: ':<35}{frequentwrd:^20} ")
    else:
        print(f"{'Most Frequent Word: ':<35}{'N/A':^20} ")
if __name__ == "__main__":
    main()
