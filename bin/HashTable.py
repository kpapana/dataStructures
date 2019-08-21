"""
Author : Karthik Papana

Implementation of hash table in Python
This class uses python's default hash() function to calculate the prehash which is further used in index calculation
It uses separate chaining method for conflict resolution

hash_func()     - return the hashed key values of input key
set()           - adds key, value pairs to the hash table
get()           - gets corresponding value of key input
delete_key()    - deletes the given key and raises keyError if key not found. Use only if you know that key exists
is_keyExists()  - returns true if give key exists else false
__rehash()      - it should automatically increase the size of hash table
__get_size()    - returns size of hash table. Later it will be used to decide if rehashing is required

Usage:
    h=HashTable()
    h[<key>]=<value>

TODO: Take conflict resolution method as input and perform corresponding resolution.
TODO: Take input to define rehashing method. It can choose between all at once rehashing or incremental rehashing

"""


class HashTable:
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for i in range(0, self.size)]
        self.enable_rehash = False
        self.__DIVIDE_FACTOR = 3
        self.__MULTIPLIER = 3
        self.__KEYERROR = "Key {} not found in hash table"

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        # check if hash table is filled atleast 2/3rd of total size
        if self.__get_size() >= (self.size-(self.size//self.__DIVIDE_FACTOR)):
            self.__rehash()
        hashed_key = self.hash_func(key)
        key_exists = False
        slot = self.hashmap[hashed_key]
        i = 0
        for i, kv in enumerate(slot):
            k = kv[0]
            if key == k:
                key_exists = True
                break
        if key_exists:
            slot[i] = (key, value)
        else:
            slot.append((key, value))

    def get(self, key):
        hashed_key = self.hash_func(key)
        slot = self.hashmap[hashed_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
        raise KeyError(self.__KEYERROR.format(key))

    def delete_key(self, key):
        hashed_key = self.hash_func(key)
        slot = self.hashmap[hashed_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if k == key:
                slot.pop(i)
                return True
        raise KeyError(self.__KEYERROR.format(key))

    def is_keyExists(self, key):
        hashed_key = self.hash_func(key)
        slot = self.hashmap[hashed_key]
        if slot is not None:
            for kv in slot:
                k = kv[0]
                if k == key:
                    return True
        return False

    def __rehash(self):
        self.size = self.size*self.__MULTIPLIER
        temp_hashmap = [[] for i in range(0, self.size)]
        for slot in self.hashmap:
            if slot is not None:
                for kv in slot:
                    key, value = kv
                    hashed_key = self.hash_func(key)
                    key_exists = False
                    new_slot = temp_hashmap[hashed_key]
                    i = 0
                    for i, kv in enumerate(new_slot):
                        k = kv[0]
                        if key == k:
                            key_exists = True
                            break
                    if key_exists:
                        new_slot[i] = (key, value)
                    else:
                        new_slot.append((key, value))
        self.hashmap = temp_hashmap

    def __get_size(self):
        occup_size = 0
        for slot in self.hashmap:
            if slot is not None:
                occup_size += len(slot)
        return occup_size

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)
