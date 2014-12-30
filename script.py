def generate_adjlist(input_file, no_of_vertices):
    """
        Given an input file, no_of_vertices (eg. for 0-5000 give no_of_vertices as 5000)
        returns {vertex: set(neighbouring vertices)}
    """

    adjlist = {}
    for i in range(0,no_of_vertices+1):
        adjlist[i] = set()
    
    #This with construct is an efficient way to open large files
    # Useful because the whole file won't be loaded into the memory, works as an iterable.
    with open(input_file, "r") as f:
        for line in f:
            a,b = line.strip().split(" ")
            a = int(a)
            b = int(b)
            adjlist[a].add(b)
            adjlist[b].add(a)

    return adjlist
        
def generate_proper_data(adjlist, output_file):
    """
        Given an adjacency list as generated by the above function, it generates proper data,
        in which both the entries (u,v) and (v,u) are present for an edge e.
    """
    
    f = open(output_file,"w")
    items = adjlist.iteritems()
    for node,neighbours in items:
        for n in neighbours:
            f.write(str(node)+" "+str(n)+"\n")

    f.close()

def correct_dataset(input_file, no_of_vertices, output_file):
    """
        Use this function to correct the dataset
        NOTE: For no_of_vertices, give n in case the vertex indices range from 0 to n
    """
    adjlist = generate_adjlist(input_file, no_of_vertices)
    generate_proper_data(adjlist, output_file)

