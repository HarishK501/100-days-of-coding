resultList = [] # holds nodes that donot have a sibling
def checkSibling(root, prev):
    global resultList
    if root:
        if prev != -1: # since root never has a sibling, it need not be in the resultList
            if not prev.left or not prev.right: # if parent node doesnot contain a left or right child, then the current node has no sibling. So, 
                resultList.append(root.data)
        prev = root
        checkSibling(root.left, prev)
        checkSibling(root.right, prev)



def noSibling(root):
    global resultList
    resultList = []
    checkSibling(root, -1) # updates the resultList
    if len(resultList) == 0: # if all nodes have a sibling, then the list will contain only -1.
        resultList.append(-1)
    return sorted(resultList) # sorting is done here only for understanding purpose.😅

#{ 
#  Driver Code Starts

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
#   print(ip)
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
    t=int(input("No. of test cases: "))
    for _ in range(0,t):
        s=input("Tree: (level-order form)= ")
        root=buildTree(s)
        ans = noSibling(root)
        print("Result:")
        for i in ans:
            print(i,end=" ")
        print("\n\n")

# } Driver Code Ends