a = list(map(int, input().split()))
for n in 3,5,7,9:
	if n in a:
		a.remove(n)

a,b,c = int(input()), int(input()), int(input())
print("YES" if a+b == c else "NO")
