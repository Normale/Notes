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


    def check_vertice(self, path, v, push=False):
        if len(path) == self.num - 1:
            return path
        if v in path:
            return False
        if (push == False):
            path.append(v)
        else:
            path = [v] + path

        for vertice in self.relations_list[path[-1] - 1]:
            done = self.check_vertice(path, vertice)
            if done:
                return done

        for vertice in self.relations_list[path[0] - 1]:
            done = self.check_vertice(path, vertice, push=True)
            if done:
                return done

        return False

    def find_path(self):
        if self.not_hamiltonian_quickcheck() == True: return False
        path = self.check_vertice([], 1)
        return path


def square_sums_row(num):
    graph = Graph(num)
    graph.create_relations()
    path = graph.find_path()
    return path


if __name__ == "__main__":
    graph = Graph(23)
    graph.create_relations()
    path = graph.find_path()
