
print("Enter the number of frames: ", end="")
capacity = int(input())

f, fault, top, pf = [], 0, 0, 'No'
print("Enter the reference string: ", end="")
s = list(map(int, input().strip().split()))

print("\nString | Frame", end='')

print("\n   ↓\n")

for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1) % capacity
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print("   %d\t" % i, end='')

    if (pf == 'No'):
        print('- - -', end=' ')

    else:
        for x in f:
            print(x, end=' ')

    for x in range(capacity-len(f)):
        print('-', end=' ')

    print()

print("\nTotal requests: %d\nTotal Page Faults: %d" % (len(s), fault))
