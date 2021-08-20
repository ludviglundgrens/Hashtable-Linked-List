class HT:
    def __init__(self, length):
        self.length = length
        self.array = [None]*length

    def add(self, key, value):
        index = hash(key) % self.length
        start_index = index

        while self.array[index] != None:
            if index == self.length-1:
                index = 0
            else:
                index += 1

            if index == start_index:
                print("No space in hashtable")
                return

        self.array[index] = [key, value]

    def search(self, key):
        index = hash(key)%self.length
        start_index = index

        while self.array[index][0] != key:
            if index == self.length-1:
                index = 0
            else:
                index += 1

            if index == start_index:
                print("Cant find key")
                return
        print("Found key and value pair:", self.array[index][0], self.array[index][1])

    def p(self):
        print(self.array)


if __name__ == "__main__":
    a = HT(5)
    a.add(key = "a", value = "1")
    a.add(key = "b", value = "2")
    a.add(key = "c", value = "3")
    a.add(key = "d", value = "4")
    a.add(key = "e", value = "5")
    a.add(key = "f", value = "6")
    a.p()
    a.search("d")
    a.search("q")