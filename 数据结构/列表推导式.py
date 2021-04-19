vec = [2, 4, 6]
[3*x for x in vec]

[[x, x**2] for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

[3*x for x in vec if x > 3]
[3*x for x in vec if x < 2]

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
[x*y for x in vec1 for y in vec2]
[x+y for x in vec1 for y in vec2]
list=[vec1[i]*vec2[i] for i in range(len(vec1))]
print(list)

[str(round(355/113, i)) for i in range(1, 6)]