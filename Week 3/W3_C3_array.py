import array as ar

a = ar.array('d',[1.2,2.1,3.3,4.2])

print ("\nInitial array: ",a)
print("\nLength of array: ",len(a))

a.append(5.5)
print("\nAfter a.append(5.5): ",a)

a.extend([6.4,7.5,8.9,9.0])
print("\nAfter a.extend([6.4,7.5,8.9,9.0]): ",a)

a.insert(4,7.5)
print("\nAfter a.insert([1,7.5]): ",a)

b=ar.array('d',[10.2,11.4,12.00])
c=ar.array('d')
c=a+b
print("\nAfter a+b: ",c)

print("\na.pop(): ",a.pop())
print("a.pop(4): ",a.pop(4))

print("\nAfter pop(): ",a)

a.remove(5.5)
print("\nAfter a.remove(5.5): ",a)

print("\nAfter slicing a[1:4]: ",a[1:4])

