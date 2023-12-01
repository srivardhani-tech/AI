import sys
import itertools

def calculate_distance(city1, city2):
    # Assuming city1 and city2 are tuples of (x, y) coordinates
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def nearest_neighbor_algorithm(cities):
    num_cities = len(cities)
    unvisited_cities = set(range(num_cities))
    current_city = 0  # Start from the first city
    tour = [current_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: calculate_distance(cities[current_city], cities[city]))
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(tour[0])  # Return to the starting city

    return tour

def total_distance(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Example usage:
cities = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
shortest_tour = nearest_neighbor_algorithm(cities)
print("Shortest tour:", shortest_tour)
print("Total distance:", total_distance(shortest_tour, cities))
