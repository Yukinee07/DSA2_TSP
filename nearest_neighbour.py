import sys
import time

def nearest_neighbor_tsp(dists, return_to_start=False):
    """
    Approximate TSP solution using the Nearest Neighbor heuristic.
    If return_to_start is False, the route will not return to the starting city.
    dists: 2D list or matrix of distances between cities.
    Returns (total_cost, path_indices).
    """
    n = len(dists)
    unvisited = set(range(1, n))
    path = [0]  # start at city 0
    total_cost = 0

    current = 0
    while unvisited:
        # Find nearest unvisited city
        next_city = min(unvisited, key=lambda city: dists[current][city])
        total_cost += dists[current][next_city]
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    if return_to_start:
        # Return to start city to complete the cycle
        total_cost += dists[current][0]
        path.append(0)

    return total_cost, path

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
        print("Usage: python nearest_neighbour.py distance_file.csv hours_file.csv")
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
    # Set return_to_start=False to avoid returning to the start city
    cost, path_indices = nearest_neighbor_tsp(dists, return_to_start=False)
    end_time = time.time()

    # Convert path to city names
    path_names = [city_names[i] for i in path_indices]

    # Print TSP path and cost
    print("Nearest Neighbor TSP Path based on distance (no return to start):")
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
