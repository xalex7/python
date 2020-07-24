def main():
    def is_vowel(c):
        if c in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            return True
        else:
            return False
    def modified(ad):
        vowel_less_ad = ""
        for i in range(len(ad)):
            if ad[i - 1] == " ":
                vowel_less_ad += ad[i]
            elif is_vowel(ad[i]) == False:
               vowel_less_ad += ad[i]

        return vowel_less_ad
    
    ad = "Desirable unfurnished flat in quiet residential area" 
    print(modified(ad)) #Printing the function just to make it easy for you to see the result;
main()

    
    
                