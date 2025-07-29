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
    dists = [[float(x) for x in line.split(',')] for line in lines[1:]]
    return city_names, dists

def read_hours_matrix(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    hours = [[float(x) for x in line.split(',')] for line in lines]
    return hours

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python held_karp.py distance_file.csv hours_file.csv")
        sys.exit(1)

    distance_filename = sys.argv[1]
    hours_filename = sys.argv[2]

    city_names, dists = read_distances_with_names(distance_filename)
    hours_matrix = read_hours_matrix(hours_filename)

    # Print distance matrix
    print("Distance Matrix (KM):")
    for row in dists:
        print(' '.join([str(n).rjust(3) for n in row]))
    print()

    start_time = time.time()
    cost, path_indices = held_karp(dists)
    end_time = time.time()

    # Convert path to city names
    path_names = [city_names[i] for i in path_indices]

    # Print distance result
    print("Optimal TSP Path based on distance:")
    print((cost, path_names))
    print(f"\nComputation Time: {end_time - start_time:.4f} seconds")

    # Calculate total travel time based on hours matrix
    total_hours = 0.0
    print("\nTravel time between consecutive cities (in hours for cities/in minutes for kulliyyah):")
    for i in range(len(path_indices) - 1):
        from_city = path_indices[i]
        to_city = path_indices[i + 1]
        travel_time = hours_matrix[from_city][to_city]
        total_hours += travel_time
        print(f"{city_names[from_city]} -> {city_names[to_city]}: {travel_time}")

    print(f"\nTotal Travel Time: {round(total_hours, 2)}")
