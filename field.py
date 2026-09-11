import turtle as t
def create_field():
    returned = ""
    print("напиши начальную координату x")
    x_start = int(input())
    print("напиши конечную координату x")
    x_end = int(input())
    
    print("напиши начальную координату y")
    y_start = int(input())
    print("напиши конечную координату y")
    y_end = int(input())
    
    print("напиши название перменной веса")
    weight = input()
    returned += f"t.up()\nt.tracer(0,0)\nfor x in range({x_start} , {x_end}):\n    for y in range({y_start}, {y_end}):\n        t.goto(x * {weight},y * {weight})\n        t.dot(10)"
    print("\n"+returned + "\n")
    