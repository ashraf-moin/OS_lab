def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)


def findMin(diff):

    index = -1
    minimum = 999999999

    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index


def shortestSeekTimeFirst(request, head):
    if (len(request) == 0):
        return

    l = len(request)
    diff = [0] * l

    for i in range(l):
        diff[i] = [0, 0]

    seek_count = 0

    seek_sequence = [0] * (l + 1)

    for i in range(l):
        seek_sequence[i] = head
        calculateDifference(request, head, diff)
        index = findMin(diff)

        diff[index][1] = True

        seek_count += diff[index][0]

        head = request[index]

    seek_sequence[len(seek_sequence) - 1] = head
    td = ''

    for i in range(len(seek_sequence)-1):

        td += '('
        if (seek_sequence[i] > seek_sequence[i+1]):
            td += str(seek_sequence[i])
            td += '-'
            td += str(seek_sequence[i+1])
        else:
            td += str(seek_sequence[i+1])
            td += '-'
            td += str(seek_sequence[i])
        td += ')+'

    td = f"{td[0: -1]}"
    print('Total distance: ' + td)
    print("All path: ", end='')
    print(*seek_sequence)
    print("Total number of head movements:", seek_count, end='')
   


if __name__ == "__main__":

    disk = []

    size = int(input("Enter the number of movements: "))

    for i in range(0, size):
        x = int(input())
        disk.append(x)

    head = int(input("Starts at "))

    shortestSeekTimeFirst(disk, head)
