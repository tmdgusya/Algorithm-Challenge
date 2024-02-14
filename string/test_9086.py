# strings that user typped go through this stream 
# T is the number of chances that user can type string
T = int(input())

for i in range(0, T):
    given_string = input()
    print(given_string[0]+given_string[-1])

