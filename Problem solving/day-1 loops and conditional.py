# # intro loops and conditional statements


# # 1. elif program
# n=int(input("Enter A number"))
# # n=10
# if n>10:
#     print(n," is greater than 10")
# elif n<10:
#     print(n," is less than 10")
# else:
#     print("Not A Number")


# # # 2. even or odd
# n=15
# if n%2==0:
#     print(n, "is even")
# else:
#     print(n,"is even")



# # 3. prime numbers
# n=11
# c=0
# for x in range(2,n-1,1):
#     if n%x==0:
#         c+=1

# if c==0:
#     print(n,"is a prime")
# else:
#     print("not a prime")



# # 4. sum of individual numbers

# n="1234"
# sum=0
# for i in n:
#     sum+=int(i)
# print(sum)




# # 5. sum of odd individual numbers present in given number
# n="237"
# sum=0
# for i in n:
#     if int(i)%2 !=0:
#         sum+=int(i)

# print(sum)


# # 6. difference b/w even and odd
# n="2376"
# esum=0
# osum=0
# for i in n:
#     if int(i)%2 ==0:
#         esum+=int(i)
#     else:
#         osum+=int(i)

# if esum >osum:
#     print(esum-osum)
# else:
#     print(osum-esum)





# # 7. which is largest sum even or odd 
# n="2376"
# esum=0
# osum=0
# for i in n:
#     if int(i)%2 ==0:
#         esum+=int(i)
#     else:
#         osum+=int(i)

# if esum >osum:
#     print(esum,"even sum is greater")
# else:
#     print(osum,"odd sum is greater")