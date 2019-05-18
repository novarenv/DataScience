arr = [1, 2, 3, 4, 5]
print(arr)
arr.append(5)
print(arr)
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(len(arr))
arr = arr*2
print(arr)

arrBaru = [7, 6, 5, 4, 3, 2, 1]
for i in arrBaru:
    print(i)
for i in range(len(arrBaru)):
    print(i)
arrKos = []
for i in range(10):
    arrKos.append(i**2)

print(arrKos)