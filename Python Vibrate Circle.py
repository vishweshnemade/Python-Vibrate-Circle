import turtle   
s = turtle.Screen()  

a = 0  
b = 0  
 
turtle.speed(0)  
turtle.goto(0,200)  #to make the circle center at the origin for this we have moved the point over y axis at 200 coordinate and then given the command of designing

i = 0
while i == 0:  
    turtle.forward(a)  
    turtle.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break  

turtle.mainloop() 