
print("Enter the number of frames: ", end="")
capacity = int(input())

f, fault, pf = [], 0, 'No'

print("Enter the reference string: ", end="")
s = list(map(int, input().strip().split()))

print("\nString | Frame", end='')

print("\n   ↓\n")

occurance = [None for i in range(capacity)]

for i in range(len(s)):
    if s[i] not in f:
        if len(f) < capacity:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i+1:]:
                    f[x] = s[i]
                    break
                else:
                    occurance[x] = s[i+1:].index(f[x])
            else:
                f[occurance.index(max(occurance))] = s[i]
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'

    print("   %d\t" % s[i], end='')

    if (pf == 'No'):
        print('- - -', end=' ')

    else:
        for x in f:
            print(x, end=' ')

    for x in range(capacity-len(f)):
        print('-', end=' ')

    print()

print("\nTotal requests: %d\nTotal Page Faults: %d" % (len(s), fault))
