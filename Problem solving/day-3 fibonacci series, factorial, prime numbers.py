

# # 1. fibonacci series

# n=int(input("Enter range"))
# i=1
# a=0
# b=1
# while i<=n:

#     c=a+b
#     print(a)

#     a=b
#     b=c
#     i+=1






# # 2. sum of given numbers

# n="123454"
# sum=0
# for i in n:
#     sum+=int(i)

# print(sum)



# # 3. Factorial of given number

# n=int(input("Enter no:"))
# fact=1
# for i in range(1,n+1,1): # 5! 1*2*3*4*5=120
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
#     st+="*"+str(i) #1*2*3*4*5
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





#  9. Next Prime number
# ex: n=11  nxt= 13,17,19

# a=13
# num=a
# nxt=0
# nxt_prime=False

# while(not nxt_prime):
#     num+=1
#     count=0
#     for i in range(2,num,1):
#         if num%i==0:
#             count+=1
#             break
    
#     if count==0:
#         nxt=num
#         nxt_prime=True

# print(nxt)



# 10. previous prime number
# ex: n=17  prev= 7,11,13

# a=13
# num=a
# prev=0
# prev_prime=False

# while(not prev_prime):
#     num-=1
#     count=0
#     for i in range(2,num,1):
#         if num%i==0:
#             count+=1
#             break
    
#     if count==0:
#         prev=num
#         prev_prime=True

# print(prev)




# 11. Nearest prime number
# ex: n=5  prev=3  nxt=7 (same difference print null)


# a=int(input("Enter Number for neaarest prime"))
# num=a

# # Next prime
# nxt=0
# ndiff=0
# nxt_prime=False

# while(not nxt_prime):
#     num+=1
#     ndiff+=1
#     count=0
#     for i in range(2,num,1):
#         if num%i==0:
#             count+=1
#             break
    
#     if count==0:
#         nxt=num
#         nxt_prime=True
# print("next prime is: ",nxt)


# # Prev prime
# num=a
# prev=0
# pdiff=0
# prev_prime=False

# while(not prev_prime):
#     num-=1
#     pdiff+=1
#     count=0
#     for i in range(2,num,1):
#         if num%i==0:
#             count+=1
#             break
    
#     if count==0:
#         prev=num
#         prev_prime=True
# print("previous prime is: ",prev)


# # comapre

# if ndiff<pdiff:
#     print("nearest prime is: ",nxt)
# elif pdiff<ndiff:
#     print("nearest prime is: ",prev)
# elif pdiff==ndiff:
#     print("nearest prime difference is Null ")
# else:
#     print("Invalid number ")



# # 12. print next 10 prime numbers of given number
# a=2
# num=a
# count=0

# while count < 10:
#     num+=1
#     fact=0
#     for i in range(2,num,1):
#         if num%i==0:
#             fact+=1
#             break
    
#     if fact==0:
#         count+=1
#         print(num)











