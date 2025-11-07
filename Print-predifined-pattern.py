#print the following patter:
# 1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5

for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()  # Move to the next line after each row


