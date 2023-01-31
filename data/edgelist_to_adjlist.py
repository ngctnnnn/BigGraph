edgelist_txt = "wiki-Vote.txt"
adjlist_txt = "sample_biggraph_data.txt"
"""
Read edge list 
"""
all_edges = []
f = open(edgelist_txt, "r")
for line in f.readlines():
    edge_uv = line.strip().split('\t')
    all_edges.append([str(edge_uv[0]), str(edge_uv[1])])
    
### Main
adj_dict = {}
for idx in range(len(all_edges)):
    if all_edges[idx][0] not in adj_dict:
        adj_dict[all_edges[idx][0]] = [all_edges[idx][1]]
    else:
        adj_dict[all_edges[idx][0]].append(all_edges[idx][1])

"""
Reset output file
"""
f = open(adjlist_txt, "w")
f.write('')
f.close()

# Write
f = open(adjlist_txt, "a")
for key in adj_dict:
    f.write(f"{key}, ")
    for idx in range(len(adj_dict[key])):
        if idx != len(adj_dict[key]) - 1:
            f.write(f"{adj_dict[key][idx]}, ")
        else:
            f.write(f"{adj_dict[key][idx]}")
    f.write("\n")
f.close()