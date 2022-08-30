import os

FibArray = [0, 1]
def fibonacci(n):
    if n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]

def average(witchkilled):
    alphabet = 0
    ArrayAvg = []
    for key in witchkilled:
        bornOnYear = int(key['year']) - int(key['age'])
        i = 0
        avg = 0
        while i < bornOnYear:
            x = fibonacci(i + 1)
            avg = avg + x
            i += 1
        ArrayAvg.append(avg)
        print("person " + chr(97 + alphabet).upper() + " born on Year =" + key['year'] + "-" + key['age'] + "=" + str(
            bornOnYear) + "number of people killed on year " + str(bornOnYear) + " is " + str(avg))
        alphabet += 1

    iterateAvg = ""
    sum = 0
    for item in ArrayAvg:
        sum += item
        iterateAvg += str(item) + "+"

    print("So the average is (" + iterateAvg[:-1] + ")/" + str(len(ArrayAvg)) + "=" + str(sum / len(ArrayAvg)))


nlist = []
i = 0
print("note:type 'no' to finish")
while True:
    inputAge = input("Input Age of death person " + str(i + 1) + ":")
    if inputAge == "no":
        print(average(nlist))
        break
    inputYear = input("Input Year of death person " + str(i + 1) + ":")
    if inputYear == "no":
        print(average(nlist))
        break
    nlist.append({'age': inputAge, 'year': inputYear})
    i += 1