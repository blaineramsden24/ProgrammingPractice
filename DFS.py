''' Depth First Search

3 Types:
PreOrder --> Start with the route and fully explore left most subtree
InOrder --> Explore left to right
PostOrder --> Start with the Fully explore the subtree before the root

2 Main approaches in python:
We can use the built in call stack (max 1000) with a recursive method uses the,
Or use an iterative method
'''

def walk(tree):
    if tree is not None:
        print(walk(tree))
        walk(tree.left)
        walk(tree.right)

'''
if we want to change from pre order to post order we just move the print statement to before, and if we want to use 
in order we can just swap the order of the tree.left and tree.right 
'''
