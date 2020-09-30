class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
#you could have 8 LinkedLists at a time because we have 8 slots, and each slot contains a LL

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

# Note: the ratio of the number of pairs to the number of buckets is called the load factor
# Load Factor = number of pairs / number of buckets
# Another word for buckets is 'slots' in the array

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity 
        self.table = [None] * self.capacity
        self.total = 0



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # DAY 2 
        load_factor = self.total/self.capacity

        if load_factor > 0.7:
            self.resize(self.capacity*2)

        return load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c) 
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # DAY 1
        # index = self.hash_index(key) #get the index
        # self.table[index] = value #at the index in the table, store the value
        # #to save key somewhere, need to use LinkedList, utilize key, will be helpful for collisions.
        
        # self.total += 1 #increment the total # of slots filled by 1

        # DAY 2
        #Hash the key and Get the index for the key
        #Search the LL at that index for the key
        #If the key is found, overwrite the value stored there
        #Else, insert the new HashTableEntry key and value at the head of the list at that index
        index = self.hash_index(key)

        if self.table[index] is None:
            self.table[index] = HashTableEntry(key, value)
        else:
            cur = self.table[index]
            if cur.key == key:
                cur.value = value
            else:
                while cur.next is not None:
                    if cur.next.key == key:
                        cur.next.value = value
                    cur = cur.next
                cur.next = HashTableEntry(key, value)
        self.total += 1
        self.get_load_factor()


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # DAY 1
        # if not self.hash_index(key): #if the key at index is not found
        #     print('key is not found')
        
        # index = self.hash_index(key)
        # self.table[index] = None #this will essentially remove the value at index because its now set to None

        # self.total -= 1 #decrement the total # of slots filled

        # DAY 2
        #Hash the key and get an index
        #Search through the LL for the matching key at that index
        #If found, Delete that node
        #Return the value of the deleted node (Else, if not found, return None)
        #moving two pointers along
        index = self.hash_index(key)
        prev = self.table[index]
        cur = prev.next

        if prev is None:
            print('Key not found')
        if prev.key == key:
            deleted_node = self.table[index]
            self.table[index] = prev.next

            self.total -= 1
            self.get_load_factor()
            return deleted_node

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                cur.next = None

                self.total -=1
                self.get_load_factor()

                return cur

            prev = cur
            cur = cur.next ####need to check against Artem's lecture if this is correctly finished?

        print("Key not found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # DAY 1
        # index = self.hash_index(key)

        # if not self.table[index]:
        #     return
        # else:
        #     return self.table[index]
        
        # DAY 2
        index = self.hash_index(key)
        cur = self.table[index]

        if cur is None:
            return
        
        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        #If load factor is 0.7, then double the size of hash table capacity.
        #Make a new array that is DOUBLE the current size of hash table
        #Re-populate the new array, go through each item (LL) in the array, and re-hash it (because hash index is based on the length!)
        #Insert the items into their new locations

        new_table = HashTable(new_capacity)

        for node in self.table:
            if node is not None:
                new_table.put(node.key, node.value)
        self.capacity = new_capacity
        self.table = new_table.table


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")