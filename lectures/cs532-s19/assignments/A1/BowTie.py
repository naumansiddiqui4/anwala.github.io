def bow_tie_structure():
    list_scc = []
    list_in = []
    list_out = []
    list_tendrils = []
    list_tubes = []
    list_disconnected = []
    outward_edges = []
    for row in range(0,len(graph)):
        outward_edges.append(False)
        # Check if in and out both entries present then SCC point
        for column in range(len(graph[0])):
            if graph[row][column] == 1:
                outward_edges[row] = True
                for row_check in range(0, len(graph)):
                    if graph[row_check][row] == 1:
                        if label_points(row) not in list_scc:
                            list_scc.append(label_points(row))
                        break
    for row in range(0, len(graph)):
        if label_points(row) not in list_scc:
            if outward_edges[row]:
                if label_points(row) not in list_scc:
                    for column in range(len(graph[0])):
                        if graph[row][column] == 1:
                            # Check if point is IN
                            # Has only outgoing edges to SCC
                            if label_points(column) in list_scc:
                                if label_points(row) not in list_in:
                                    list_in.append(label_points(row))
            else:
                for row_check in range(0, len(graph)):
                    if graph[row_check][row] == 1:
                        # Check if point is OUT
                        # Has only incoming edges from SCC
                        if label_points(row_check) in list_scc:
                            if label_points(row) not in list_out:
                                list_out.append(label_points(row))

    for row in range(0, len(graph)):
        if label_points(row) not in list_scc and label_points(row) not in list_out and label_points(row) not in list_in:
            if outward_edges[row]:
                for column in range(len(graph[0])):
                    if graph[row][column] == 1:
                        # Check if point is Tendril
                        # Has only outgoing edges to OUT
                        if label_points(column) in list_out:
                            if label_points(row) not in list_tendrils:
                                list_tendrils.append(label_points(row))
                        else:
                            if label_points(row) not in list_disconnected:
                                list_disconnected.append(label_points(row))
            else:
                for column in range(len(graph[0])):
                    if graph[column][row] == 1:
                        # Check if point is Tendril
                        # Has only incoming edges to IN
                        if label_points(column) in list_in:
                            if label_points(row) not in list_tendrils:
                                list_tendrils.append(label_points(row))
                        else:
                            if label_points(row) not in list_disconnected:
                                list_disconnected.append(label_points(row))
    for points in list_scc:
        index_value = get_index(points)
        tube_point = True
        for column in range(0, len(graph[0])):
            if graph[index_value][column] == 1 and label_points(column) in list_scc:
                tube_point = False
            if tube_point:
                for row in range(0, len(graph)):
                    if graph[row][index_value] == 1 and label_points(row) in list_scc:
                        tube_point = False
            if tube_point:
                if label_points(index_value) not in list_tubes:
                    list_tubes.append(points)
    list_scc = list(set(list_scc) - set(list_tubes))
    print("SCC: " + str(list_scc))
    print("IN: " + str(list_in))
    print("OUT: " + str(list_out))
    print("Tendrils: " + str(list_tendrils))
    print("Tubes: " + str(list_tubes))
    print("Disconnected: " + str(list_disconnected))


def label_points(val):
    list_label = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    return list_label[val]


def get_index(point):
    list_label = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    return list_label.index(point)
if __name__ == "__main__":
    file_graph = open("GraphInput.txt", "r")
    graph = []
    line_count = 0
    for line in file_graph:
        graph.append([])
        line_split = line.rstrip().split(" ")
        for entry in line_split:
            graph[line_count].append(int(entry))
        line_count += 1
    file_graph.close()
    bow_tie_structure()
