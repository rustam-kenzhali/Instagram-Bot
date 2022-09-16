count = int(input())
minutes = input().split()
minutes = [int(i) for i in minutes]

frs, third, fifth = 0, 0, 0

for i in range(count - 1):
    fifth = (fifth + minutes[i])*2

print(fifth)

