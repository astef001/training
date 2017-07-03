def nr_gen(stop, start=1):
    n = stop
    while n >= start:
        yield n
        if n == 1:
            break
        if n % 2:
            n = 3*n+1
        else:
            n = int(n/2)


def main():
    with open("input.in","r") as f:
        while True:
            try:
                start, stop = [int(x) for x in next(f).split()]
            except StopIteration:
                break
            else:
                all_gen = [nr_gen(x) for x in range(start, stop+1)]
                sums = []
                for x in all_gen:
                    sums.append(sum(1 for i in x))
                print(start, stop, max(sums))
