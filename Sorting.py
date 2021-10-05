import random


class General_algorithm():
    dataBubble = [3, 8, 7, 5, 1, 9, 2, 4, 6]
    dataQuick = [3, 8, 7, 5, 1, 9, 2, 4, 6]
    counter = 0

    def count(self):
        self.counter += 1


class Bubble_Sort(General_algorithm):

    def sort(self, inp):
        self.dataBubble = inp
        print(f"Array to be sorted: {inp}")
        for y in inp:
            test = True
            for x in range(len(inp)):
                if (x < len(inp) - 1):
                    if (inp[x] > inp[x + 1]):
                        test = False
                        new_value = inp[x + 1]
                        inp[x + 1] = inp[x]
                        inp[x] = new_value
            if test == True:
                break
            self.count()
            print(f"Sorting nr. {self.counter}: {inp}")

    def quicksort = ():
