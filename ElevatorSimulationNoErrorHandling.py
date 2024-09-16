class ElevatorState:
    def enter_state(self):
        print(self.__class__.__name__)

    def handle_event(self, event):
        pass

class IdleAtFirstFloor(ElevatorState):
    def handle_event(self, event):
        if event == "1":
            return OpenAtFirstFloor()
        elif event == "2":
            return MovingUp()
        return self

class IdleAtSecondFloor(ElevatorState):
    def handle_event(self, event):
        if event == "3":
            return OpenAtSecondFloor()
        elif event == "4":
            return MovingDown()
        return self

class OpenAtFirstFloor(ElevatorState):
    def handle_event(self, event):
        if event == "5":
            return IdleAtFirstFloor()
        elif event == "6":
            return MovingUp()
        return self

class OpenAtSecondFloor(ElevatorState):
    def handle_event(self, event):
        if event == "7":
            return IdleAtSecondFloor()
        elif event == "8":
            return MovingDown()
        return self

class MovingUp(ElevatorState):
    def handle_event(self, event):
        if event == "9":
            return OpenAtSecondFloor()
        return self

class MovingDown(ElevatorState):
    def handle_event(self, event):
        if event == "10":
            return OpenAtFirstFloor()
        return self

class ElevatorContext:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.current_state.enter_state()

    def trigger_event(self, event):
        new_state = self.current_state.handle_event(event)
        if new_state != self.current_state:
            self.current_state = new_state
            self.current_state.enter_state()

def main():
    context = ElevatorContext(IdleAtFirstFloor())
    while True:
        print("\n1. External Up at First Floor (Open Doors)")
        print("2. External Up at Second Floor (Move Up)")
        print("3. External Down at Second Floor (Open Doors)")
        print("4. External Down at First Floor (Move Down)")
        print("5. Close Doors at First Floor")
        print("6. Go to Second Floor from First Floor")
        print("7. Close Doors at Second Floor")
        print("8. Go to First Floor from Second Floor")
        print("9. Arrive at Second Floor")
        print("10. Arrive at First Floor")
        print("0. Exit")
        event = input("Enter choice: ")
        if event == "0":
            print("Exiting elevator simulation.")
            break
        context.trigger_event(event)

if __name__ == "__main__":
    main()
