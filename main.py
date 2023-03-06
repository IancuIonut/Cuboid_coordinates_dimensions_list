print ("Type a number then press Enter: ")
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# nested for loops for generating the (i,j,k) coordonate list
for i in range(x+1):
  for j in range(y+1):
    for k in range (z+1):
     if i+j+k != int(n): # to exclude the sum that is = n.
      print([i,j,k], end=",")


print()
print()

# using list Comprehension is a much faster
list= [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
num_pairs = len(list)
print(num_pairs, " pairs of coordinates")
print()
print(list)