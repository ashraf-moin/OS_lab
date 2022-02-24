
print("Enter the number of frames: ", end="")
capacity = int(input())

f, st, fault, pf = [], [], 0, 'No'

print("Enter the reference string: ", end="")
s = list(map(int, input().strip().split()))

print("\nString | Frame", end='')

print("\n   ↓\n")

for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
            st.append(len(f)-1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Yes'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
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

print("\nTotal Requests: %d\nTotal Page Faults: %d" % (len(s), fault))
