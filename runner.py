n = int(input("Enter number of elements: "))
a = input("Enter the array of elements: ").split()
a = sorted(a)
#print(max(a))
m = a[0]
for i in a:
    if m<i:
        m = i # finding the largest number
#print(m)
m1 = a[0]
#print(m)
for i in a:
    if m1 < i and i < m:
        m1 = i # finding the 2nd largest number
print(m1)
