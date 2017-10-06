


import itertools
import random

# https://dfns.dyalog.com/s_life.htm
# for _ in xrange(10):

def main():
    on_rules = [(1,1,1), (1,1,0), (1,0,1), (0,0,1)]
    initial = [random.randint(0, 1) for _ in itertools.repeat(None, 18)]
    iterations = 10
    fixed_boundary = False
    
    
    arr = initial if isinstance(initial, list) else (
            [int(i) for i in str(initial)])
    length = len(initial)
    
    print("on rules:", on_rules)
    print("initial:", str(initial))
    print("iterations:", iterations)
    print("length:", length)
    print("".join(str(e) for e in arr), "(initial)")
    for i in range(iterations):
        copy = list(arr)
        # index out of bounds
        arr[0] = 1 if ((0 if fixed_boundary else copy[-1]),
                copy[0], copy[1]) in on_rules else 0
        arr[-1] = 1 if (copy[-2], copy[-1],
                (0 if fixed_boundary else copy[0])) in on_rules else 0
        
        for j in range(1, length-1):
            arr[j] = 1 if (copy[j-1], copy[j], copy[j+1]) in on_rules else 0
        print("\n" + "".join(str(e) for e in arr))


if __name__ == "__main__":
    main()