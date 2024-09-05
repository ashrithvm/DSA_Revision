# link: https://www.geeksforgeeks.org/problems/second-largest3735/1

#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        big=max(arr)
        second=-1
        for i in arr:
            if i>second and i<big: second=i
        return second


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends