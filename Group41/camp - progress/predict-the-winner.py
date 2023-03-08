class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def checkPossibilities(left,right):
            if left > right:
                return 0

            choice1 = nums[left] + min(checkPossibilities(left + 2,right),checkPossibilities(left + 1,right - 1))
            choice2 = nums[right] + min(checkPossibilities(left + 1,right - 1),checkPossibilities(left,right - 2))
            return max(choice1 , choice2)

        
        return 2*checkPossibilities(0,len(nums)-1) >= sum(nums) 

    
# 6% solution 
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def checkPosibilites(left,right,player1,player2,turn):
            if left > right:
                return player1 >= player2

            if turn:
                player1_choice1 = checkPosibilites(left + 1,right,player1 + nums[left],player2,not turn)
                player1_choice2 = checkPosibilites(left,right - 1 ,player1 + nums[right],player2,not turn)
                return player1_choice1 or player1_choice2
            else:
                player2_choice1 = checkPosibilites(left + 1,right,player1 ,player2 + nums[left],not turn)
                player2_choice2 = checkPosibilites(left,right - 1 ,player1 ,player2 + nums[right],not turn)
                return player2_choice1 and player2_choice2

        
        return checkPosibilites(0,len(nums)-1,0,0,True)




        