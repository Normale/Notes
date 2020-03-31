#DAFTCODE 2020 SPRING PYTHON LEVEL-UP QUALIFICATION TASK
#todo: optimalizations, 
#IDEAS:
#1. dijkstra algorithm
#2. do it linearly without creating classes
class Node:
    def __init__(self, number, left=0, right=0):
        self.number = number
        self.right = left
        self.left = right
        self.value = 0
        self.best_path = []
    def get_value(self):
        if self.value == 0:
            try:
                if (self.right.get_value() < self.left.get_value()):
                    self.value = self.number + self.right.get_value()
                    self.best_path = self.right.best_path + [self.number]
                else:
                    self.value = self.number + self.left.get_value()
                    self.best_path = self.left.best_path + [self.number]

            except:
                self.value = self.number
                self.best_path = [self.number]
        else: pass
        return self.value

    def __str__(self):
        return str(self.number)



if __name__ == "__main__":
    numbers = []

    with open("Files/easy.txt", "r") as file:
        for line in file:
            numbers.append(list(map(int, line.strip().split(" "))))

    nodes = []
    tmp_list = []
    for number in numbers[len(numbers) - 1]:
        tmp_list.append(Node(number))
    nodes.append(tmp_list)

    for i in range(2, len(numbers) + 1):
        tmp_list = []
        for k in range(len(numbers[-i])): #cause length of numbers[i] == i + 1
            tmp_node = Node(numbers[-i][k])
            tmp_node.left = nodes[i-2][k]
            tmp_node.right = nodes[i-2][k+1]
            tmp_list.append(tmp_node)
        nodes.append(tmp_list)
    value = nodes[-1][0].get_value()
    path = ''.join(str(e) for e in nodes[-1][0].best_path[::-1])
    print(f"value: {value}, path: {path}")