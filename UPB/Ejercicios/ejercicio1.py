a = 10
b = 12
c = 13
d = 10

expresion = ((a > b) or (a < c)) and ((a == c)or(a >= b))
print (expresion)

#Solución

# a > b = False
# a < c = True
#Primera parte = True

# a == c = False
# a >= b = False
#Segunda parte = False

#Primera parte and Segunda parte = False