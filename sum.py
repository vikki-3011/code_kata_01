a = int(raw_input())
b = int(raw_input())
c = []
sum=0
for i in range (1,b+1):
  c.append(i)
for j in range(b):
  sum=sum+c[j]
print(sum)
