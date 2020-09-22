class Solver:
    def __init__(self):
        self.x = 0
        self.result = -1


    def KthSmallestElementUtil(self, root, K):
        if root:
            self.KthSmallestElementUtil(root.left, K)
            
            self.x = self.x + 1
            
            if self.x == K:
                self.result = root.data
                
            self.KthSmallestElementUtil(root.right, K)
        return

    def printResult(self, root, K):
        self.KthSmallestElementUtil(root, K)
        return self.result
        
# Return the Kth smallest element in the given BST 
def KthSmallestElement(root, K): 
    return Solver().printResult(root, K)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input("No. of testcases: "))
    for _ in range(0,t):
        s=input("Tree list(level-order): ")
        root=buildTree(s)
        k1=int(input("K: "))
        print(KthSmallestElement(root, k1))
        
# } Driver Code Ends