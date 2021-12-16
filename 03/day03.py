file_name = 'input.txt'

def part_one():
    lenght = 0

    with open(file_name, 'r') as f:
        lines = f.readlines()
        lenght = len(lines[0].rstrip('\n'))

    count_one = [0] * lenght
    count_zero = [0] * lenght
    gamma_rate   = [0] * lenght
    epsilon_rate = [0] * lenght
    gamma_value = 0
    epsilon_value = 0
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lenght = len(lines[0].rstrip('\n'))
        
        for line in lines:
            line.rstrip('\n')
            for i in range(0, lenght):
                if line[i] == '1':
                  count_one[i] += 1
                else:
                  count_zero[i] += 1

    for i in range(0, lenght):
        if count_one[i] > count_zero[i]:
            gamma_rate[i] = 1
        else:
            epsilon_rate[i] = 1
    gamma_rate.reverse()
    epsilon_rate.reverse()
    for i in range(0, lenght):
        gamma_value += gamma_rate[i] * (2**i)
        epsilon_value += epsilon_rate[i] * (2**i)
    print(f"Result part one: {gamma_value * epsilon_value}")

def part_two():
    pass

if __name__ == '__main__':
    part_one()
    part_two()
