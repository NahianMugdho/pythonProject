
inp =  input("Enter a String:")
def split(word): # FUNCTION to make list from a String
    return list(word)

def join(list): #funtion to make a string from a LIST
    str = ""
    return (str.join(list))

inp = split(inp)
print(inp)

n = len(inp)
for c in range(0,n-1,2):
    inp[c],inp[c+1]= inp[c+1],inp[c]


print(join(inp))
