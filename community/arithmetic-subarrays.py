class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        index={}
        for i in range(len(r)):
            index[i]=nums[l[i]:r[i]+1] 
        for i in index.keys():
            a=index[i]
            a.sort()
        ans=[]
        for i in index.keys():
            change=index[i][1]-index[i][0]
            for j in range(1,len(index[i])):
                diff=index[i][j]-index[i][j-1]
                boolean=True
                if(change!=diff):
                    boolean=False
                    ans.append(boolean)
                    break 
            if boolean != False:
                ans.append(True)

        return(ans)
                    