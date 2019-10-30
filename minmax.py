the_array = [15, 22, 84, 14, 88, 23]

def maxMinSum(list):
    x = max(list)
    y = min(list)
    diff = x - y
    return x, y, diff



def main():
    print(maxMinSum(the_array))

if __name__ == '__main__':
    main()