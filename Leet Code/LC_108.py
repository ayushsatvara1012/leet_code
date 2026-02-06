class Treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def convertToBinaryTree(n):
    mid = len(n)//2
    root = Treenode(n[mid])

    root.left = convertToBinaryTree(n[:mid])
    root.right = convertToBinaryTree(n[mid+1:])

    return root
print(convertToBinaryTree([1,2,3,4,5,6,7,8,9,10]))