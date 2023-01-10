class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        splitted_num1=num1.split("+")
        splitted_num2=num2.split("+")

        real1=int(splitted_num1[0])
        img1=int(splitted_num1[1][:-1])

        real2=int(splitted_num2[0])
        img2=int(splitted_num2[1][:-1])

        real_term= (real1*real2) - (img1*img2)
        img_term= real1 * img2 + real2 * img1
        
        return(f'{real_term}+{img_term}i')
