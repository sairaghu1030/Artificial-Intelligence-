class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2
    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2
    def __hash__(self):
        return hash((self.jug1, self.jug2))
def water_jug_dfs(current_state, jug_capacity1, jug_capacity2, target_volume, visited, path):
    if current_state in visited:
        return False
    visited.add(current_state)
    path.append(current_state)
    if current_state.jug1 == target_volume or current_state.jug2 == target_volume:
        print("Solution found:")
        print_path(path)
        return True
    if water_jug_dfs(State(jug_capacity1, current_state.jug2), jug_capacity1, jug_capacity2, target_volume, visited, path):
        return True
    if water_jug_dfs(State(current_state.jug1, jug_capacity2), jug_capacity1, jug_capacity2, target_volume, visited, path):
        return True
    if water_jug_dfs(State(0, current_state.jug2), jug_capacity1, jug_capacity2, target_volume, visited, path):
        return True
    if water_jug_dfs(State(current_state.jug1, 0), jug_capacity1, jug_capacity2, target_volume, visited, path):
        return True
    transfer_amount = min(current_state.jug1, jug_capacity2 - current_state.jug2)
    if water_jug_dfs(State(current_state.jug1 - transfer_amount, current_state.jug2 + transfer_amount),
                      jug_capacity1, jug_capacity2, target_volume, visited, path):
        return True
    transfer_amount = min(jug_capacity1 - current_state.jug1, current_state.jug2)
    if water_jug_dfs(State(current_state.jug1 + transfer_amount, current_state.jug2 - transfer_amount),
                      jug_capacity1, jug_capacity2, target_volume, visited, path):
        return True
    path.pop()  # Backtrack
    return False
def print_path(path):
    for state in path:
        print(f"Jug1: {state.jug1}, Jug2: {state.jug2}")
    print()
def water_jug_problem(jug_capacity1, jug_capacity2, target_volume):
    start_state = State(0, 0)
    visited = set()
    path = []
    if not water_jug_dfs(start_state, jug_capacity1, jug_capacity2, target_volume, visited, path):
        print("No solution found.")
# Example usage:
jug_capacity1 = 4
jug_capacity2 = 3
target_volume = 2

water_jug_problem(jug_capacity1, jug_capacity2, target_volume)
