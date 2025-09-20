# LIST
# a = [ 3,5,8,9,2,34.5 , True ]
# #first way
# for i in range (len(a)):
#     print(a[i])

# #second way
# for i in a:
#     print(i)
# 

# l = [ 1,2,4,5]

# l.append(6)
# l.append(7)
# print(l)

# l = [1,3,4,5,6]
# l.insert(1,2)
# print(l)

# l = [ 1,2,3,4,5,6]
# l.remove(2)
# print(l)

# l = [1,2,3,4,5,6]
# l[0] = 10
# print(l)

# l = [-45 , 67, 12 ,-68 ,-69 ,48]
# print("positive elements are")
# for i in l :
#     if i >= 0 :
#         print(i)
# print("negative elements are")
# for i in l:
#     if i < 0 :
#         print(i)

# l = [ 12 ,234,56, 67,13 ,90 ,78 ]
# sum = 0

# for i in l:
#        sum = sum + i 
# print(sum / len(l))

# l = [ 12 , 123, 234 , 678 , 456 , 789]
# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest :
#         largest = l[i]
#         index = i
#     print(f" your largest number is {largest} at index {index}")

# l = [ 12, 13 , 16 , 19 , 17]
# largest = l[0]
# sec_largest = l[0]
# for i in l:
#     if i > largest :
#         sec_largest = largest
#         largest = i
        
#     elif i > sec_largest:
#         sec_largest = i
    
# print(sec_largest , largest)        

# l = [12 , 13 , 14 , 15, 16]
# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")  
# 

# l = [ 1, 2,5,3,6,8,7,9,0]
# largest = l[0]
# smallest = l[0]
# for i in  l:
#     if i > smallest:
#         largest = i 
#     elif i < largest:
#         smallest = i 
# print( largest , smallest)   
# 
# l = [23 , 45 , 78 ,56, 55 ,20 ]     
# sum = 0 
# for i in l:
#     sum = sum + i 
# print(sum)     

# l = [ 1 , 2, 2, 3, 4, 2 ,6 ,8 ,8]
# elements = 8
# print("count:" , l.count(elements))

# l = [1 , 4, 6 , 2, 3, 9 , 2 ,5]
# rev_list= []
# for i in range(len(l)-1 , -1 , -1):
#     rev_list.append(l[i])
# print("rev_list :" , rev_list)  
# 
# l = [ 1 , 2, 3 , 2 ,1 ]  
# if l == l[::-1]:
#     print("palindrome list:")
# else:
#     print("not palindrome")

# l = [ 1, 2, 2, 3, 4, 4 ,5 ,6, 8, 8]
# unique = list(set(l))
# print("without duplicates:" , unique)

# l= [ 10 , 20 , 30 , 40 , 20 , 50]
# element = 20
# if element in l:
#     print("first occurance index:",
#     l.index(element))
# else:
#     print("element not found")

# l1 = [ 1 , 2, 3, 4, 5]
# l2 = [ 6, 7, 8, 9, 10]
# merged = l1 + l2
# print("merged list:" , merged)

# l = [ 10 , 20 , 30 , 40 , 50 , 99]
# unique = sorted(set(l))
# print("second smallest:" , unique[1])
# print("second largest :" , unique[-3])

# l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = []
# odd = []
# for i in l :
#     if i % 2 == 0 :
#         even.append(i)
#     else:
#         odd.append(i)
# print(f" even number: {even}" )
# print(f"odd number: {odd}")        

# square = []
# for i in range(1,21):
#   square.append(i ** 2)
#   print(square)

# l = [ 10 , -5 , 0 , 8 , -3 , 0 , 12 , 60]
# pos = neg = zero = 0
# for i in l:
#     if i > 0:
#         pos += 1
#     elif i < 0:
#         neg += 1
#     else:
#          zero += 1
# print("positive:" , pos  , " negative:" , neg , " zero:" , zero)    
# 
# l1 = [ 1 , 4, 5, 8, 2 , 6 ]
# l2 = [ 1 , 9, 8, 5, 4, 3 , 2]    
# common = list(set(l1) & set(l2))
# print("common elements:" , common)

# l1 = [ 1 , 4, 5, 8, 2 , 6 ]
# l2 = [ 1 , 9, 8, 5, 4, 3 ]
# difference = list(set(l1) - set(l2))
# print("difference (l1 - l2):" , difference)

# l = [ 5 , 2 , 9 , 1 , 7]
# for i in range(len(l)):
#     for j in range(0, len(l)-i-1):
#         if l[j] > l[j+1]:
#             l[j] , l[j+1] = l[j+1] , l[j]
#             print("bubble sorted list:" , l)

#question
# l = [100, 22, 43, 54, 95, 78, 1, 80, 35, 10]
# max_value = max(l)
# min_value = min(l)
# print("max:" , max(l))
# print("min:" , min(l))

# l = [100, 22, 43, 54, 95, 78, 1, 80, 35, 10]
# reversed_list = l[::-1]
# print("Reversed:" , reversed_list)

# l = [ 1 , 2, 3, 4, 5, 4, 3, 2, 1]
# unique_list = list(set(l))
# print("unique :" , unique_list )

# l1 = [ 1, 2, 3 , 4, 5]
# sum(l1)
# print("sum:" , sum (l1))
# print("average :" , sum(l1)/len(l1))

# l = [ 1, 2 , 4, 5, 6, 8, 7]
# for i in range (l) :
#     if l % 2 == 0 :
#         print("even numbers :" )

# l= [5, 6, 3, 4,9]
# l.sort()
# l.reverse()
# print(l)

