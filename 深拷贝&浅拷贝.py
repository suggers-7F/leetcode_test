import copy

# x = [1,2]
# y = x
# a = x.copy()
# b = copy.copy(x)
# c = x[:]
# d = copy.deepcopy(x)
#
#
# print(a)
# print(b)
# print(c)
# print(d)
# print("=========")
#
# x[0] = 111
# print(x)
# print(y)
# print(a)
# print(b)
# print(c)
# print(d)
#
#
#


print("==============")



x = [1,2]
y = [3,4]
z = [x,y]
print(id(x))
print(id(y))
print(id(z))
print(id(z[0]))
print(id(z[1]))

f = z
a = z.copy()
b = copy.copy(z)
c = z[:]
d = copy.deepcopy(z)


print(a)
print(b)
print(c)
print(d)
print("=========")

z[0] = [11,22]




print(z)
print(f)
print(a)
print(b)
print(c)
print(d)