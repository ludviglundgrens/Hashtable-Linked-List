from linkedlist import LL

class HT_LL():
    def __init__(self, length):
        self.length = length
        self.array = [None]*length

    def add(self, key, value):
        val = hash(key) % self.length

        if self.array[val] == None:
            self.array[val] = LL()
            self.array[val].add(key, value)

        else:
            self.array[val].add(key, value)
    
    def search(self, key):
        index = hash(key) % self.length
        if self.array[index] == None:
            print("Key not in hashtable")
            return
        else:
            node_i = self.array[index].headnode
            while node_i.key != key:
                if node_i.nextnode == None:
                    print("Key not in hashtable")
                    return
                else: 
                    node_i = node_i.nextnode
            print("Found key and value pair:", node_i.key, node_i.value)

    def printallLL(self):
        for index, item in enumerate(self.array):
            if item != None:
                print("Arraynumber", index)
                item.printlist()
                print("\n")

if __name__ == "__main__":
    a = HT_LL(10)
    a.add("name", "Ludvig")
    a.add("age", "tjugofyra")
    a.add("city", "stockholm")
    a.add("country", "sweden")
    a.add("country", "sweden")
    a.add("country", "sweden")
    a.printallLL()
    a.search("test")
    a.search("name")
    a.search("country")
