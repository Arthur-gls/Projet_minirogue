


bg_test1 = ['--------',
           '|      |',
           '--------']

bg_test2 = ['--------',
           '|   G  |',
           '--------']

def print_bg(background):
    for line in background:
        print(line)

while True:
    print_bg(bg_test1)
    mvmt = input()
    if mvmt == 'a':
        print_bg(bg_test2)
    elif mvmt == 'b':
        break
    else:
        print_bg(bg_test1)

