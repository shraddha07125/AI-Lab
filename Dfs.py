
# DFS for Water Jug Problem

def dfs():

    stack = [(0, 0)]
    visited = []

    while stack:

        a, b = stack.pop()

        if (a, b) in visited:
            continue

        visited.append((a, b))

        print("Jug A:", a, "Jug B:", b)

        # Goal condition
        if a == 2:
            print("Goal Reached!")
            return

        # Possible operations

        # Fill Jug A
        stack.append((4, b))

        # Fill Jug B
        stack.append((a, 3))

        # Empty Jug A
        stack.append((0, b))

        # Empty Jug B
        stack.append((a, 0))

        # Pour A into B
        pour = min(a, 3 - b)
        stack.append((a - pour, b + pour))

        # Pour B into A
        pour = min(b, 4 - a)
        stack.append((a + pour, b - pour))

    print("No Solution Found!")


dfs()
