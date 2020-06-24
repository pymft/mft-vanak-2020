def stars(n: int, pattern: str = "*"):
    for i in range(n):
        print(pattern * n)


stars(4)
stars(5, pattern="$")
