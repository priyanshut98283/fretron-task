import matplotlib.pyplot as plt

def draw_flight_paths(flights):
    colors = ['red', 'blue', 'green']
    
    plt.figure(figsize=(8, 6))
    
    for i, flight in enumerate(flights):
        x_coords, y_coords = zip(*flight)
        plt.plot(x_coords, y_coords, marker='o', color=colors[i], label=f'Flight {i+1}')
        
        for j, (x, y) in enumerate(flight):
            plt.text(x, y, f'({x},{y})', fontsize=9, ha='right')
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Flight Paths')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example input
flights = [
    [(1, 1), (2, 2), (3, 3)],
    [(1, 1), (2, 4), (2, 2)],
    [(1, 1), (4, 2), (3, 4)]
]

draw_flight_paths(flights)
