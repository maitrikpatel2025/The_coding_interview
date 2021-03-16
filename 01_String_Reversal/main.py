def revse_string(string):
    new_string=''
    for i in range(len(string)-1,-1,-1):
        new_string += string[i]
    return new_string

revse_string("dixant")

string1="maitrik"
string2=string1[6:0:-2]
print(string2)