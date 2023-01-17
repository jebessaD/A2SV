class Solution:
    def sortSentence(self, s: str) -> str:
        
        word=''
        number=""
        sentence=s.split(" ")
        for letter in s:
            if letter.isdigit():
                
                number+=letter
                if letter == s[-1]:
                    sentence[int(number)-1]=word
                
            else:
                
                if letter !=" ":
                    word +=letter
                
                else:
                    sentence[int(number)-1]=word
                    word=""
                    number=""
   
        return(' '.join(map(str, sentence)))      