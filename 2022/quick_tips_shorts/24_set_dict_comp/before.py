def main():
    my_set: set[int] = {i * i for i in range(10)}
    print(my_set)

    my_dict: dict[int, int] = {i: i * i for i in range(10)}
    print(my_dict)


if __name__ == "__main__":
    main()
