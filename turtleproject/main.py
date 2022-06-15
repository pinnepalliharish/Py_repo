# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.color("green","brown")
# timmy.shape("turtle")
# timmy.fd(100)
# my_s=Screen()
# my_s.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.field_names=["pokeman name","Types"]
table.add_rows(
    [
        ["pikachu","electric"],
        ["s","w"],
        ["d","g"]
    ]
)
table.align="l"
print(table)