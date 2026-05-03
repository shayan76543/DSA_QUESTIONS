class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
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
    if root.data<value:
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

 
    