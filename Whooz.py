class NightClub:

    def __init__(self, input=None, wjEntranceQueue=None):
        self.input = input
        if wjEntranceQueue is None:
            wjEntranceQueue = []
        self.wjEntranceQueue = wjEntranceQueue
        self.liar = "Q24"


    # --START Validate Age
    # Check if age is under 18 or if = to 90 not if 90 and above just if = 90-- as per requirements in entry rule
    def validateAge(self):
     for x in range(0, length):
        age = int(self.input[x][1:])
        if age < 18:
            print(str(self.input[x]) + " is under 18 and is being kicked out of the entrance queue!\n")
        elif age == 90:
            print(str(self.input[x]) + " is 90 and cannot be helped onto the entrance queue beca!\n")
        else:
            self.wjEntranceQueue.append(self.input[x])
            print("Individuals who are allowed to enter: " + str(self.wjEntranceQueue) + "\n")
    # --END Validate Age

    # --START bubble sorting -- Descending to age
    def sorting(self):
        isSorted = False
        length = len(nc.wjEntranceQueue) - 1
        # if two ages are exactly the same example G32 and I32, G32 must be first

        # Asuming letter depicts order you arrived sort alphabetically first
        nc.wjEntranceQueue.sort()
        # then sorting by age descending [1:] -- bubble sorting
        while not isSorted:
            isSorted = True
            for x in range(0, length):
                if self.wjEntranceQueue[x][1:] < self.wjEntranceQueue[x + 1][1:]:
                    isSorted = False  # when two ages in the wrong order is found
                    temp = self.wjEntranceQueue[x + 1]
                    self.wjEntranceQueue[x + 1] = self.wjEntranceQueue[x]
                    self.wjEntranceQueue[x] = temp
        # --END bubble sorting

        print("Order to enter: " + str(nc.wjEntranceQueue)+ "\n")

    # --START find liar x age
    def find_index(self, array, find):
        for i, v in enumerate(array):
            if array[i] == find:
                return i

    def findLiarX(self):
    # check that index is not 1 or less to avoid get index out of bound when -2
        if liar_index >= 1:
            currentAge = int(self.wjEntranceQueue[liar_index][1:])
            ageTwoPosAhead = int(self.wjEntranceQueue[liar_index - 2][1:])
            x = currentAge + ageTwoPosAhead
            print("X must be equal to: " + str(x))
    # --END find liar x age


nc = NightClub(input)
nc.input = (
    ["A19", "B28", "C23", "D4", "E78", "F90", "G32", "H54", "I32", "J12", "J67", "L90", "M87", "N6", "O36", "P12",
     "Q24"])
length = len(nc.input)
print("Input" + nc.input)
nc.validateAge()
print(nc.wjEntranceQueue)
nc.sorting()
liar_index = nc.find_index(nc.wjEntranceQueue, nc.liar)
nc.findLiarX()