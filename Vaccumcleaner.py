
# Simple Reflex Vacuum Cleaner Agent

def vacuum_agent(location, status):

    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Move Right"

    else:
        return "Move Left"


# Environment
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

# Run agent
for i in range(6):

    status = rooms[location]

    print("Location:", location)
    print("Status:", status)

    action = vacuum_agent(location, status)
    print("Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    print("Rooms:", rooms)
    print("----------------")

print("Final Environment:", rooms)
