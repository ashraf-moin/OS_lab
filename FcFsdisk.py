def FCFS(arr, head, size):

    total_distance = 0
    distance, cur_track = 0, 0
    td = ''

    for i in range(size):
        cur_track = arr[i]

        td += '('
        if (cur_track > head):
            td += str(cur_track)
            td += '-'
            td += str(head)
        else:
            td += str(head)
            td += '-'
            td += str(cur_track)
        td += ')+'

        distance = abs(cur_track - head)

        total_distance += distance

        head = cur_track

    td = f"{td[0: -1]}"
    print('Total distance: ' + td)
    print("All Path: ", end='')
    print(*arr)
    print("Total number of head movements =", total_distance, end='')


if __name__ == '__main__':

    disk = []

    size = int(input("Enter the number of movements: "))

    for i in range(0, size):
        x = int(input())
        disk.append(x)

    head = int(input("Starts at "))

    FCFS(disk, head, size)
