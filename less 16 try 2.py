class Turtle:
    def __init__(self, x=0, y=0, step=1):
        self.x = x
        self.y = y
        self.step = step

    def up(self):
        self.y += self.step

    def down(self):
        self.y -= self.step

    def left(self):
        self.x -= self.step

    def right(self):
        self.x += self.step

    def evolve(self):
        self.step += 1

    def degrade(self):
        if self.step == 0:
            raise ValueError("Черепаха достигла цели, будь как черепаха.")
        self.step -= 1

    def count_moves(self, x2, y2):
        distance_x = abs(x2 - self.x)
        distance_y = abs(y2 - self.y)
        steps_x = distance_x // self.step if distance_x % self.step == 0 else distance_x // self.step + 1
        steps_y = distance_y // self.step if distance_y % self.step == 0 else distance_y // self.step + 1
        return max(steps_x, steps_y)

def control_turtle(turtle):
    direction = input("Направление движения (up, down, left, right): ")

    if direction == "up":
        turtle.up()
    elif direction == "down":
        turtle.down()
    elif direction == "left":
        turtle.left()
    elif direction == "right":
        turtle.right()

    print(f"Текущая позиция: ({turtle.x}, {turtle.y})")
    turtle.evolve()
    print(f"Черепаха выросла, и ее текущий размер шага теперь составляет: {turtle.step}")

    target_x = int(input("цель по x координате: "))
    target_y = int(input("цель по y координате: "))
    steps = turtle.count_moves(target_x, target_y)
    print(f"Черепаха находится в ({turtle.x}, {turtle.y}), ей осталось {steps} шагов до цели.")

    try:
        turtle.degrade()
        turtle.degrade()
    except ValueError as e:
        print(e)

user_turtle = Turtle()
control_turtle(user_turtle)
