#list comprehension
#new_list=[Expression  ,for items list ,if conditions]
'''a=[x for x in range(1000) if x%2==0]
print(a)
b=[3**i for i in range(20)]
print(b)'''
#list methods
#1)append
a=[1,2,3]
a.append(4)
print(a)

#2)insert
a.insert(1,0.5)
print(a)

# 3)sort
c=[2,3,6,5,4,5,]
c.sort()
print(c)
# 4)pop
# 5)clear-->clear the list
# 6)reverse-->reverse the list given

# 7)count----> count is used to find the frequence of number

# 8)index

# at the time of calling the method ,we used the .(dott)
#to access the Method 
# in using the function we does not Requied to used the dot symbol
'''
functions used in the list
1)len(list)-->length of element
2)max(list)-->maxium number in the list
3)min(list)--.min number in the list
4)list(seq)-->converted list in to the sequences
5)sum(list)-->sum of list

'''
print(len(c))