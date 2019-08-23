import time

start_time = time.time()


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value >= self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
        else:
            print("you need a root")

    def contains(self, target):
        if self.value == target:
            return self.value
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left:
                return self.left.contains(target)

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

# names = names_1 + names_2
# x = {}
# for name in names:
#     if not name in x:
#         x[name] = 1
#     else:
#         x[name] += 1
# for key in x:
#     if x[key] > 1:
#         duplicates.append(key)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
