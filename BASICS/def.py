def sum(a,b):
    return a+b
print(sum(2,2))
# new 
s=0
def rev(n):
   global s
   if n==0:
       return s
   ld=n%10
   s=(s*10)+ld
   return rev(n//10)
print(rev(1112))
#
def pal( s):
    
    if(s[::-1])!=(s):
        print("its not pal")
    else:
        print("its pal")
print(pal("mam"))
v="aeiouAEIOu"
f=0
def count(c):
    global f 
    for ch in c:
        if ch in v:
            f+=1
    return f
    
print(count("education"),f)
lis=[1,2,3,5,6,55,0,-1]
m=0;
for i in lis:
    if i>m:
        m=i

print(m)
print(max(lis))
lis1=[1,2,3,5,6,55,0,-1]
mn=0;
for j in lis1:
    if j<mn:
        mn=j

print(mn)
print(min(lis1))
