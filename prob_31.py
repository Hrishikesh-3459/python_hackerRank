# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar


s = input().split()

m = int(s[0])
d = int(s[1])
y = int(s[2])

print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())

