limit = float(input())
n = int(input())
amount = n
error_amount = 0
more_limit = 0
max = -9999
middle_value = 0
for i in range(n):
    x = input()
    if x != 'error':
        x = float(x)
        if x > limit:
            more_limit += 1
        if x > max:
            max = x
        middle_value += x
    else:
        error_amount += 1
print(amount, error_amount, more_limit, f'{max:.1f}', f'{middle_value/(amount - error_amount):.1f}', sep='\n')
