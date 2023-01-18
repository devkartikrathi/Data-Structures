class Node:

    def __init__(self, a=None):
        self.data = a
        self.next = None
        self.prev = None

class LinkedList:

    class sll:

        def __init__(self):
            self.head = None

        def insert(self, data):
            nnode = Node(data)
            if self.head:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = nnode
            else:
                self.head = nnode

        def delete(self):
            if not self.head:
                print("There is no element to remove")
            elif not self.head.next:
                self.head = None
            else:
                temp = self.head
                tmp = self.head
                while temp.next:
                    tmp = temp
                    temp = temp.next
                tmp.next = None

        def insert_at(self, data, posi):
            if (posi > len(self)+1) or posi<1:
                print("Enter a valid position")
            else:
                nnode = Node(data)
                count = 1
                if self.head:
                    if posi == 1 and len(self)>1:
                        nnode.next = self.head
                        self.head = nnode
                    else:
                        temp = self.head
                        tmp = self.head
                        while posi != count:
                            count+=1
                            temp = tmp
                            tmp = temp.next
                        temp.next = nnode
                        nnode.next = tmp

        def delete_from(self, posi):
            if len(self)>=posi:
                if posi == 1:
                    self.head = self.head.next
                else:
                    temp = self.head
                    count = 1
                    tmp = self.head
                    while count != posi:
                        tmp = temp
                        temp = temp.next
                        count +=1
                    tmp.next = temp.next

        def __len__(self):
            count = 0
            if self.head:
                count = 1
                temp = self.head
                while temp.next:
                    
                    temp = temp.next
                    count+=1
                return(count)
            else:
                return(count)

        def prnt(self):
            if self.head:            
                temp = self.head
                print(temp.data)
                while temp.next:
                    temp = temp.next
                    print(temp.data)
            else:
                print("No data available")

        def search(self, item):
            if len(self)>0:
                count=1
                temp = self.head
                if temp.data == item:
                    print("Element {} found at  position {}".format(item, count))
                else:
                    while temp.next:
                        temp = temp.next
                        count+=1
                        if temp.data == item:
                            print("Element {} found at position {}".format(item, count))
                            break
                        else:
                            print("Element {} not found".format(item))
                            break

    class dll:

        def __init__(self):
            self.head = None

        def insert(self, data):
            nnode = Node(data)
            if self.head:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = nnode
            else:
                self.head = nnode

    class csll:

        def __init__(self):
            self.head = None
            self.last = None

        def insert(self, data):
            nnode = Node(data)
            if self.last:
                temp = self.head
                while  temp.next != self.head:
                    temp = temp.next
                temp.next = nnode
                self.last = nnode
                self.last.next = self.head
            else:
                self.head = nnode
                self.last = self.head
                self.last.next = self.head

        def delete(self):
            if not self.last:
                print("There is no element to remove")
            elif self.head.next == self.head:
                self.head = None
                self.last = None
            else:
                temp = self.head
                tmp = self.head
                while temp.next != self.head:
                    tmp = temp
                    temp = temp.next
                self.last = tmp
                tmp.next = self.head

        def prnt(self):
            if self.last:
                temp = self.head
                print(temp.data)
                while temp.next != self.head:
                    temp = temp.next
                    print(temp.data)
            else:
                print("No data available")