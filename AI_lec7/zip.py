
num = list(range(1,10))
days = ['mon','tue','wed','thu','fri','sat','sun']


for number, day in zip(num, days):
    print(day, 'is day', number)
    
days_pair = [(number,day) for number,day in zip(num, days) if 0<number<8]
             
print(days_pair)