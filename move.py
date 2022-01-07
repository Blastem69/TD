class Mob:
    def __init__(self, x, speed):
        self.x = x
        self.speed = speed

    def move(self, target_x):
        for i in range(self.speed):
            if self.x < target_x:
                self.x = self.x + 1
            elif self.x > target_x:
                self.x = self.x - 1
                if self.x == target_x:
                    break

class NormalMob(Mob):
    def __init__(self, x):
        super().__init__(x, speed=3)


class FastMob(Mob):
    def __init__(self, x):
        super().__init__(x, speed=6)

normal = NormalMob(x=0)
fast = FastMob(x=40)

target_x = 20
for _ in range(16):
    normal.move(target_x)
    fast.move(target_x)
    print("normal: "+str(normal.x))
    print("fast: "+str(fast.x))
    print()
