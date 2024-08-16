#creating node class bcz it will repeat in all methods

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


#creating a linked list 

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


#print method in linkdlst

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        

#append method at the end

    def append(self, value):
        new_node = Node(value)
        if self.head is None: # == 0
            self.head= new_node
            self.tail= new_node
        else:
            self.tail.next = new_node
            self.tail= new_node
        self.length+= 1
        return True

#pop at the end method

    def pop(self):
        if self.length== 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-= 1
        if self.length==0:
            self.head= 0
            self.tail=0
        return temp
    
# prepend method adds node in the begining of a linkdlst

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head =new_node 
            self.tail = new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.length+=1
        return True    

# poping out first element or node frm linkdlst

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail==None
        return temp   

#get and set method for linkdlst

    def get(self,index):
        if index<0 or index>= self.length:
            return None
        temp=self.head
        for _ in range(index):
              temp= temp.next
        return temp
        
    def set_value(self, index, value):
        temp=self.get(index)
        if temp is not None:
            temp.value= value
            return True
        return False

# insert method in linkdlst

    def insert(self,index, value):
        if index<0 or index> self.length:
             return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node= Node(value)
        temp= self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

#remove method
    
    def remove(self,index):
        if index<0 or index>= self.length:
            return None
        if index==0:
            return self.pop_first()
        if index== self.length-1:
            return self.pop()
        prev= self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp

#reverse a linkdlist
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after

#calling linkdlst by giving values/ attributes

my_linked_list = LinkedList(2)

my_linked_list.append(3)

my_linked_list.prepend(1)
my_linked_list.append(4)
my_linked_list.append(5)

#print(my_linked_list.pop_first())

#print(my_linked_list.pop_first())

#my_linked_list.reverse()


my_linked_list.print_list()

