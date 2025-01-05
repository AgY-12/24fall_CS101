n = int(input())
cube = {i**3: i for i in range(2, n+1)}
reversed_cube = {v: k for k, v in cube.items()}
ans = []
for b in range(2, n):
    for c in range(b, n):
        for d in range(c, n):
            if (a := reversed_cube[b]+reversed_cube[c]+reversed_cube[d]) in cube:
                ans.append((cube[a], b, c, d))
ans.sort()
for s in ans:
    print(f"Cube = {s[0]}, Triple = ({s[1]},{s[2]},{s[3]})")