class Board:
    def __init__(self, soldiers):
        self.soldiers = set(soldiers)
    
    def is_soldier_at(self, position):
        return position in self.soldiers

    def remove_soldier(self, position):
        if position in self.soldiers:
            self.soldiers.remove(position)
    
    def get_soldiers(self):
        return self.soldiers

class Castle:
    def __init__(self, start_position):
        self.position = start_position
    
    def move(self, direction):
        x, y = self.position
        if direction == 'left':
            return (x, y - 1)
        elif direction == 'right':
            return (x, y + 1)
        return self.position

def find_all_paths(castle, board, path=None):
    if path is None:
        path = []
    
    directions = ['left', 'right']
    all_paths = []
    
    for direction in directions:
        new_pos = castle.move(direction)
        
        if board.is_soldier_at(new_pos):
            board.remove_soldier(new_pos)  # Kill the soldier
            new_path = path + [f'Kill {new_pos}']
            
            # Move to the new position and continue finding paths
            castle.position = new_pos
            all_paths.extend(find_all_paths(castle, board, new_path))
            
            # Backtrack
            board.soldiers.add(new_pos)  # Restore soldier
            castle.position = path[-1] if path else castle.position  # Return to the previous position
    
    # If no more soldiers can be killed, add the final path
    if not all_paths and not board.get_soldiers():
        all_paths = [path + [f'Arrive ({castle.position[0]},{castle.position[1]})']]
    
    return all_paths

def get_input_coordinates(prompt, num_coordinates):
    coordinates = []
    for i in range(num_coordinates):
        coord = input(f"Enter coordinates for {prompt} {i+1}: ")
        x, y = map(int, coord.split(','))
        coordinates.append((x, y))
    return coordinates

def print_paths(paths):
    for index, path in enumerate(paths, start=1):
        print(f"\nPath {index}:")
        print("========")
        for step in path:
            print(step)

def main():
    num_soldiers = int(input("Enter number of soldiers: "))
    soldiers = get_input_coordinates("soldier", num_soldiers)
    
    castle_start = tuple(map(int, input("Enter the coordinates for your 'special' castle: ").split(',')))
    
    board = Board(soldiers)
    castle = Castle(castle_start)
    
    paths = find_all_paths(castle, board)
    
    if paths:
        print_paths(paths)
    else:
        print("No valid path found.")

# Run the program
main()
