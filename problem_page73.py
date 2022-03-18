str = "Hello Test ! 123 123 ,good"


def upper_find(string):
    data=[]
    for c in string:
        if c.isupper()==True:
            b = c
            data.append(b)
    print("Upper Case letters :",data)

def lower_find(string):
        data=[]
        for c in string:
            if c.islower()==True:
                b = c
                data.append(b)
        print("Lower Case Letters:",data)

def digit_find(string):
        data = []
        for c in string:
            if c.isdigit()==True:
                b = c
                data.append(b)
        print("digit Letters:",data)

def special_find(string):
    data =[]
    for c in string:
        if c in "!, @#$%^&*.<>?/|":
            b = c
            data.append(b)
    print("Special Characters:",data)




upper_find(str)
lower_find(str)
digit_find(str)
special_find(str)
