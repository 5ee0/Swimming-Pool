#Idea
### Situation 1: The time slot of some lifeguards was totally covered by others, then we can fire this one.
### Situation 2: Situation 1 doesn't exist. Then we should consider which lifeguard owns shortest time slot.


import time


##parameter##

class Node:
    def __init__(self, left, right, length):
        self.left = left  #start time
        self.right = right  #end time
        self.length = length  #time length

    def __lt__(self, other):  # Compare: Based on start time, the smaller one is in front, if start time is the same, then based on the end time
        if self.left == other.left:
            return self.right < other.right
        else:
            return self.left < other.left


fileNum = int(10)
filePath = 'dist/in/'
outputPath = 'dist/out/'
# Maxtime
maxTime = int(1e5 + 10)

# worktime
workTime = []


##parameter over##

def algo(workTime):
    # Sort
    workTime.sort()
    # The end time of the  i-1 lifeguard
    pointer = 0
    # Final covered time
    retVal = 0
    # Mark whether Situation exists : False - No True - Yes
    flag = False
    # Go through
    for i in range(len(workTime)):
        # Situation 1: The time slot of some lifeguards was totally covered by others.
        if workTime[i].right <= pointer:
            flag = True
        else:
            # Situation 2
            # Compare the work time of i lifeguard and i-1 lifeguard
            _wortTime = min(workTime[i].right - workTime[i].left, workTime[i].right - pointer)
            # Totalization
            retVal += _wortTime
            # Calculate the work time of i lifeguard
            workTime[i].length = _wortTime
            if i > 0 and workTime[i].left < pointer:
                # Calculate the work time of i-1 lifeguard
                workTime[i - 1].length -= pointer - workTime[i].left
            # Update Mark
            pointer = workTime[i].right

    if flag is True:
        # Case1
        print(retVal)
        return retVal
    else:
        # Case2
        minTime = (1 << 29)
        # Find shortest work time
        for n in workTime:
            minTime = min(minTime, n.length)
        print(retVal - minTime)
        return retVal - minTime


if __name__ == '__main__':
    # Read file
    for i in range(1, 1 + fileNum):
        # record start time
        startTime = time.process_time()
        with open(filePath + str(i) + '.in', encoding='utf-8') as fileObj:
            file = fileObj.read()
        # Split each row
        contents = file.split()
        # Read amounts of lifeguards
        num = int(contents[0])
        # Read work time
        workTime.clear()
        for j in range(num):
            workTime.append(
                Node(
                    int(contents[2 * j + 1]),
                    int(contents[2 * j + 2]),
                    int(contents[2 * j + 2]) - int(contents[2 * j + 1])
                )
            )
        fileObj.close()
        
        retVal = algo(workTime)


        # Output result
        with open(outputPath + str(i) + '.out', mode='a', encoding='utf-8') as outputFile:
            outputFile.write(str(retVal) + '\n')
        outputFile.close()
