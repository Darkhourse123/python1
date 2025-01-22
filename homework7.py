#task1
# 10>5 and 3==3 # True and true will be true
# 5<3 or 2>=2 # false or true will be true
# not(4!=4)# not false will be true
#(2<5)and(5>10) # true and false will be false
#(7>=7)or(3<2and8!=8) # true or(false and false) will be true or false will be true

#task2
# bool(0) # false
# bool(1) # true
# bool(-100) #true
# bool() or bool("") # False
# bool(" ") # True
# bool(None) # i think will be false

#task3
#part1
x=None
y=None
print(x is y) # true
#part2
a=1000
b=1000
print(id(a)) #130454501972784
print(id(b))#130454501972784
print(id(a)==id(b))# true
c=5
d=5
print(id(c)) #130454500934000
print(id(d)) #130454500934000
print(id(c)==id(d)) # true

#part3
x=45
if x > 0:
    print(f'{x}положительное число')
elif x==0:
    print(f'{x}положительное число')
else:
    print(f'{x}')






