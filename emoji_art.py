# print('\U0001f600' * 3)
emoji = '\U0001f600'

# Using while loop
# count = 1
# while count < 11:
#     print(emoji * count)
#     count += 1
    
# Using for loop
# for num in range(1,11):
#     print(emoji * num)

# Center the emojis
count = 1
while count < 20:
    print(' ' * (19 - count) + emoji * count)
    count += 2