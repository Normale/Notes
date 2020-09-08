def tst(n):
    lista = []
    for i in range(1, n):
        if (i**2 <= 2*n): 
            lista.append(i**2)
        else: 
            return lista
    return lista

class Graph:
    def __init__(self, n):
        self.num = n + 1
        self.possible_sums = tst(self.num)
        self.relations_list = []
        self.vertices = [n for n in range(1,self.num)]
    def create_relations(self):
        for v in self.vertices:
            relation = []
            for i in range(1,self.num):
                if (i != v) and (i+v) in self.possible_sums:
                    relation.append(i)
            self.relations_list.append(relation)
    
    def not_hamiltonian_quickcheck(self):
        '''Quick check if graph contains more than two single vertice, 
        if YES, there is no point in further checking, it will not have hamiltonian path including all the vertices
        Returns TRUE if graph IS NOT hamiltonian (doesnt contain spanning hamiltonian path)'''
        if not all(self.relations_list): return True #if there is a vertice with no relations
        count_1 = sum(len(sublst)==1 for sublst in self.relations_list) 
        if count_1 > 2: return True

    def bf_add(self, v, path):
        if len(path) == self.num - 1: return path
        if v in path: return False
        
        path = path + [v]
        for vertice in self.relations_list[v - 1]:
            done = self.bf_add(vertice, path)
            if done: return done

        
    def brute_force(self):
        path = []
        for v in self.vertices:
            x = self.bf_add(v, path)
            if x:
                return x
        return False


def square_sums(num):
    graph = Graph(num)
    graph.create_relations()
    path = graph.find_path()
    return path


if __name__ == "__main__":
    graph = Graph(5)
    graph.create_relations()
    path = graph.brute_force()
    print(path)
