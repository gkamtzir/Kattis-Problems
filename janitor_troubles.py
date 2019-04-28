import math

a, b, c, d = map(int, input().split())

hemiperipheral = (a + b + c + d)/2

result = math.sqrt((hemiperipheral-a)*(hemiperipheral-b)*(hemiperipheral-c)*(hemiperipheral-d))

print("%.16f" % result)
