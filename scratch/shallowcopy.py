
import copy
#makes list
li = [[1,2]]

#x has a shallow copy of contents of li[0], which references pointing back to li
x = [li[0][:]]
print(x)
#changed part of x, but it won't chage part of li. Even though it is a shallow copy, the copies primative data types and immutable
x[0][0]=2
print(x, li)


li2 = [[1,2], [3,4]]
# x2 = copy.copy(li2[0])
#shallow copy copies the lists into another list. Bc of this, when we modify li2[0][1], the reference to the list points back to 
# li2, so x2 and li2 changes. This is different from above when we made the shallow copy with primative data types, you can see it doesn't happen
x2 = li2[:]
print(x2, li2)
li2[0][1] = 6
print(x2, li2)