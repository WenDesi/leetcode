class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.timer = 0
        self.cache_count = 0
        self.capacity = capacity
        self.result = {}
        self.key_time = {}

    def get(self, key):
        """
        :rtype: int
        """
        self.timer += 1
        if key not in self.result:
            return -1
        self.key_time[key] = self.timer
        return self.result[key]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.timer += 1

        if key in self.result:
            self.result[key] = value
            self.key_time[key] = self.timer
            return

        if self.cache_count < self.capacity:
            self.cache_count += 1
            self.result[key] = value
            self.key_time[key] = self.timer
        else:
            llist = list(self.result)

            mmin = 2147483647
            index = 0
            for ele in llist:
                if self.key_time[ele] < mmin:
                    mmin = self.key_time[ele]
                    index = ele

            self.key_time.pop(index)
            self.result.pop(index)
            self.result[key] = value
            self.key_time[key] = self.timer