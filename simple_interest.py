# Python3 program to find simple interest
# for given principal amount, time and
# rate of interest.


def simple_interest(principle, time, rate):
    print('The principal is', principle)
    print('The time period is', time)
    print('The rate of interest is', rate)

    si = (principle * time * rate) / 100

    print('The Simple Interest is', si)
    return si


# Driver code
simple_interest(10000, 5, 3)
