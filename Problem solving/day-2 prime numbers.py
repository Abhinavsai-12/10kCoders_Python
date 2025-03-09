

# # for loop(practice)

# # 1. practice
# for i in "banana":
#     print(i)

# # 2. practice
# for i in range(1,25,2):
#     print(i)


# # 3. practice
# x= int(input())
# for i in range(1,x,1):
#     print(i)



# prime numbers,not prime, maximum and minimum


# # 1. Sum of prime numbers in a given number

# n="123456789"
# sum=0
# nsum=0

# for i in n:
#     x=int(i)
    
#     # prime number
#     c=0
#     for i in range(2,x-1,1):
#         if x%i==0:
#             c+=1
#     if c==0:
#         sum+=x
#     if c!=0:
#         nsum+=x

# print(sum, "is sum of prime numbers")
# print(nsum, "is sum of non prime numbers")



# # 2 largest prime in given number

# n="46537129"
# y=0

# for i in n:
#     x=int(i)

#     # prime
#     c=0
#     for j in range(2,x-1,1):
#         if x%j==0:
#             c+=1
    
#     if c==0:
#         if x>y:
#             y=x
         
# print(y)



# # 3. two largest prime numbers

# n="46537129"
# y=0
# z=0

# for i in n:
#     x=int(i)

#     # prime
#     c=0
#     for j in range(2,x-1,1):
#         if x%j==0:
#             c+=1
    
#     if c==0:
#         if x>y:
#             z=y
#             y=x
         
# print(y)
# print(z) 


# # 4. minimum prime number in given number

# n="4653729"
# max=0

# for i in n:
#     x=int(i)

#     # prime
#     c=0
#     for j in range(2,x-1,1):
#         if x%j==0:
#             c+=1
    
#     if c==0:
#         if x>max:
#             max=x

#         # min
#         min=max
#         if min>x:
#             min=x
         
# print(max)
# print(min)


# # 5. sum of largest and smallest prime number in given digits


# n="4653729"
# max=0
# sum=0

# for i in n:
#     x=int(i)

#     # prime
#     c=0
#     for j in range(2,x-1,1):
#         if x%j==0:
#             c+=1
    
#     if c==0:
#         if x>max:
#             max=x

#         # min
#         min=max
#         if min>x:
#             min=x
         
# print(max)
# print(min)

# sum=max+min
# print(sum, "is sum of largest and smallest prime num")



# # 6.  largest non prime in given number

# n="46537129"
# y=0

# for i in n:
#     x=int(i)

#     # prime
#     c=0
#     for j in range(2,x-1,1):
#         if x%j==0:
#             c+=1
    
#     if c!=0:
#         if x>y:
#             y=x
         
# print(y)



