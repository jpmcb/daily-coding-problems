class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size
        self.data = [None] * size

    def put(self, key, val):
        hashVal = self.hashfunction(self, len(self.buckets))

        # if the bucket is empty
        if self.buckets[hashVal] == None:
            self.buckets[hashVal] = key
            self.data[hashVal] = val

        else:
            if self.buckets[hashVal] == key:
                self.data[hashVal] = val

            else:
                nextbucket = self.rehash(hashVal, len(self.buckets))
            
    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        pass
    
    