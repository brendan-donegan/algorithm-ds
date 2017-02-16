class UnionFind:

    def __init__(self, num):
        self.items = list(range(num))

    def union(self, p, q):
        """
        int p: the first item to connect
        int q: the second item to connect
        """
        p_id = self.items[p]
        q_id = self.items[q]
        for i in range(len(self.items)):
            if self.items[i] == p_id:
                self.items[i] = q_id

    def connected(self, p, q):
        """
        int p: the first item to check if connected to
        int q: the second item
        return True if connected, otherwise False
        """
        return self.items[p] == self.items[q]
