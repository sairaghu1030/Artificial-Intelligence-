class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = 0
    def move_left(self):
        if self.position > 0:
            self.position -= 1
    def move_right(self):
        if self.position < len(self.environment) - 1:
            self.position += 1
    def clean(self):
        if self.environment[self.position] == 1:
            print(f"Cleaning dirty square at position {self.position}")
            self.environment[self.position] = 0
        else:
            print(f"No dirt to clean at position {self.position}")
    def print_environment(self):
        print("Environment:", self.environment)
# Example usage
if __name__ == "__main__":
    # Initialize environment (0 represents a clean square, 1 represents a dirty square)
    environment = [0,1]
    # Create a vacuum cleaner
    vacuum_cleaner = VacuumCleaner(environment)
    # Display initial environment
    vacuum_cleaner.print_environment()
    # Move and clean
    vacuum_cleaner.move_right()
    vacuum_cleaner.clean()
    # Display updated environment
    vacuum_cleaner.print_environment()
