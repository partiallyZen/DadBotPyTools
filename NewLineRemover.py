
string1 = ()

f = open('list.txt', 'r')
string1=str(f.read())

print("Your list.txt before |")
print(string1)
string2 = string1.replace('\n','"],["')

print("Your list.txt after |")
print(string2)