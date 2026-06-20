print("Looping")
#for loop
i=1
for i in range(5):
    i*5
    print(i)
# while loop
j=0
while j < 5:
    j*2
    print(j)
    j+=1
# 1. Print 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print even numbers
for i in range(2, 21, 2):
    print(i)

# 3. Multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5*i}")

# 4. Sum of first 10 numbers
sum = 0
for i in range(1, 11):
    sum += i
print("Sum =", sum)

# 5. Countdown using while
n = 5
while n > 0:
    print(n)
    n -= 1

# 6. Break example
for i in range(10):
    if i == 5:
        break
    print(i)

# 7. Continue example
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 8. Nested loop
for i in range(3):
    for j in range(3):
        print(i, j)