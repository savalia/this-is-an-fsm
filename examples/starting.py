"""
# Example: starting.py
# Demonstrates starting from the "Starting" state and performing the next transition.

from loader import load_fsm_from_json

CONFIG_PATH = "fsm_config.json"


def run(start_state_name: str = "Starting") -> str:
    """Load the FSM from JSON with the given start state, perform the next expected event,
    and return the resulting state."""
    fsm, _ = load_fsm_from_json(CONFIG_PATH, start_state_name=start_state_name)
    # From Starting the expected next event is 'ready' -> Waiting
    fsm.trigger("ready")
    return fsm.get_state()


if __name__ == "__main__":
    print(run())
"""