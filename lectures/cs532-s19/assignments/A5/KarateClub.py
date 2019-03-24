import matplotlib.pyplot as plt
from networkx.algorithms.community.centrality import girvan_newman
import networkx as nx
from matplotlib.pyplot import figure
import copy


def most_central_edge(G):
    centrality = nx.edge_betweenness_centrality(G, weight='weight')
    return max(centrality, key=centrality.get)


def disconnected_graph():
    G = nx.karate_club_graph()
    print("Node Degree")
    for v in G:
        print('%s %s' % (v, G.degree(v)))
    comp = girvan_newman(G,most_valuable_edge=most_central_edge)
    partition_dict = {}
    list_items = []
    for c in next(comp):
        print(c)
        list_items.append(list(c))
    for items in list_items:
        for i in items:
            partition_dict[i] = list_items.index(items)

    print(partition_dict)


    labels = {}

    for i in range(0, G.number_of_nodes()):
        labels[i] = i
        if i == 0:
            labels[i] = "Mr. Hi"
        elif i == 33:
            labels[i] = "John A."

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=600 ,cmap=plt.cm.RdYlBu, node_color=list(partition_dict.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, labels,font_size=16)

    plt.axis('off')
    plt.show()


def connected_graph():
    G = nx.karate_club_graph()
    pos = nx.spring_layout(G)
    print("Node Degree")
    for v in G: print('%s %s' % (v, G.degree(v)))
    labels = {}

    for i in range(0, G.number_of_nodes()):
        labels[i] = i
        if i == 0:
            labels[i] = "Mr. Hi"
        elif i == 33:
            labels[i] = "John A."
    nx.draw_networkx(G, pos, with_labels=False)
    nx.draw_networkx_labels(G, pos, labels, font_size=16)
    plt.axis('off')
    plt.show()


def multiple_iterations():
    G = nx.karate_club_graph()
    print("Node Degree")
    for v in G:
        print('%s %s' % (v, G.degree(v)))
    # comp = girvan_newman(G,most_valuable_edge=most_central_edge)
    comp = girvan_newman(G)
    comp1 = girvan_newman(G)
    comp2 = girvan_newman(G)
    list_items = []
    for c in comp:
        list_temp = []
        for itr in c:
            list_temp.append(list(itr))
        list_items.append(list(list_temp))
    counter = 0
    for items in list_items:
        print("Iteration")
        partition_dict = {}
        for i in items:
            for j in i:
                partition_dict[j] = items.index(i)
        print(partition_dict)
        temp_G = copy.deepcopy(G)
        print(temp_G.edges())
        for key_i in partition_dict:
            for key_j in partition_dict:
                if temp_G.has_edge(key_i, key_j) and partition_dict[key_i] != partition_dict[key_j]:
                    temp_G.remove_edge(key_i, key_j)
        labels = {}
        print(temp_G.edges())
        for i in range(0, temp_G.number_of_nodes()):
            labels[i] = i
            if i == 0:
                labels[i] = "Mr. Hi"
            elif i == 33:
                labels[i] = "John A."
        if counter > 1:
            figure(figsize=(20, 20))
        else:
            figure(figsize=(15, 15))
        pos = nx.spring_layout(temp_G)
        nx.draw_networkx_nodes(temp_G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=list(partition_dict.values()))
        nx.draw_networkx_edges(temp_G, pos, alpha=0.3)
        nx.draw_networkx_labels(temp_G, pos, labels, font_size=16)

        plt.axis('off')
        file_name = "Girvan_Newman" + str(counter) + ".png"
        plt.savefig(file_name)
        if counter < 4:
            counter = counter + 1
        else:
            exit()

    '''
    print(partition_dict)


    labels = {}

    for i in range(0, G.number_of_nodes()):
        labels[i] = i
        if i == 0:
            labels[i] = "Mr. Hi"
        elif i == 33:
            labels[i] = "John A."

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=600 ,cmap=plt.cm.RdYlBu, node_color=list(partition_dict.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, labels,font_size=16)

    plt.axis('off')
    plt.show()
    '''

multiple_iterations()
# connected_graph()
# disconnected_graph()


