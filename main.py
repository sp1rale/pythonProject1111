def draw_line(length, direction, character):
    if direction == "горизонтальна":
        print(character * length)
    elif direction == "вертикальна":
        for _ in range(length):
            print(character)

draw_line(10, "горизонтальна", "-")

draw_line(5, "вертикальна", "|")
