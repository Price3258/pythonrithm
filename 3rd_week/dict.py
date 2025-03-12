
class Dict:
    def __init__(self):
        self.items = [None]*8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index= hash(key)% len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test",3)
print(my_dict.get("test"))


class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k,v in self.items:
            if k ==key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key,value)

    def get(self, key):
        index= hash(key)% len(self.items)
        return self.items[index].get(key)


linked_dict = Dict()
linked_dict.put("test",3)
print(linked_dict.get("test"))
linked_dict.put("333",6)
linked_dict.put("77",7)
print(linked_dict.get("333"))
print(linked_dict.get("77"))
