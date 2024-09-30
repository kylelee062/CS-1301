import random
import helper

grid_size = 15
grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
grid[7][7] = 1

x = 7 
y = 7 

def agent_mover(grid):
    random.seed(43543)
    global x
    global y
    for i in range(100):
        rand_num = random.randint(1, 20)
        if 1 <= rand_num <= 7:  # then the agent will move up in the grid.
            if x > 0:
                x -= 1
                grid[x][y] += 1
        elif 8 <= rand_num <= 14:  # then the agent will move down in the grid.
            if x < 14:
                x += 1
                grid[x][y] += 1
        elif 15 <= rand_num <= 17:  # then the agent will move left in the grid.
            if y > 0:
                y -= 1
                grid[x][y] += 1
        elif 18 <= rand_num <= 20:  # then the agent will move right in the grid.
            if y < 14:
                y += 1
                grid[x][y] += 1
    return grid



print("Movement Heat Map")
helper.print_grid(agent_mover(grid))
print(f"Agent's Final Position: ({x},{y})")
print(f'Distance: {abs(x-7)+abs(y-7)}')

