# Define the grid world
grid_world = [[0, 1, -1], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
start_state = [3, 0]
goal_state = [0, 1]
penality_state = [0,2]
obstacle = [2,1]
gamma = 0.95
epsilon = 0.0001
step_cost = -0.04

# Define the actions
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the transition probabilities
prob_dir_action = 0.7
prob_perp_action = 0.15

# Define the utility function
utility1 = [[0, 1, -1], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
utility2 = [[0, 1, -1], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Value Iteration algorithm
iteration=0
while True:
    # print("hi")
    delta = -float('inf')
    # utility1 = utility2.copy()
    utility1 = [[element for element in row] for row in utility2]
    # print(utility1)
    for i in range(4):
        for j in range(3):
            if [i, j] == goal_state or [i, j] ==penality_state or [i, j] ==obstacle:
                continue
            # print("hi")
            max_utility = -float('inf')
            for a in actions:
                next_i, next_j = i + a[0], j + a[1]
                if next_i < 0 or next_i >= 4 or next_j < 0 or next_j >= 3:
                    next_i, next_j = i, j
                if [next_i, next_j] == [2, 1]:#wall
                    next_i, next_j = i, j

                expected_utility = prob_dir_action *(step_cost + gamma*utility1[next_i][next_j])
                for b in actions:
                    if (b == a) or ((a[0]== -b[0]) and (a[1]== -b[1])) :
                        continue
                    next_i2, next_j2 = i + b[0], j + b[1]
                    if next_i2 < 0 or next_i2 >= 4 or next_j2 < 0 or next_j2 >= 3:
                        next_i2, next_j2 = i, j
                    if [next_i2, next_j2] == [2, 1]:#wall
                        next_i2, next_j2 = i, j

                    expected_utility += prob_perp_action * (step_cost + gamma*utility1[next_i2][next_j2])
                if expected_utility > max_utility:
                    max_utility = expected_utility
            utility2[i][j] = max_utility
            # print(utility1[i][j],utility2[i][j])
            delta = max(delta, abs(utility2[i][j] - utility1[i][j]))
            # print(delta)
    print("iteration:",iteration,"\n")
    for row in utility2:
        print(row)
    print("\n","--------------------------------------------------------")
    iteration+=1
    if delta < epsilon:
        break

# Print the utility values for each cell
# print(iteration)
for row in utility2:
    print(row)
print("\n")

# -------------------------------------BONUS-----------------------------------------------------

# Define the optimal policy for each cell
policy = [['*' for _ in range(3)] for _ in range(4)]

for i in range(4):
    for j in range(3):
        if [i, j] == goal_state or [i, j] ==penality_state or [i, j] ==obstacle:
            continue
        max_utility = -float('inf')
        best_action = None
        for a in actions:
            next_i, next_j = i + a[0], j + a[1]
            if next_i < 0 or next_i >= 4 or next_j < 0 or next_j >= 3:
                next_i, next_j = i, j
            if [next_i, next_j] == [2, 1]: # wall
                next_i, next_j = i, j

            expected_utility = prob_dir_action * (step_cost + gamma * utility2[next_i][next_j])
            for b in actions:
                if (b == a) or ((a[0] == -b[0]) and (a[1] == -b[1])):
                    continue
                next_i2, next_j2 = i + b[0], j + b[1]
                if next_i2 < 0 or next_i2 >= 4 or next_j2 < 0 or next_j2 >= 3:
                    next_i2, next_j2 = i, j
                if [next_i2, next_j2] == [2, 1]: # wall
                    next_i2, next_j2 = i, j

                expected_utility += prob_perp_action * (step_cost + gamma * utility2[next_i2][next_j2])
            if expected_utility > max_utility:
                max_utility = expected_utility
                best_action = a
        if best_action == (0, 1):
            policy[i][j] = '→'
        elif best_action == (0, -1):
            policy[i][j] = '←'
        elif best_action == (1, 0):
            policy[i][j] = '↓'
        elif best_action == (-1, 0):
            policy[i][j] = '↑'

# Print the optimal policy for each cell
for row in policy:
    print(row)