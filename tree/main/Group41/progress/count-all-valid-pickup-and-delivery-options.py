class Solution:
    def countOrders(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        @cache
        def dp(picked, delivered):
            if picked == 0 == delivered:
                return 1
            
            if picked == 0:
                return ( delivered * dp( 0 , delivered - 1)) 

            if delivered == 0:
                return (picked * dp(picked - 1, 1)) 

            return (delivered * dp(picked, delivered - 1) + picked * dp(picked - 1, delivered + 1)) % modulo  
        return dp(n, 0) % modulo