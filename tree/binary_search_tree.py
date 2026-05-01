class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def insert(root,value):
    if root is None:
        return node(value)
    if root.data==value:
        return root
    if root.data>value:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root
def search(root,value):
    if root is None:
        return ("Tree is empty")
    if root.data==value:
        return "Found Value in Tree"
    if root.data>value:
        return search(root.left,value)
    else:
        return search(root.right,value)
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
root=insert(None,33)
root=insert(root,445)
root=insert(root,23)
root=insert(root,412)
root=insert(root,61)
inorder(root)
print(search(root,11))




