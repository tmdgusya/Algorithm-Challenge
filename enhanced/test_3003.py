
standard = [1, 1, 2, 2, 2, 8]
owns = list(map(int, input().split()))
# O(1) -> O(5)
# Time complexity doesn't increase futhur as we already know limit of this function
for i in range(0, len(standard)):
    print(standard[i] - owns[i], end=" ")

