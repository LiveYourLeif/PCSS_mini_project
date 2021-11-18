

class General_algorithm():
    file = open("saveData.txt", "r")
    value = file.read().splitlines()
    file.close()

    counter = 0

    def count(self):
        self.counter += 1


class Bubble_Sort(General_algorithm):

    def sort(self, inp):
        self.value = inp
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
