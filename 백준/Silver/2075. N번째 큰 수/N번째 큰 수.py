def main() -> None:  # Sliding Window
    n: int = int(input())
    num: list[int] = []

    num = sorted(list(map(int, input().split())))

    for i in range(n-1):
        tmp = sorted(list(map(int, input().split())))

        for j in range(n):
            if num[0] < tmp[j]:
                num[0] = tmp[j]
                num.sort()

    print(num[0])
    

if __name__ == '__main__':
    main()