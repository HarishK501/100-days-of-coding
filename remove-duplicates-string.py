# Code for removing duplicates in a string
# Input : balloon
# Output: balon

# Input : aaabbbbcccccdddd
# Output: abcd

# Expected Time Complexity: O(|s|)
# Expected Auxiliary Space: O(constant)

# Constraints:
# 1 <= |S| <= 105
# S conatins lowercase english alphabets

class Solution:
    def removeDups(self, S):
        result = ''
        word_count_dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

        for i in range(0,len(S)):
            if word_count_dict[S[i]] == 0:
                word_count_dict[S[i]] += 1
                result += S[i]
            else:
                word_count_dict[S[i]] += 1

        return result
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input("No. of testcases: "))
	for i in range(T):
		s = input("Enter a string: ")
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer, "\n")


# } Driver Code Ends



   