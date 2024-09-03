# recursive binary search tree

    def __r_contains(self,current_node,value):
        if current_node==None:
            return False
        if value==current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left,value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        

    def r_contains(self,value):
        return self.__r_contains(self.root,value)


    def __r_insert(self, current_node,value):
        if current_node==None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node        

    def r_insert(self,value):
        if self.root==None:
            self.root= Node(value)
        self.__r_insert(self.root,value)    
    
    def min_value(self,current_node):
        while current_node.left is not None:
            current_node=current_node.left
        return current_node.value    
    

    def __delete_node(self,current_node,value):
        if current_node ==None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left,value)
        elif value > current_node.value:
            current_node.right =  self.__delete_node(current_node.right,value)
        else:
            if current_node.left==None and current_node.right==None:
                return None
            elif current_node.left==None:
                current_node=current_node.right
            elif current_node.right==None:
                current_node=current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value=sub_tree_min 
                current_node.right = self.__delete_node(current_node.right,sub_tree_min)
        return current_node   

    def delete_node(self,value):
            self.__delete_node(self.root,value)




my_tree=BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
#my_tree.insert(18)
#my_tree.insert(27)
#my_tree.insert(52)
#my_tree.insert(82)
#my_tree.r_insert(92)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value,'\n')

my_tree.delete_node(47) 


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right)

#print(my_tree.min_value(my_tree.root))
#print(my_tree.min_value(my_tree.root.right))

#print(my_tree.r_contains(27))
#print(my_tree.r_contains(92))

#print(my_tree.contains(27),'\n')
#print(my_tree.contains(17),'\n')



''' AFTER DELETING A NODE IF YOU WANT TO ACCESS THE VALUES 
    THN U HVE TO USE THIS BELLOW CODE BCZ ABOVE CODE WILL GIVE YOU ATTRIBUT ERROR 

my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

# Before deletion
print(my_tree.root.value)         # Should print 2
print(my_tree.root.left.value)    # Should print 1
print(my_tree.root.right.value)   # Should print 3

# Delete the root node (2)
my_tree.delete_node(2)

# After deletion
if my_tree.root is not None:
    print(my_tree.root.value)  # Should now be 3, which is the in-order successor
else:
    print("Root is None")

if my_tree.root.left is not None:
    print(my_tree.root.left.value)  # Should print 1
else:
    print("Left child is None")

if my_tree.root.right is not None:
    print(my_tree.root.right.value)  # Right child might be None if the tree was small
else:
    print("Right child is None")
'''
