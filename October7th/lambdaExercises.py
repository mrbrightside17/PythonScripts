#lambda is a tool used to build functions quickly
#it can use any number of parameters as portrayed below.
double=lambda x :  x*2

print 'double: ' + str(double(2))

sumOfThree=lambda x, y, z: x+y+z

print 'sumOfThree: ' + str(sumOfThree(1,2,3))

#At the same time, it is possible to use list comprehension functions
#with the lambda.
#filter()

map_a_list = [1,2,3,4,5]
map_b_list = [10,20,30,40,50]
my_list = [1,5,4,6,8,11,3,12]

filter_list = [filter(lambda x: (x%2==0), my_list)]

print 'filter function & lambda:'
print filter_list

#map()
map_list= [map(lambda x: x * 2, my_list)]

print 'map function & lambda:'
print map_list

print 'map function & lambda with two lists:'
print map(lambda x, y: x+y, map_a_list, map_b_list)

#reduce()
reduce_list = [reduce(lambda x, y: x+y, my_list)]

print 'reduce function & lambda:'
print reduce_list

#it is also a common practice to use the lambda function to sort a  tuple list.
tuple_list = [(1, 2), (4, 1), (9, 10), (13, -3)]
tuple_list.sort(key=lambda x: x[1])

print 'lambda sorting on tuple_list:'
print tuple_list