def print_pyramid(pyramid):
    if pyramid < 1 or pyramid > 8:
        print("Out of range. I said ' 1-8 ' ... ")
        return

    for i in range(1, pyramid + 1):
        spaces = " " * (pyramid - i)
        hashes = "#" * i
        print(spaces + hashes)


if __name__ == "__main__":
    pyramid = int(input("How tall do u want the pyramid to be? (1-8): "))
    print_pyramid(pyramid)