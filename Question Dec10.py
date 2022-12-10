#User function Template for python3

class Solution:
    def buildLowestNumber(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if len(num) == k:
            return "0"
        stack = []
        for i in range(len(num)):
            while stack and k and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k:
            stack.pop()
            k -= 1
        return str(int("".join(stack)))

# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))