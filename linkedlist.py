class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextnode = None

class LL:
    def __init__(self):
        self.headnode = None

    def add(self, key, value):
        if self.headnode == None:
            self.headnode = Node(key, value)

        elif self.headnode.nextnode == None:
            self.headnode.nextnode = Node(key, value)

        else:
            node_i = self.headnode.nextnode
            while node_i.nextnode != None:
                node_i = node_i.nextnode
            node_i.nextnode = Node(key, value)

    def printlist(self):
        print(self.headnode.key, self.headnode.value)
        node_i = self.headnode.nextnode
        while node_i != None:
            print(node_i.key, node_i.value)
            node_i = node_i.nextnode 

if __name__ == "__main__":
    a = LL()
    a.add(key = "name", value = "Ludvig")
    a.add(key = "name", value = "Ludvig")
    a.printlist()