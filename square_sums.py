'''
Task:
Pick some integer N. Given all of the integers from 1 to N, 
can you arrange all elements such that each adjacent pair sums to a square number?

Detailed explanation:
https://www.codewars.com/kata/5a667236145c462103000091

More optimized solution: https://github.com/charlieturner/square-sum-sequences
'''

from time import time
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
        self.vertices = list(range(1,self.num))
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
    
    def delete(self, vertex, relations, vertices_o):
        vertices = vertices_o.copy()
        try:
            vertices.remove(vertex)
        except:
            return False
        if not vertices: return [vertex]
        for v in relations[vertex - 1]:
            res = self.delete(v, relations, vertices)
            if res != False:
                res.append(vertex)
                return res
        return False

    def deleting_approach(self):
        if self.not_hamiltonian_quickcheck(): return False
        for v in self.vertices:
            result = self.delete(v, self.relations_list, self.vertices)
            if result != False:
                return result
        return False
        

def square_sums(num):
    graph = Graph(num)
    graph.create_relations()
    path = graph.brute_force()
    return path


if __name__ == "__main__":
    time1 = time()
    for i in range(289, 290):
        # graph = Graph(i)
        # graph.create_relations()
        # path = graph.deleting_approach()
        # print(f"{i}: {path}")
        print(f"{i} => {square_sums(i)}")

    time2 = time()
    print(time2-time1)