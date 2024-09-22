x = 0.0
k = 0.0
a = 0.0
sum = 0.0
while x <= 1:
    for i in range(10):
        d = (((-1) ** k) * x ** (2 * k + 3)) / ((2* k + 1) * (2 * k + 3)) 
        a = a + d
        k = k + 1
    
    
    
    
    
    
    
    x = x + 0.1
    sum = sum + a
    print (a)
    print("====================") 
    print(sum)
    print("********************")

