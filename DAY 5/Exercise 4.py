def count_primes(numbers):

    prime_numbers=[2]
    iterations = 3

    if numbers<2:
        return 0
    while iterations<=numbers:
        for n in range(3,iterations,2):
            if iterations %n ==0:
                iterations+=2
                break
        else:
            prime_numbers.append(iterations)
            iterations+=2

    print(prime_numbers)
    return len(prime_numbers)

print(count_primes(50))


