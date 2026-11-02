
# Initial and goal state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# BFS function
def bfs():

    queue = [(start, [])]
    visited = []

    while queue:

        state, path = queue.pop(0)

        if state == goal:
            return path + [state]

        if state not in visited:

            visited.append(state)

            zero = state.index(0)

            moves = [-3, 3, -1, 1]

            for move in moves:

                new_pos = zero + move

                if 0 <= new_pos < 9:

                    if move == -1 and zero % 3 == 0:
                        continue

                    if move == 1 and zero % 3 == 2:
                        continue

                    new_state = list(state)

                    new_state[zero], new_state[new_pos] = (
                        new_state[new_pos], new_state[zero]
                    )

                    if new_state not in visited:
                        queue.append((tuple(new_state), path + [state]))

    return None


# Display solution
result = bfs()

if result:

    print("Solution Found!")

    for i, state in enumerate(result):

        print("\nStep", i)

        for j in range(0, 9, 3):
            print(state[j:j+3])

    print("\nTotal Moves:", len(result) - 1)

else:
    print("No Solution Found!")
