# Jun-seo has a bag that can contain N things and limits K kg
# Each item that Jun-seo has W weight and V value.
# Which way will be best way that satisfy Jun-seo's traveling before serving military

max_numbers, max_weight = map(int, input().split())

# solution (simple)
# we gonna be saving the way of deviding vlaue by weight
# and storing this values with weight [(divided, weight)] into array
# and re-odering that array by desending
# and pop off the element from the first index of array until reach the max_weight
# What if there is values like the one below
# (value, weight) [(13, 6), (8, 4), (6, 3), (12, 5)]
# they are gonna be like that after calculations
# what if only takes the lightest one
# [(100, 10), (20, 5)]
values = []
for i in range(0, max_numbers):
    # this w, v will be the weight and value of product
    W, V = map(int, input().split())
    ratio = W / V
    values.append([ratio, V, W])

values = sorted(values, key=lambda v: -v[0])

acc = 0
index = 0
answer = 0
while acc <= max_weight and index < len(values):
    accum = acc + values[index][2]
    if accum > max_weight:
        index += 1
        continue
    acc += values[index][2]
    answer += values[index][1]

print(answer)


