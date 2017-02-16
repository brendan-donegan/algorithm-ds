#!/usr/bin/python3
import sys
from uf import UnionFind

def main():
    import pdb; pdb.set_trace()
    with open(sys.argv[1]) as pairs:
        num_pairs = [pair.strip() for pair in pairs.readlines()]
    union_find = UnionFind(len(num_pairs))
    for pair in num_pairs:
        p, q = [int(x) for x in pair.split(' ')]
        if not union_find.connected(p, q):
            union_find.union(p, q)
            print(p, q)

if __name__ == "__main__":
    main()
