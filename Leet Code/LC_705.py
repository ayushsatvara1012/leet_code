class Hashset:
    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self,key):
        return key%self.size

    def add(self,key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        if key not in bucket:
            bucket.append(key)
    def remove(self,key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)

    def contains(self,key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        return key in bucket