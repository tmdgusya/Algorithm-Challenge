text = input()
t = text[::-1]  # Reverse the string
print("1" if all(c == t[i] for i, c in enumerate(text)) else "0", end="")

