# The first line of input contains an integer,
# The second line contains  space-separated integers.
# The third line contains an integer,
# The fourth line contains  space-separated integers.

if __name__ == '__main__':
    m_size = int(input())
    m = input()
    n_size = int(input())
    n= input()

    lis_m = m.split()
    lis_n = n.split()
    newlist_m = set(list(map(int,lis_m)))
    newlist_n = set(list(map(int,lis_n)))

    newSetm = newlist_n.difference(newlist_m)
    newSetn = newlist_m.difference(newlist_n)
    newSet = newSetm.union(newSetn)

    lis = sorted(i for i in newSet)
    for i in lis:
        print(i)

