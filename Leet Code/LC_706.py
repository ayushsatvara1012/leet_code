from future.moves.urllib.request import to_bytes


class Hashmap:
    def __init__(self):
        self.size = 100
        self.buckets =  [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        i = 0
        while i < len(bucket):
            existing_key,existing_value = bucket[i]
            if existing_key == key:
                bucket[i] = (key,value)
            i+=1
        bucket.append((key,value))


        return bucket

    def remove(self, key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        i = 0
        while i < len(bucket):
            existing_key,existing_value = bucket[i]
            if existing_key == key:
                bucket.pop(i)
        return

    def get(self,key):
        bucket_index = self._hash(key )
        bucket = self.buckets[bucket_index]

        i = 0
        while i< len(bucket):
            k,v = bucket[i]
            if k== key:
                return v
            i+=1
        return -1

    def display(self):
        return self.buckets

hm = Hashmap()
print(hm.put(4,5))
print(hm.display())

print(hm.put(2,3))
print(hm.display())

print(hm.get(6))
hm.remove(2)
print(hm.display())