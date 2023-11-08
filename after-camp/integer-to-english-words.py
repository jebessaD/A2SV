class Solution:
    def numberToWords(self, num: int) -> str:
        stack=[]
        underTwenty =["One", "Two", "Three", "Four", "Five", 
                  "Six", "Seven", "Eight", "Nine","Ten", 
                  "Eleven", "Twelve", "Thirteen", "Fourteen",
                  "Fifteen", "Sixteen","Seventeen", "Eighteen", "Nineteen"]

        Tenth_words =["Twenty", "Thirty", 
                       "Forty", "Fifty", "Sixty", 
                       "Seventy", "Eighty", "Ninety"]

        def threeDigits(num):
            stack=[]
            if(num<1000):
                rem=num%100
                hun=num//100
            
                if(hun>=1):
                    stack.append(underTwenty[hun-1] + " Hundred")
                if(rem<20 and rem>0): 
                    stack.append(underTwenty[rem-1])
                elif(rem<100 and rem>=20):
                    stack.append(Tenth_words[rem//10 - 2])
                    if(rem%10 >0):
                        stack.append(underTwenty[rem%10 - 1])
                return stack
            else:
                big_nums=['Thousand', 'Million', 'Billion']
                for power, word in enumerate(big_nums, 1):
                    if num < 1000**(power+1):
                        return threeDigits(num//1000**power) + [word] + threeDigits(num%1000**power)
        
        
        if(num==0):
            return "Zero"
        return " ".join(threeDigits(num))
        
        