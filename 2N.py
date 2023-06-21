import networkx as nx
from itertools import chain, combinations
import matplotlib.pyplot as plt
import time

start_time = time.time()

G = nx.path_graph(20)


def neighbors(G):
    ng = {}
    for i in G.nodes():
        modng = list(G[i]) + [i]
        ng[i] = modng
    return ng


neighbors(G)
nbrs = neighbors(G)


def neighborsset(v):
    a = []
    for i in v:
        a += nbrs[i]
    return set(a)


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def subsets(G):
    i = []
    for node in powerset(G.nodes):
        i.append(tuple(node))
    return i


def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


cg = nx.Graph()


def configurationGraph(v):
    cg.add_nodes_from(v)

    edges_to_add = []  # List to store edges

    for i in cg.nodes:
        lis = list()
        if i != ():
            for j in i:
                lis += nbrs[j]
        lis = list(set(lis))
        rem_ver = list()
        rem_ver = Diff(list(G.nodes), list(i))
        for j in rem_ver:
            lis1 = lis + [j]
            edges_to_add.append((i, tuple(set(lis1))))  # Add edges to the list

    cg.add_edges_from(edges_to_add)  # Add edges outside the loop
    print("Burning Sequence :",nx.shortest_path(cg,source=(),target=v[-1]))
    print("Burning Number :",len(nx.shortest_path(cg,source=(),target=v[-1]))-1)
    #pos = nx.spring_layout(cg)
    #nx.draw(cg, pos)
    #labels = {node: node for node in cg.nodes}
    #nx.draw_networkx_labels(cg, pos, labels)

    #plt.show()

configurationGraph(subsets(G))

end_time = time.time()

print("Running time :",end_time-start_time)