time = 0
sum = 0
result = [0]
n = int(input('Enter the number of process: '))

for i in range(0,n):
  process = input("Enter the process name for "+str(i+1)+":")
  result.append(process)

  time = int(input("Enter the brust time for "+str(i+1)+":"))
  last_element = result[-2] 
  sum += last_element 
  temp = last_element + time 
  result.append(temp)

print()
print('The average waiting time: ',sum/n)
print(*result)