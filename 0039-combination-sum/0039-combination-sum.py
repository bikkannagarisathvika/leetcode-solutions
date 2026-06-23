class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(index,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target or index==len(candidates):
                return
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path,total+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna