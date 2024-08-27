import networkx as nx
import matplotlib.pyplot as pl

def int_to_list (n):
    return map(int,str(n))

def nxt(n):
    ns = int_to_list(n)
    return sum( map(lambda x: x**2, ns) )

def happy(n):
    sad = [4, 16, 37, 58, 89, 145, 42, 20]
    list = []
    while n > 1 and (n not in sad):
          n = nxt(n)
          list.append(n)
    return n == 1 , list

values = []

G = nx.DiGraph()
G.add_node(1)

for sads in [20, 4, 16, 37, 58, 89, 145, 42, 20]:
    G.add_node(sads, label = sads)
    G.add_edge(sads, nxt(sads))
for i in range(1,10000):
    h,l = happy(i)
    #if h:
    #    print(":)",i,l)
    #else:
    #    print("  ",i,l)

    for j in l:
        if j not in values:
            G.add_node(j, label=j)
            G.add_edge(j,nxt(j))
            values.append(j)
#for n in G:
#    G.node[n]['name'] = n

pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'))
nx.draw_networkx_edges(G, pos)

pl.show()
