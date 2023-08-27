class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s < 1:
            raise ValueError("Черепаха не может больше уменьшатся")
        self.s -= 1

    def count_moves(self, x2, y2):
        return max(abs(x2 - self.x), abs(y2 - self.y)) // self.s + (max(abs(x2 - self.x), abs(y2 - self.y)) % self.s != 0)  # noqa: E501

turtle = Turtle()
direction = input("Выберете курс черепахи(up, down, left, right): ")
if direction == "up":
    turtle.go_up()
elif direction == "down":
    turtle.go_down()
elif direction == "left":
    turtle.go_left()
elif direction == "right":
    turtle.go_right()
print(f"Текущая позиция черепахи: ({turtle.x}, {turtle.y})")
turtle.evolve()
print(f"Черепаха увеличилась и теперь её размер: {turtle.s}")
x = int(input("цель по x-координате: "))
y = int(input("цель по у-координате: "))
print(f"Сейчас черепаха в ячейке ({x}, {y}) ей осталось {turtle.count_moves(x, y)} Шагов до цели")  # noqa: E501
try:
    turtle.degrade()
    turtle.degrade()
except ValueError as e:
    print(e)



class CashBox:
    def __init__(self, amount=0):
        self.amount = amount

    def top_up(self, x):
        self.amount += x

    def count_1000(self):
        return self.amount // 1000

    def take_away(self, x):
        if self.amount < x:
            raise ValueError("В кассе нет столько денег:(")
        self.amount -= x

cash_box = CashBox()
amount = int(input("Внесённая в кассу сумма: "))
cash_box.top_up(amount)
print(f"Всего в кассе: {cash_box.amount} денег")
print(f"В кассе {cash_box.count_1000()} тысяч")
amount = int(input("Введите сумму, которую необходимо взять из денежного ящика: "))
try:
    cash_box.take_away(amount)
except ValueError as e:
    print(e)
print(f"В кассе осталось {cash_box.amount} денег")