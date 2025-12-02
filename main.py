# main.py (manual run)
from loader import load_fsm_from_json

if __name__ == "__main__":
    try:
        # Code review comment -> Example: start from default initial state.
        fsm, states = load_fsm_from_json("fsm_config.json")

        # Code review comment -> Example: start from a different initial state.
        # fsm, states = load_fsm_from_json("fsm_config.json", start_state_name="Processing")

        events = ["stop", "reset", "start", "ready", "process", "monitor", "stop", "reset"]
        for event in events:
            print(f"\nEvent: {event}")
            try:
                fsm.trigger(event)
            except ValueError as e:
                print(f"Error: {e}")
            print(f"Current State: {fsm.get_state()}")
    except Exception as e:
        print(f"Failed to start FSM: {e}")