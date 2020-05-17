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
            output = cur
            cur = cur.next

            if i == index:  output.next = cur.next
            i += 1

    def display(self):
        ds = []
        cur = self.head

        while cur.next != None:
            cur = cur.next
            ds.append(cur.data)


        print(ds)


'''''# test
'''

test = LinkList()
print(test.display())
test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
test.append(6)


print(test.length())
print(test.get_data(4))
print(test.display())
print(test.delete(2))
print(test.display())