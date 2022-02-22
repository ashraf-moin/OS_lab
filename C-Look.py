disk_size = 200


def CLOOK(arr, head):

    seek_count = 0
    distance = 0
    cur_track = 0

    left = []
    right = [head]

    seek_sequence = []

    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])

    left.sort()
    right.sort()

    for i in range(len(right)):
        cur_track = right[i]

        seek_sequence.append(cur_track)

        distance = abs(cur_track - head)

        seek_count += distance

        head = cur_track

    seek_count += abs(head - left[0])
    head = left[0]

    for i in range(len(left)):
        cur_track = left[i]

        seek_sequence.append(cur_track)

        distance = abs(cur_track - head)

        seek_count += distance

        head = cur_track

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

    print("Path: ", end='')
    print(*seek_sequence)
    print("Total number of head movements:", seek_count, end='')



disk = []

size = int(input("Enter the number of movements: "))

for i in range(0, size):
    x = int(input())
    disk.append(x)

head = int(input("Head starts at "))

CLOOK(disk, head)
