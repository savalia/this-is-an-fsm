"""
Example: waiting.py
Start from "Waiting", trigger the next expected event ('process') and return the resulting state.
"""
from loader import load_fsm_from_json

CONFIG_PATH = "fsm_config.json"


def run(start_state_name: str = "Waiting") -> str:
    """Load the FSM from JSON with the given start state, perform the next expected event,
    and return the resulting state.
    """
    fsm, _ = load_fsm_from_json(CONFIG_PATH, start_state_name=start_state_name)
    # From Waiting -> 'process' -> Processing
    fsm.trigger("process")
    return fsm.get_state()


if __name__ == "__main__":
    print(run())