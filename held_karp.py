import itertools
import sys
import time

def held_karp(dists):
    n = len(dists)
    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2**n - 1) - 1
    res = [(C[(bits, k)][0] + dists[k][0], k) for k in range(1, n)]
    opt, parent = min(res)

    path = []
    for _ in range(n - 1):
        path.append(parent)
        bits, parent = bits & ~(1 << parent), C[(bits, parent)][1]
    path.append(0)
    path.reverse()

    return opt, path

def read_distances_with_names(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    city_names = lines[0].split(',')
    dists = [[int(x) for x in line.split(',')] for line in lines[1:]]
    return city_names, dists

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python held_karp.py filename.csv")
        sys.exit(1)

    filename = sys.argv[1]
    city_names, dists = read_distances_with_names(filename)

    # Print distance matrix
    for row in dists:
        print(' '.join([str(n).rjust(3) for n in row]))
    print()

    start_time = time.time()
    cost, path_indices = held_karp(dists)
    end_time = time.time()

    # Convert path to city names
    path_names = [city_names[i] for i in path_indices]

    # Print result
    print((cost, path_names))
    print(f"\nComputation Time: {end_time - start_time:.4f} seconds")
