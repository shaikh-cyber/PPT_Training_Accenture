#Given Inputs : ABC DEFGH -> Output : ADBECFGH
s=input()
s1=input()
i=0
res=''
while i<len(s) or i<len(s1):
  if i<len(s):
    res+=s[i]
  if i<len(s1):
    res+=s1[i]
  i=i+1
print(res)


Output 'as expected'
