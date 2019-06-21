import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
name_list = {}
duplicates = []

def make_name_list(name):
  global name_list
  if name == "Alex Matthews":
    print(name)
  if name in name_list:
    name_list[name] += 1
  else:
    name_list[name] = 1

namesBST1 = BinarySearchTree("Name 1")
for name_1 in names_1:
    namesBST1.insert(name_1)

# for name_2 in names_2:
#     if namesBST1.contains(name_2):
#         duplicates.append(name_2)

namesBST2 = BinarySearchTree("Name 2")

for name_2 in names_2:
  namesBST2.insert(name_2)

namesBST1.for_each(make_name_list)
namesBST2.for_each(make_name_list)

for name in name_list:
  if name_list[name] > 1:
    duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
