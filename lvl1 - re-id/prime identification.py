def getPrimes(i):
    primes= '2'
    start_num = 2
    while i+4 >= len(primes):
        start_num = start_num + 1
        prime = True
        for number in range(2,int(start_num/2) + 1):
            if start_num%number == 0:
                prime = False
                break
        if prime == True:
            primes += str(start_num)
    return primes

def solution(i):
    # Your code here
    primes = getPrimes(i)
    return primes[i:i+5]

if __name__ == '__main__':
    print(solution(0))
    print(solution(3))
    print(solution(70))