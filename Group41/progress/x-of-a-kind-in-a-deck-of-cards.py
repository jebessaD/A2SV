class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        frequency = Counter(deck)

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)

        arr = list(frequency.values())
        curr_gcd = arr[0]
        for num in arr:
            curr_gcd = gcd(curr_gcd,num)
        if curr_gcd == 1:
            return False
        return True
