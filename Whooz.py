wjPatrons=["A19","B28","C23","D4","E78","F90","G32","H54","I32","J12","J67","L90","M87","N6","O36","P12","Q24"]
print ("Input List: " + str(wjPatrons) + "\n")
length = len(wjPatrons)

#--START Validate Age
#Check if age is under 18 or if = to 90 not if 90 and above just if = 90-- as per requirements in entry rule
wjEntranceQueue = []

for x in range(0, length):
    age = int(wjPatrons[x][1:])
    if age < 18 :
        print (str(wjPatrons[x]) + " is under 18 and is being kicked out of the entrance queue!\n")
    elif age == 90:
        print (str(wjPatrons[x]) + " is 90 and cannot be helped onto the entrance queue!\n")
    else:
        wjEntranceQueue.append(wjPatrons[x])
#--END Validate Age
print ("Allowed to enter: " + str(wjEntranceQueue) + "\n")

#--START bubble sorting -- Descending to age

isSorted = False
length = len(wjEntranceQueue) -1

#if two ages are exactly the same example G32 and I32, G32 must be first

#Asuming letter depicts order you arrived sort alphabetically first
wjEntranceQueue.sort()
#then sorting by age descending [1:] -- bubble sorting
while not isSorted:
    isSorted = True
    for x in range(0, length):
        if wjEntranceQueue[x][1:] < wjEntranceQueue[x + 1][1:] :
            isSorted = False  #when two ages in the wrong order is found
            temp = wjEntranceQueue[x + 1]
            wjEntranceQueue[x + 1] = wjEntranceQueue[x]
            wjEntranceQueue[x] = temp
#--END bubble sorting
print ("Order to enter: " + str(wjEntranceQueue) + "\n")

#--