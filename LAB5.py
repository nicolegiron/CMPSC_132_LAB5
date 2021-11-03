#Lab #5
#Due Date: 03/20/2021, 11:59PM
'''
# Collaboration Statement:

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return ("Node({})".format(self.value))

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.numChildren(x.root)
        2
        >>> x.numChildren(x.root.left)
        2
        >>> x.numChildren(x.root.right)
        1
        >>> x.getMin
        2
        >>> x.getMax
        11
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.isEmpty()
        False
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)


    def isEmpty(self):
    	return self.root == None


    @property
    def getMin(self):
        root = self.root
        while root.left != None:
            root = root.left
        return root.value


    @property
    def getMax(self):
        root = self.root
        while root.right != None:
            root = root.right
        return root.value


    def getHeight(self, node):
        if self.root == None or node == None or node.left == None and node.right == None:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def __contains__(self,value):
        node = self.root
        while node != None:
            if node.value == value:
                return True
            elif node.value < value:
                node = node.right
            else:
                node = node.left
        return False



    def numChildren(self, node):
        if node.left != None and node.right != None:
            return 2
        elif node.left != None or node.right != None:
            return 1
        else:
            return 0
