"""
Author : Karthik Papana

Implementation of HASH table in Python
This class uses python's default hash() function to calculate the index for hash
It uses separate chaining method for conflict resolution

hash_func() - return the hashed key values of input key
set() - adds key, value pairs to the hash table
get() - gets corresponding value of key input
__rehash() - it should automatically increase the size of hash table
__get_size() - returns size of hash table. Later it will be used to decide if rehashing is required

TODO: Take conflict resolution method as input and perform corresponding resolution.
TODO: Take input to define rehashing method. It can choose between all at once rehashing or incremental rehashing

"""


class HashTable:
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for i in range(0, self.size)]
        self.enable_rehash = False

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        if self.__get_size() >= (self.size-(self.size//3)):# check if hash table is filled atleast 2/3rd of total size
            self.__rehash()
        hashed_key = self.hash_func(key)
        key_exists = False
        slot = self.hashmap[hashed_key]
        i = 0
        for i, kv in enumerate(slot):
            k, v = kv
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
        raise KeyError("Key {} not found in hash table".format(key))

    def delete_key(self, key):
        hashed_key = self.hash_func(key)
        slot = self.hashmap[hashed_key]
        for i,kv in enumerate(slot):
            k,v = kv
            if k == key:
                slot.pop(i)
                return True
        raise KeyError('Key %s not found in hash table'.join(key))
        
    def __rehash(self):
        print("in rehash, current occupied size of hashtabe is {} and total space is {}".format(self.__get_size(),self.size))
        self.size = self.size*3
        temp_hashmap=[[] for i in range(0,self.size)]
        for slot in self.hashmap:
            if slot is not None:
                for kv in slot:
                    key,value = kv
                    hashed_key = self.hash_func(key)
                    key_exists = False
                    new_slot = temp_hashmap[hashed_key]
                    i = 0
                    for i, kv in enumerate(new_slot):
                        k, v = kv
                        if key == k:
                            key_exists = True
                            break
                    if key_exists:
                        new_slot[i] = (key, value)
                    else:
                        new_slot.append((key, value))
        self.hashmap=temp_hashmap
        print(self.hashmap)

    def __get_size(self):
        occup_size=0
        for slot in self.hashmap:
            if slot is not None:
                occup_size += len(slot)
        return occup_size

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)
