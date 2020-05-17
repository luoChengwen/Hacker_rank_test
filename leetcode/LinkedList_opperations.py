class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = Node()

    def append(self, to_append_data):
        to_append_node = Node(to_append_data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = to_append_node

    def length(self):
        cur = self.head
        i = 0
        while cur.next != None:
            cur = cur.next
            i += 1
        return i

    def get_data(self, index):

        if index >= self.length():
            print('out of range')
            return None
        else:
            cur = self.head
            i = 0
            while True:
                cur = cur.next
                if i == index: return cur.data
                i += 1

    def delete(self, index):

        if index >= self.length():
            print('out of range')
            return None

        cur = self.head
        i = 0

        while cur.next != None:
            last_node = cur
            cur = cur.next
            if i == index:  last_node.next = cur.next
            i += 1

    def insert(self, index, val):
        cur = self.head

        i = 0
        while cur.next != None:
            last_node = cur
            cur = cur.next

            if i == index:
                last_node.next = Node(val)
                last_node.next.next = cur
            i+=1

    def display(self):
        ds = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            ds.append(cur.data)
        return ds

'''''# test
'''
#
test = LinkList()
output = test.append(1)
print(test.display())
test.append(2)
test.append(3)
test.append(4)
test.append(5)
test.append(6)
print(test.display())

print('length is: ',test.length())
print('the fourth data in the list is',test.get_data(4))

print(test.delete(2))
print(test.display())
print(test.insert(3,4.44))
print(test.display())