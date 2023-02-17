def main() -> None:  # Two Pointers
    n, m = map(int, input().split())  # length, sum
    num: list[int] = list(map(int, input().split()))  # num
    count: int = 0
    start: int = 0
    end: int = 0

    while end < n:
        Sum: int = sum(num[start:end + 1])

        if Sum == m:
            count = count + 1
            end = end + 1
        elif Sum > m:
            start = start + 1
        else:
            end = end + 1

    print(count)


if __name__ == '__main__':
    main()
