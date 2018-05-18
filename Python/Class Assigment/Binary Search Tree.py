# BST.py
from BST import BST

B = BST()

#creates binary search tree
B.insert_rec(7)
B.insert_rec(5)
B.insert_rec(10)
B.insert_rec(2)
B.insert_rec(12)

#adds 6,3,11, and 14 to binary tree
B.insert_rec(6)
B.insert_rec(3)
B.insert_rec(11)
B.insert_rec(14)

#finds maximum and minimum values
print(max(B.asList()))
print(min(B.asList()))

#prints products of all numbers in tree
product = 1

for i in B.asList():

    product = product * i

print(product)

