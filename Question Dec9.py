# Black and White
# Given the chessboard dimensions. Find out the number of ways we can place a black and a white Knight on this chessboard such that they cannot attack each other.

# Note:
# The knights have to be placed on different squares. A knight can move two squares horizontally and one square vertically (L shaped),
# or two squares vertically and one square horizontally (L shaped). The knights attack each other if one can reach the other in one move.

# Input :
# N = 2, M = 2

# Output :
# 12

# Explanation :
# There are 12 ways to place knights on the board such that they cannot attack each other.

# Your Task:
# Your task is to complete the function numOfWays() which takes the dimensions of the chessboard as input parameters
# and returns the number of ways to place the knights such that they cannot attack each other.


def valid(i,j,n,m): #checking the probable position of knight is feasible on chess
    return i>=0 and j>=0 and i<n and j<m

def numOfWays(M, N):
    # code here
    mod=1000000007
    ans=0

    dirs=[[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]] #possible directions where knight can go

    for i in range(N):
        for j in range(M):
            total=N*M
            minus=1
            for x in dirs:
                if valid(i+x[0],j+x[1],N,M):
                    minus+=1

            total-=minus
            ans=(ans+total)%mod

    return (ans%mod)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m,n = map(int,input().strip().split())
        print(numOfWays(m,n))

# } Driver Code Ends