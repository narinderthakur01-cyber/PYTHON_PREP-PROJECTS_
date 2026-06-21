arr=[1,2,33,4,56,22,90,-1,42,21]
max=arr[0]
smax=arr[0]
for i in range (len(arr)):
    if arr[i] > max:
        smax=max
        max=arr[i]
    elif arr[i]>smax and arr[i] != max:
        smax=arr[i]

print(max,smax)
arr.sort()
print(arr)
arr.reverse()
print(arr)
arr1=[1,0,3,0,2,0]
j=0
for k in range(len(arr1)):
    if(arr1[k]!=0):
        t =arr1[k]
        arr1[k]=arr1[j]
        arr1[j]=t
        j+=1

print(arr1)

lis=[1,2,3,33,12]
lis1=[0,8,5]
lis=lis+(lis1)
lis.append(87)
lis.remove(33)
print(lis)
for i in lis:
    if i%2==0:
        print(i)
    elif i%3==0:
        print(i)
    else:
        print(i)
s={55,33,66,22,11,99}
s.add(77)
s.add(00)
print(s)
s.remove(00)
print(s)
d={
    "name":"Manish",
    "key":"12"

}
print(d)
d.update({"key":"10"})
print(d)
def reverse_num(n, rev=0):
    if n == 0:
        return rev

    return reverse_num(n // 10, rev * 10 + n % 10)

def is_palindrome(n):
    return n == reverse_num(n)

print(is_palindrome(121)) 
print(is_palindrome(123))   