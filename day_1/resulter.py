left = []
right = []
distances = []

with open("input", "r") as numbers:
    loaded = numbers.readlines()

    for pair in loaded:
        left.append(int(pair.split(" ")[0]))
        right.append(int(pair.split(" ")[3].strip()))

left.sort()
right.sort()

for i, n in enumerate(left):
    dif = right[i] - n
    distances.append(abs(dif))


print(sum(distances))

#my answer = 1882714


