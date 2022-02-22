disk_size = 200


def SCAN(arr, head, direction):

    seek_count = 0
    distance, cur_track = 0, 0
    left = [head]
    right = []
    seek_sequence = []

    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(disk_size - 1)

    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])

    left.sort()
    right.sort()

    run = 2
    while (run != 0):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]

                seek_sequence.append(cur_track)

                distance = abs(cur_track - head)

                seek_count += distance

                head = cur_track

            direction = "right"

        elif (direction == "right"):
            for i in range(len(right)):
                cur_track = right[i]

                seek_sequence.append(cur_track)

                distance = abs(cur_track - head)

                seek_count += distance
                head = cur_track

            direction = "left"

        run -= 1

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

    print("All Path: ", end='')
    print(*seek_sequence)
    print("Total number of head movements:", seek_count, end='')
    


disk = []

size = int(input("Enter the number of movements: "))

for i in range(0, size):
    x = int(input())
    disk.append(x)

head = int(input("Starts at "))
direction = "left"

SCAN(disk, head, direction)
