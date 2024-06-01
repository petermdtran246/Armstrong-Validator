def Armstrong(n):
    sum = 0
    m = n
    while n > 0:
        r = n % 10
        n = n // 10
        sum += r*r*r
    if sum == m:
        print('Armstrong.')
    else:
        print('Not an Armstrong.')

n = int(input('Enter n: '))
Armstrong(n)