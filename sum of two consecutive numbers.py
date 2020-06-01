def nums(num):
    prev = 0
    for i in range(num):
        sum=prev+i
        print(sum)
        prev = i
        
num = int(input("Enter number: "))
nums(num)
