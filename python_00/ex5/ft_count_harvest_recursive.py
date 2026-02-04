def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def ft_rec(day):
        if (day > n):
            print("Harvest time!")
            return
        else:
            print("DAY ",day)
            ft_rec(day + 1)
    ft_rec(1)
