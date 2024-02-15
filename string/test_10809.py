# the result will be the index of first occurence of an alphabet letter within the strings.
print(*map(input().find, map(chr, range(97, 123))))
