class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def preorder(root):
    if root!=None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
root=node(22)
root.left=(node(33))
root.right=(node(44))
root.left.left=(node(34))
root.left.right=(node(35))
root.right.left=(node(45))
root.right.right=(node(46))
preorder(root)