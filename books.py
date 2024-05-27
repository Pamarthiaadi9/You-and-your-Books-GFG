
class Solution:
    def max_Books(self, n, k, arr):
        # code here
        ans = 0
        curr = 0
        i = 0
        while i < n:
            if arr[i] <= k:
                curr += arr[i]
            else:
                curr = 0
            
            ans = max(ans, curr)
            i += 1
        return ans

