nums = []

with open("numbers") as f:
    nums = list(map(int, f.readlines()))

    for x in nums:
        for y in nums:
            if x + y == 2020:
                print(x * y)

    for x in nums:
        for y in nums:
            for z in nums:
                if x + y + z == 2020:
                    print(x * y * z)