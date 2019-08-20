"""
Author : Karthik Papana

Implementation of HASH table in Python
This class uses python's default hash() function to calculate the index for hash
It uses separate chaining method for conflict resolution

hash_func() - return the hashed key values of input key
set() - adds key, value pairs to the hash table
get() - gets corresponding value of key input
rehash() - it should automatically increase the size of hash table
get_size() - returns size of hash table. Later it will be used to decide if rehashing is required

TODO: Take conflict resolution method as input and perform corresponding resolution.
TODO: Take input to define rehashing method. It can choose between all at once rehashing or incremental rehashing

"""


class HashTable:
    def __init__(self):
        self.size = 256
        self.hashmap = [[] for i in range(0, self.size)]

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    # TODO: consider rehashing method before adding items to hash table
    def set(self, key, value):
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
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                return v
        return

    # TODO: need to add logic to rehash
    def rehash(self):
        pass

    # TODO: returns the size of hash table
    def get_size(self):
        pass

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)
