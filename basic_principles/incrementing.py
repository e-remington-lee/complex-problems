# When iterating over things, don't get caught up in how many times something is iterrated, know that by heart

n = 5
c=0
for x in range(5):
    # print(x)
    c+=1
print(c)
# same number of iterations as
c=0
while n>0:
    n-=1
    c+=1
print(c)


search=[
    ['A', 'F', "O", "A"],
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'X', 'S', 'S']]


print(search[2][2:2+2])

arr=[0,1,2,3,4,5]
i=0
#Will i hit every index in the array--yes
while i<len(arr):
    print(arr[i])
    i+=1

