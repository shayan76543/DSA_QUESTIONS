class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insertion(root,value):
    if root is None:
        return node(value)
    if root.data==value:
        return root
    if root.data>value:
        root.left=insertion(root.left,value)
    else:
        root.right=insertion(root.right,value)
    return root 
def searching(root,value):
    if root is None:
        return False
    if root.data==value:
        return True
    if root.data>value:
        return searching(root.left,value)
    else:
        return searching(root.right,value)
def get_successor(root):
    root=root.right
    while root!=None and root.left is not  None:
        root=root.left
    return root

def deletion(root,value):
    if root==None:
        return "Empty List"
    if root.data>value:
        root.left=deletion(root.left,value)
    elif root.data<value:
        root.right=deletion(root.right,value)
    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            succ=get_successor(root)
            root.data=succ.data
            root.right=deletion(root.right,succ.data)
    return root


        
        
    
