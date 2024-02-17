# how to check whether this string is palindrome or not
# checking this string in bruth-force way
# first, check the firs character of this string, and the end char of this string
# if they are not same character, this function gonna return false
# if they are matched each other, this function gonna return true
def is_matched(start: str, end: str) -> bool:
    return start == end

given_string = input()
limit = int(len(given_string) / 2)
# We gonna iterate over this given string
# We can iterate over this give string until the index `i` reach half of length of this string ( len(given_string) / 2 )
for i in range(0, limit):
    if not is_matched(given_string[i], given_string[-(i+1)]):
        print("0")
        exit(0)

print("1")
