import random

def read_sensors():
    left = random.choice([0, 1])
    center = random.choice([0, 1])
    right = random.choice([0, 1])
    obstacle = random.choice([True, False])
    return left, center, right, obstacle

def move_robot(left, center, right, obstacle):
    if obstacle:
        return "STOP - Obstacle detected"
    
    if center == 1:
        return "MOVE FORWARD"
    elif left == 1:
        return "TURN LEFT"
    elif right == 1:
        return "TURN RIGHT"
    else:
        return "SEARCHING PATH"

for _ in range(10):
    sensors = read_sensors()
    action = move_robot(*sensors)
    print(f"Sensors: {sensors} -> Action: {action}")
