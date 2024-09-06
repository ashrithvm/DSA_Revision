# GFG link: https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1

def searchInSorted(self,arr, N, K):
    #Your code here
    for i in range(N):
        if arr[i]==K:
            return 1
    return -1