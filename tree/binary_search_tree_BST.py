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
def get_successor(root):
    root=root.right
    while(root!=None and root.left!=None):
        root=root.left
    return root
def delete(root,value):
    if root==None:
        return root
    if root.data>value:
        root.left=delete(root.left,value)
    elif root.data<value:
        root.right=delete(root.right,value)
    else:
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left 
        else:
            succ=get_successor(root)
            root.data=succ.data
            root.right=delete(root.right,succ.data)
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
root=insert(None,20)
root=insert(root,15)
root=insert(root,12)
root=insert(root,18)
root=insert(root,30)
root=insert(root,25)
root=insert(root,50)
root=insert(root,40)
inorder(root)
print("\n")
delete(root,30)
inorder(root)





