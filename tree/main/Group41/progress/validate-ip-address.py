class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        arrv4 = queryIP.split('.')
        arrv6 = queryIP.split(':')
        v4 = True
        v6 = True
        if len(arrv4) != 4:
            v4 = False
        if len(arrv6) != 8:
            v6 = False
        
        for num in arrv4:
            if not num.isnumeric():
                v4 = False
                break
            if len(str(int(num))) != len(num):
                v4 = False
                break
            if int(num) > 255 or int(num) < 0:
                v4 = False
                break
        a_to_f = {"a","b","c","d","e","f","A","B","C","D","E","F"}
        for chars in arrv6:
            if len(chars) > 4 or len(chars) < 1 :
                v6 = False
                break

            for let in chars:
                if not (let in a_to_f or let.isnumeric()):
                    v6 = False
                    break
                if not v6:
                    break
                

        if v4: 
            return "IPv4"
        elif v6:
            return "IPv6"

        return "Neither"

                


        
        