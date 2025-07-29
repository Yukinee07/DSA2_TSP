# Heuristic and Exact Approaches to Solving the Travelling Salesman Problem (TSP)

This project provides practical and research-based implementations of two major algorithms—Held-Karp (exact) and Nearest Neighbor (heuristic)—to solve the Travelling Salesman Problem (TSP) on real-world datasets. You can apply these solutions to both **Malaysian cities** and intra-campus routes at **IIUM Gombak**.

## 📂 Project Structure

- `held_karp.py`: Python implementation of the Held-Karp algorithm (dynamic programming/exact TSP).
- `nearest_neighbour.py`: Python implementation of the Nearest Neighbor heuristic algorithm.
- `malaysia_city_distance.csv`: Distance matrix (km) for 10 major Malaysian cities.
- `hours_malaysia_city_distance.csv`: Travel time matrix (hours) for 10 cities.
- `iium_kulliyyah_distance.csv`: Walking distance matrix (meters) between IIUM Gombak kulliyyahs.
- `iium_kulliyyah_time_distance.csv`: Walking time matrix (minutes) for kulliyyahs.
- `README.md`: This file.
- `ex.csv`/`malaysia_city_distance.csv`/other datasets: Additional sample or experimental data.
- Other Python or CSV files provide supporting data and extend the capability for more scenarios.

## 📖 Project Overview

The Travelling Salesman Problem (TSP) seeks the shortest possible route visiting each node exactly once and returning to the start. TSP is NP-hard and highly relevant in logistics, delivery, and route optimization.

You can compare:
- **Exact Algorithm (Held-Karp)**—guarantees the shortest route for small to medium datasets.
- **Heuristic Algorithm (Nearest Neighbor)**—computes near-optimal tours much faster for large datasets.

The datasets include:
- Driving distances and times between Malaysian cities (for logistics scale problems).
- Walking distances and times between IIUM Gombak kulliyyahs (smaller, campus navigation problems).

## 🏁 How to Run

> **Make sure you have Python 3+ installed. All scripts use standard libraries; pandas is required (`pip install pandas`).**

### For Malaysian Cities

- **Held-Karp (Exact Solution):**
  ```
  python held_karp.py malaysia_city_distance.csv hours_malaysia_city_distance.csv
  ```
- **Nearest Neighbor (Approximate Solution):**
  ```
  python nearest_neighbour.py malaysia_city_distance.csv hours_malaysia_city_distance.csv
  ```

### For IIUM Kulliyyahs

- **Held-Karp (Exact Solution):**
  ```
  python held_karp.py iium_kulliyyah_distance.csv iium_kulliyyah_time_distance.csv
  ```
- **Nearest Neighbor (Approximate Solution):**
  ```
  python nearest_neighbour.py iium_kulliyyah_distance.csv iium_kulliyyah_time_distance.csv
  ```

### General Usage

Replace filenames with any compatible distance/time CSV matrices to solve for your own datasets.

## 🧩 Inputs

- **First argument:** CSV file of pairwise distances between locations.
- **Second argument:** CSV file of pairwise travel times (optional, for travel time reporting).

> All CSVs must be square matrices with the same header and row order (see sample files for format).

## 📊 Output

- The scripts output the shortest/approximate route, total distance, and total travel time on the console.
- For larger datasets, additional logs (computation time, step-by-step construction) may be displayed.

## 📝 References

- The methodology and algorithms follow the detailed explanations and experimental analysis provided in the attached project reports. For a deeper understanding of algorithm, data format, performance trade-offs, and use cases, consult the included PDF project documentation.

**Recommended:**  
Fork or clone the project, try your own data, and compare the efficiency and quality of both approaches for real-world route planning or coursework.
