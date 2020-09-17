import cProfile

def get_next_pair(red, blue):
    while True:
        while True:
            top = 2 * (blue * (blue - 1))
            bot = ((red + blue) * (red + (blue - 1)))
            if top < bot:
                blue += 1
            elif top == bot:
                return red, blue
            else:
                break
        red += 1

# old_red = 6
# old_blue = 15

# new_red = 35
# new_blue = 85

# while True:
#     part_red = new_red / old_red
#     part_blue = new_blue / old_blue

#     try_red = int(new_red * part_red)
#     try_blue = int(new_blue * part_blue)

#     old_red = new_red
#     old_blue = new_blue
#     new_red, new_blue = get_next_pair(try_red, try_blue)
#     if new_red + new_blue >= 1_000_000_000_000:
#         print(new_blue)
#         break

def get_solution(target=1_000_000_000_000):
    old_red = 6
    old_blue = 15

    new_red = 35
    new_blue = 85

    while True:
        part_red = new_red / old_red
        part_blue = new_blue / old_blue

        try_red = int(new_red * part_red)
        try_blue = int(new_blue * part_blue)

        old_red = new_red
        old_blue = new_blue
        new_red, new_blue = get_next_pair(try_red, try_blue)
        if new_red + new_blue >= target:
            return new_blue

cProfile.run('get_solution()')