# loader.py
import json
from state import State
from fsm import FiniteStateMachine

def load_fsm_from_json(config_path, start_state_name=None):
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        # Code review comment -> Added error handling for missing config file.
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
    except json.JSONDecodeError as e:
        # Code review comment -> Added error handling for invalid JSON format.
        raise ValueError(f"Invalid JSON format in '{config_path}': {e}")

    # Code review comment -> Create State objects with JSON-defined on_enter/on_exit messages.
    states = {}
    for state_def in config.get("states", []):
        name = state_def.get("name")
        if not name:
            raise ValueError("Each state must have a 'name' field.")
        enter_msg = state_def.get("on_enter")
        exit_msg = state_def.get("on_exit")

        def make_enter(msg):
            return lambda s: print(msg) if msg else None

        def make_exit(msg):
            return lambda s: print(msg) if msg else None

        states[name] = State(name, make_enter(enter_msg), make_exit(exit_msg))

    # Code review comment -> Add transitions from config.
    for state_name, transitions in config.get("transitions", {}).items():
        if state_name not in states:
            raise ValueError(f"Transition defined for unknown state '{state_name}'.")
        for event, next_state_name in transitions.items():
            if next_state_name not in states:
                raise ValueError(f"Transition from '{state_name}' points to unknown state '{next_state_name}'.")
            states[state_name].add_transition(event, states[next_state_name])

    # Code review comment -> Determine initial state from parameter or default in config.
    if start_state_name:
        if start_state_name not in states:
            raise ValueError(f"Invalid start state: {start_state_name}")
        initial_state = states[start_state_name]
    else:
        default_initial = config.get("default_initial")
        if default_initial not in states:
            raise ValueError("Default initial state in config is invalid.")
        initial_state = states[default_initial]

    return FiniteStateMachine(initial_state, states["Unknown"]), states