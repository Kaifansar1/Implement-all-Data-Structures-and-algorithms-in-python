class SimpleHashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [None] * size
                                            
    def _hash(self, key):               #output will chnge every time u run....
        return hash(key) % self.size    #bcz using in built hash function
    
    def _hash2(self, key):
        # A simple custom hash function using the sum of character codes
        hash_value = 0      #output will not chnge by using this custom function
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size
    

    def print_table(self):
        for i, val in enumerate(self.table):
            print(i, ":",val)

    def set_item(self, key, value):
        index= self._hash(key)
        if self.table[index]==None:
            self.table[index]=[]
        self.table[index].append([key,value])    


my_ht=SimpleHashTable()
my_ht.set_item('bolts', 1400)
my_ht.set_item('washers', 50)
my_ht.set_item('lumber', 70)


my_ht.print_table()

'''''
To get consistent output across different runs of your program, you can either:

 1. Disable Hash Randomization:

      Set the PYTHONHASHSEED environment variable to a fixed value before running your program.

      You can do this by running your Python script with a fixed hash seed:

      PYTHONHASHSEED=0 python your_script.py


 2. Use a Custom Hash Function:

     Instead of relying on Python’s hash() function, you can implement a simple, consistent  hash function. 
     This way, you ensure that the same input will always produce the same hash output.     '''''