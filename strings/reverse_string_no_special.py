
def reverseSting(text):
    text = list(text)
    left = -1
 
    # Loop from last index until half of the index
    for i in range(len(text) - 1, len(text) // 2, -1):
        # I did this myself, you need to make sure left is always less than i or you can undo your swaps
        # if not i > left:
        if left >= i:
            break
        # match character is alphabet or not        
        if text[i].isalpha():
            temp = text[i]
            while True:
                left += 1
                if text[left].isalpha():
                    text[i] = text[left]
                    text[left] = temp
                    break
    return "".join(text)
     
# Driver code
# string = "a!!!b.c.d,e'f,ghi"
string = ".........ab"
print ("Input string: ", string)
string = reverseSting(string)
print ("Output string: ", "".join(string))