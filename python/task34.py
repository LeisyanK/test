ПРОСТЫЕ ЧИСЛА (ИЗ ИНТЕРНЕТА)

def primes(n, verbose=0):
    """ Returns  a list of primes < n """
    # (c) Robert William Hanks - https://stackoverflow.com/a/3035188/5741205
    def pr(*args):
        if verbose > 0:
            print(*args)
    sieve = [True] * n
    pr("все чётные числа игнорируются и будут пропущены при возврате...\n")
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            pr('содержимое решета:\t{}'.format([x for x in range(3,n,2) if sieve[x]]))
            pr(f'i:{i} вычёркиваем все числа кратные "{i}", начиная с "{i}^2": {list(range(i*i, n, 2*i))}')
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
            pr(f'sieve[{i}*{i}::2*{i}]=[False]*(({n-i}*{i-1})//(2*{i})+1)')
            pr('содержимое решета:\t{}'.format([x for x in range(3,n,2) if sieve[x]]))
            pr('*' * 60)
    return [2] + [i for i in range(3,n,2) if sieve[i]]