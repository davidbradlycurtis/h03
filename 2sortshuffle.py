unsorted = open("01.txt", "r")
sorted = open("02.txt", "w")

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    sorted.write(line)

unsorted.close()
sorted.close()
print("Done")
