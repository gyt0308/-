from igraph import * 

def addVertex(g, name_str):
    """
    Adds new vertex to the graph if it doesn't already exist.
    """
    try:
        if(name_str not in g.vs['name']):
            print('Inserted node ',name_str)
            g.add_vertex(name=name_str)
        else:
            print ('Node ',name_str,' already present')
            print(g.vs.find(name_str).index)   
    except KeyError:
        g.add_vertex(name=name_str)
    return g

def write_tuple_to_file(f, t):
    """
    Writes tuple to the given filestream object 
    """
    string=str(t[0])+' '+str(t[1])+'\n'
    f.write(string)
def retrieve_edge_name_tuple(g, t):
    """
    Returns the name of the edge given the tuple
    """
    a=(g.vs[t[0]]['name'], g.vs[t[1]]['name'])
    return a

def load_dataset(g):
    """
    Load dataset
    """
    DATA_PATH = "data/facebook/"
    fileNums=[0]#, 107, 348, 414, 686, 698, 1684, 1912, 3437, 3980]
    
    for i,eachNum in enumerate(fileNums):
        print(eachNum)
        fileName = DATA_PATH + str(eachNum) + ".edges"
        print('fileName=', fileName)
        f = open(fileName)
        line = f.readline()
         while line!='':
            c = (line.split())
            g = addVertex(g,c[0])
            g = addVertex(g,c[1])
            print('Adding ',c[0],'-->',c[1])
            g.add_edge(c[0],c[1]) 
            line = f.readline()
    
    g.simplify()    
    return

def calculate_eigen(g):
    eigen = g.evcent(directed = False)
    for i in range(1, 6):
        maxVal = max(eigen)
        #print(i,'==node',g.vs[eigen.index(maxVal)]['name'],' with score of ',maxVal)
         eigen.remove(maxVal)
    eigen = g.evcent(directed = False)
    
    return eigen


def calculate_closeness(g):
    close = g.closeness(g.vs)
    for i in range(1, 6):
        maxVal = max(close)
        #print(i,'==node',g.vs[close.index(maxVal)]['name'],' with score of ',maxVal)
        close.remove(maxVal)
    close=g.
