def move(x, speed, target_x):
    for i in range(speed):
        if x < target_x:
            x = x + 1
        elif x > target_x:
            x = x - 1
        if x == target_x:
           return target_x

    return x 

##########

normal_x = 0  
normal_speed = 3

fast_x = 40
fast_speed = 6

target_x = 20
for _ in range(16):
    normal_x = move(normal_x, normal_speed, target_x)
    fast_x = move(fast_x, fast_speed, target_x)
    print("normal: "+str(normal_x))
    print("fast: "+str(fast_x))
    print()

