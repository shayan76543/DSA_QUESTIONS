class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# preorder Traversing
# Rule: Root → Left → Right
def preorder(root):
    if root!=None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
# inorder Traversing 
# Rule:
# Left → Root → Right
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
# postorder traversing
# Rule:
# Left → Right → Root
def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
root=node(22)
root.left=(node(33))
root.right=(node(44))
root.left.left=(node(34))
root.left.right=(node(35))
root.right.left=(node(45))
root.right.right=(node(46))
preorder(root)
print()
inorder(root)
print()
postorder(root)