#Input -> 321 - 3,2,1:32,31:321

s=input(); sum=0
for i in range(len(s)):
  for j in range(i,len(s)):
    sum+=int(s[i:j+1])
print(sum)

#Input 321 
#Output 381
