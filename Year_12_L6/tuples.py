from haversine import haversine

london = (51.5074, -0.1278)  # Latitude and Longitude of London
paris = (48.8566, 2.3522)    # Latitude and Longitude of Paris
new_york = (40.7128, -74.006)  # Latitude and Longitude of New York City
tokyo = (35.6895, 139.6917)   # Latitude and Longitude of Tokyo

shortest_distance = float('inf')
route = []

for i in [london, paris, new_york, tokyo]:
    for j in [london, paris, new_york, tokyo]:
        for k in [london, paris, new_york, tokyo]:
            for l in [london, paris, new_york, tokyo]:
                if len({i, j, k, l}) == 4:  # Ensure all cities are unique
                    distance = (haversine(i, j) +
                                haversine(j, k) +
                                haversine(k, l))
                    
                    name_i = "London" if i == london else "Paris" if i == paris else "New York" if i == new_york else "Tokyo"
                    name_j = "London" if j == london else "Paris" if j == paris else "New York" if j == new_york else "Tokyo"
                    name_k = "London" if k == london else "Paris" if k == paris else "New York" if k == new_york else "Tokyo"
                    name_l = "London" if l == london else "Paris" if l == paris else "New York" if l == new_york else "Tokyo"

                    if distance < shortest_distance:
                        shortest_distance = distance
                        route = [name_i, name_j, name_k, name_l]

                    #print(f"Route: {name_i} -> {name_j} -> {name_k} -> {name_l} | Distance: {distance:.2f} km")

print("Shortest route:", route)
print("Shortest distance (km):", shortest_distance)
