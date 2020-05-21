class Node:
    def __init__(self, val=None):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert(self, data):

        if self.val == data:
            print('already exist')
            return False

        elif self.val > data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True

        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def find(self, data):
        if self.val == data:
            print('found')
            return True

        elif self.val < data:
            if self.right_child: return self.right_child.find(data)
            else: return False

        else:
            if self.left_child: return self.left_child.find(data)
            else: return False

    def inorder(self):
        if self:
            if self.left_child: self.left_child.inorder()
            print(self.val)
            if self.right_child: self.right_child.inorder()




    def preorder(self):
        if self:
            print(self.val)
            if self.left_child: self.left_child.preorder()
            if self.right_child: self.right_child.preorder()

    def postorder(self):
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(str(self.val))

    # def postorder(self):
    #     if self:
    #         if self.left_child: self.left_child.postorder()
    #         if self.right_child: self.right_child.postorder()
    #         print(str(self.val))


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            self.root.find(data)
        else:
            return False

    '''
            1
           / \
          2   3
         / \
        4   5

    inorder: left - root - right 42513
    preorder: root - left - right 12453
    postoder: left - right - root 45231

    '''

    def inorder(self):
        self.root.inorder()

    def preorder(self):
        self.root.preorder()

    def postorder(self):
        self.root.postorder()

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)

        else:
            print('not in the tree')
            return False

    def inorder(self):
        self.root.inorder()

    def preorder(self):
        self.root.preorder()

    def postorder(self):
        self.root.postorder()

    '''
    binary tree
            1
           / \
          2   3
         / \
        4   5

    inorder: left - root - right 42513
    preorder: root - left - right 12453
    postoder: left - right - root 45231


    binary search tree
    
             5
           /   \
          3     7
         /     
        1    
         \
          2
          
    inorder: left - root - right 12357
    preorder: root - left - right 53127
    postoder: left - right - root 21375

    '''

test = BST()
test.insert(5)
test.insert(3)
test.insert(7)
test.insert(1)
test.insert(2)


'''

    binary search tree
    
             5
           /   \
          3     7
         /     /  
        1     6
         \
          2
          
    inorder: left - root - right 123567
    preorder: root - left - right 531276
    postoder: left - right - root 213675

    '''
test = BST()
test.insert(5)
test.insert(3)
test.insert(7)
test.insert(1)
test.insert(2)
test.insert(6)

test.find(5)
test.postorder()
