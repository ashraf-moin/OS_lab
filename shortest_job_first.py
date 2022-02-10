dictionary = {}
result = [0]
sum = 0

n = int(input('Enter the number of process: '))
for i in range(0,n):
  key = input("Enter the process name for "+str(i+1)+":") 
  value = int(input("Enter the brust time for "+str(i+1)+":")) 
  dictionary[key] = value


dictionary = sorted(dictionary.items(), key = lambda x: x[1])


for key, val in dictionary:
  last_element  = result[-1]
  sum += last_element 
  temp = last_element + val

  result.append(key)
  result.append(temp)


print('The average waiting time: ',sum/n)
print(*result)

