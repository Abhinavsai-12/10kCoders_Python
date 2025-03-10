

# # 1. fibonacci series

# n=int(input("Enter range"))
# i=1
# a=0
# b=1
# while i<=n:

#     c=a+b
#     a=b
#     b=c
    
#     i+=1
#     print(a)






# # 2. sum of given numbers

# n="123454"
# sum=0
# for i in n:
#     sum+=int(i)

# print(sum)



# # 3. Factorial of given number

# n=int(input("Enter no:"))
# fact=1
# for i in range(1,n+1,1):
#     fact=fact*i

# print("Factorial of {n} is:",fact)



# 4.  Factorial of individual no's of given number's

# n=input("Enter no:")
# for j in n:

#     fact=1
#     j=int(j)
#     for i in range(1,j+1,1):
#         fact=fact*i
#     print("Factorial of {n} is:",fact)

    
# # 5. removing duplicate numbers in given number
# n="324356"
# unique=""

# for i in n:
#     if i not in unique:
#         unique+=i
# print(unique)




# 6. removing duplicate numbers in given number and Factorial of individual no's of given number

# import math
# n = "324356"
# unique = ""

# # Remove duplicate digits
# for i in n:
#     if i not in unique:
#         unique += i
# print("Unique digits:", unique)


# # Calculate factorial of each unique digit
# for j in unique:
#     num = int(j)  
#     fact = math.factorial(num) 
#     print("Factorial of ",num," is: ",fact)




# # 7. write a program to print the factorial of a number in the below format
# # i/p: 5
# # o/p: 1*2*3*4*5 = 120


# n=int(input("Enter no:"))
# fact=1
# st="1"
# for i in range(2,n+1,1):
#     fact=fact*i
#     st+="*"+str(i)
# print(st, " = ", fact)



# # 8. write a program to print sum of prime numbers in fibonaci series

# import math

# n = int(input("Enter range: "))
# i = 1
# a, b = 0, 1
# prime_sum = 0

# while i <= n:
#     c = a + b  
#     a, b = b, c
#     i += 1

#     # Prime Check
#     if a > 1:  # 1 is not prime
#         is_prime = True
#         for x in range(2, int(math.sqrt(a)) + 1):
#             if a % x == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             prime_sum += a  # Add to sum if prime

# print("Sum of prime numbers in Fibonacci series:", prime_sum)





#  9. Nearest Prime number




