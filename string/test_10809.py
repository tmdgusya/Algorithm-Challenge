from typing import List
# the result will be the index of first occurence of an alphabet letter within the strings.

given_string: str = input()
words: dict[str, int] = {}

alphabet: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(0, len(given_string)):
    if words.get(given_string[i]) is None:
        words[given_string[i]] = i

answer: List[int] = []
for i in range(0, len(alphabet)):
    index: int | None = words.get(alphabet[i])
    if index == None:
        answer.append(-1)
    else:
        answer.append(index)

print(*answer, sep=' ')
print('1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1')
