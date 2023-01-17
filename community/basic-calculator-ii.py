class Solution:
    def calculate(self, s: str) -> int:
        arr=s.replace(" ","").replace("-","+-").split("+")
        # try to split(format) the string in to array of operations
        result=0
        stack=[]
        for i in arr:
            sign="p" #default set sign p is for positive and n is for negative
            if(i.isnumeric()):
                result +=(int(i))   # if the formatted arr is parsable to int
            else:
                if(i[0]=="-"):  # if the number is negative set sign to negative
                    sign="n"
                    i=i[1:len(i)] # then only take number without sign
                n=""
                for l,char in enumerate(i):  # loop in i and check if it is number or operands
                    if(char.isnumeric()):   #if it is number just concatnate
                        n+=char
                    if(not char.isnumeric() or l==len(i)-1):  # if it is not or loop is end
                        stack.append(n)                       # append the number
                        n=""
                        if (len(stack)==3):# check if lenth of stack is 3 if it is 3 we can perform mathematical operation
                            a=int(stack[0])
                            b=int(stack[2])
                            opp=0
                            if(stack[1]=="*"):
                                opp=a*b
                            else:
                                opp=a//b
                            stack=[]    # make stack empty 
                            stack.append(str(opp)) #and append the result 
                        if( l !=len(i)-1):  # append * or / to the stack
                            stack.append(char)
                        else:
                            break
                if(sign=="p"):        #check sign and perform addition or subtraction
                    result +=int(stack[0])
                else:
                    result -=int(stack[0])
                stack=[]
        return result
                    
                    
                        
                        