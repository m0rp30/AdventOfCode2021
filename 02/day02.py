file_name = 'day02.txt'

def part_one():
    pos = 0
    depth = 0
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            cmd, move = line.rstrip('\n').split(' ')

            if cmd == 'forward':
                pos += int(move)

            if cmd == 'down':
                depth += int(move)
            elif cmd == 'up':
                depth -= int(move)

    print(f"Part one: {pos * depth}")

def part_two():
    pos = 0
    depth = 0
    aim = 0
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
        
        for line in lines:
            cmd, move = line.rstrip('\n').split(' ')

            if cmd == 'forward':
                pos += int(move)
                depth = depth + (int(move) * aim)

            if cmd == 'down':
                aim += int(move)
            elif cmd == 'up':
                aim -= int(move)
    
    print(f"Part two: {pos * depth}")

if __name__ == '__main__':
    part_one()
    part_two()
