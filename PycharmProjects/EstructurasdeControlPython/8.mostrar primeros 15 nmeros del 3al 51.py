if __name__ == '__main__':
    for num in range(3, 51):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)