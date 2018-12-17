n, current_days = map(int, input().split())
past_days = list(map(int, input().split()))

years = 0
streak = True
for days in past_days:
    if current_days < days and streak:
        years += 1
    elif current_days >= days:
        streak = False

if years == len(past_days):
    print('It had never snowed this early!')
else:
    print('It hadn\'t snowed this early in %d years!' % years)
