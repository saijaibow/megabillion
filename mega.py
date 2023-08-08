import csv
numbers = [0] * 71
mega = [0] * 26
with open('Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv', newline='') as csvfile:
    next(csvfile)
    linereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in linereader:
        linenumbers = row[1].split(' ')
        intSet = set(map(int,linenumbers))
        if (max(intSet) > 70) or (int(row[2]) > 25):
            continue
        for x in linenumbers:
            numbers[int(x)] += 1
        mega[int(row[2])] += 1
    print(numbers)
    print(mega)
        
newSet = []
for x in range(5):
    index = numbers.index(max(numbers))
    newSet.append(index)
    numbers[index] = 0

print("The most frequent drawn numbers are: " + ', '.join(list(map(str,newSet))))
print("The most frequent drawn mega ball is: " + str(mega.index(max(mega))))