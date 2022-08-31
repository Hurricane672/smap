from models import routeGetter
import networkx as nx
import matplotlib.pyplot as plt

def main(routeList):
    b=len(routeList);
    jiedian=[];
    lengthcount=[];
    for i in range(b):
       lengthcount.append(len(routeList[i]))

    for i in range(b):
        for j in range(lengthcount[i]):
          jiedian.append(routeList[i][j])

    print(jiedian)

    res = []
    for i in jiedian:
        if i not in res:
            res.append(i)

    print(res)

    t = []
    for i in range(len(res)):
        t.append([])
        for j in range(len(res)):
            t[i].append('1')
    print(t)

    s = []
    for i in range(len(res)):
        s.append([])
        for j in range(len(res)):
            s[i].append('0')
    print(s)

    lst=res
    for i in range(1, len(lst)):
            x = lst[i]
            left = 0
            right = i-1
            mid = int(right / 2)
            while left < right:
                if lst[mid] > x:
                    right = mid-1
                elif lst[mid] <= x:
                    left = mid+1
                mid = int((left + right) / 2)
            if lst[mid] <= x:
                index = mid+1
            else:
                index = mid

            for j in range(i, index, -1):
                lst[j-1], lst[j] = lst[j], lst[j-1]

    for i in range(b):
        for j in range(len(routeList[i]) - 1):
            s[res.index(routeList[i][j])][res.index(routeList[i][j + 1])]= '1'
    print(s)

    word = res
    A =s
    G = nx.DiGraph()

    num = len(res)
    nodes = []
    for i in range(num):
        nodes.append(word[i])
    for node in nodes:
        G.add_node(node)
    edges = []
    for i in range(num):
        for j in range(num):
            if A[i][j] == '1':
                sor = word[i]
                des = word[j]
                edges.append((sor, des))
            else:
                pass
    r = G.add_edges_from(edges)

    nx.draw(G, with_labels=True, node_color='y', )
    plt.show()

    print(A)


if __name__ == '__main__':
    targets = [['192.168.1.2','192.168.1.1'] , ['192.168.1.2'] , ['192.168.1.2','192.168.1.3']]
    main(targets)
