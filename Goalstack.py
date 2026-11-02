
# Initial state
on = {
    'A': 'table',
    'B': 'table',
    'C': 'B'
}

# Goal state
goal = {
    'A': 'B',
    'B': 'C',
    'C': 'table'
}

# Goal Stack Planning
def planning():
    actions = []

    # Move C to table
    if on['C'] != 'table':
        actions.append("UNSTACK C from B")
        actions.append("PUTDOWN C")
        on['C'] = 'table'

    # Move B onto C
    if on['B'] != 'C':
        actions.append("PICKUP B")
        actions.append("STACK B on C")
        on['B'] = 'C'

    # Move A onto B
    if on['A'] != 'B':
        actions.append("PICKUP A")
        actions.append("STACK A on B")
        on['A'] = 'B'

    print("Actions:")
    for action in actions:
        print(action)

    print("\nFinal State:")
    print(on)


planning()
