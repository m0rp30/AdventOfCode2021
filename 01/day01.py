
file_name = "day01.txt"

def part_one():

    result = 0
    with open(file_name, 'r') as f:
        lines = f.readlines()
        last = int(lines[0])

        for line in lines[1:]:
            if last < int(line):
                result += 1
            last = int(line)

    print(f"Part one: {result}")

def part_two():
    result = 0
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lenght = len(lines)

        if lenght >= 3:
            last = int(lines[0]) + int(lines[1]) + int(lines[2])
            
        for i in range(1, lenght):
            current = -1

            if i + 2 < lenght:
                current = int(lines[i]) + int(lines[i + 1]) + int(lines[i +2])
            else:
                break
            
            if last < current:
                result += 1

            last = current
            
    print(f"Part two: {result}")

if __name__ == "__main__":
    part_one()
    part_two()
