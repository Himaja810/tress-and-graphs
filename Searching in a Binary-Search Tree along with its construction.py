#  searching key in binary search tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def searchInBST(root,target):
    if root==None:
        return False
    elif root.data==target:
        return True
    elif root.data<target:
        return searchInBST(root.right,target)
    return searchInBST(root.left,target)

def insertIntoBST(root, ele):
    if root == None:
        newBlock = TreeNode(ele)
        return newBlock

    if root.data < ele:
        root.right = insertIntoBST(root.right, ele)
    else:
        root.left = insertIntoBST(root.left, ele)
    return root


n=int(input())
nums = list(map(int,input().split()))
target1=int(input())

#      18
#   10    25
# 8  15 22  28

# preorder: 18, 10, 8, 15, 25, 22, 28
# inorder: 8 10 15 18 22 25 28
# postorder: 8 15 10 22 28 25 18


root = None
for ele in nums:
    root = insertIntoBST(root, ele)
#printPreorderTraversal(root)
#print()
#printInorderTraversal(root)
#print()
#printPostorderTraversal(root)

if searchInBST(root,target1)==True:
    print("Target element is found")
else:
    print("Target element is not found")

searchInBST(root,target1)
