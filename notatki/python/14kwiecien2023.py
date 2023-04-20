import random ; import time

const = 80
rand_left=39

while True:
    rand_left-=random.randint(-1,1)
    if rand_left>0 and rand_left<80:
        print(" "*(const-rand_left),"I"," "*rand_left) 
        time.sleep(0.05)
    elif rand_left>78:
        rand_left-=1
    else:
        rand_left+=1
