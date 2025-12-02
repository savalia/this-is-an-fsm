# fsm.py
from state import State

class FiniteStateMachine:
    def __init__(self, initial_state: State, unknown_state: State):
        # Code review comment -> Added type checks for initial_state and unknown_state.
        if not isinstance(initial_state, State) or not isinstance(unknown_state, State):
            raise TypeError("Initial and unknown states must be State instances.")
        self.current_state = initial_state
        self.unknown_state = unknown_state
        self.current_state.enter()

    def trigger(self, event):
        # Code review comment -> Added validation for event type and non-empty string.
        if not isinstance(event, str) or not event.strip():
            raise ValueError("Event must be a non-empty string.")

        next_state = self.current_state.get_next_state(event)
        if next_state:
            self.current_state.exit()
            self.current_state = next_state
            self.current_state.enter()
        else:
            print(f"No valid transition for event '{event}' from state '{self.current_state.name}'.")
            self.current_state.exit()
            # Code review comment -> Recovery logic: if in Unknown and event is reset, go to Idle.
            if self.current_state == self.unknown_state and event == "reset":
                self.current_state = self.unknown_state.get_next_state("reset") or self.unknown_state
            else:
                self.current_state = self.unknown_state
            self.current_state.enter()

    def get_state(self):
        return self.current_state.name