inp =  input("Enter a String:")
def split(word): # FUNCTION to make list from a String
    return list(word)

def join(list): #funtion to make a string from a LIST
    str = ""
    return (str.join(list))

def pall_check(string):
    if string == string [::-1]: #string[::-1]== Reverse a String
        print("It is Pallindrome")
    else:
        print("NOT pallindrome")
inp = split(inp)
print(inp)

n = len(inp)
for c in range(0,n-1,1):
    inp[c],inp[-c+n-1]= inp[-c+n-1],inp[c]

inp = join(inp)
pall_check(inp)
