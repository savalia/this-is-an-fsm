# Unit tests for the examples using unittest framework
import unittest

from loader import load_fsm_from_json
# Import example run functions (examples package required)
from examples import starting, waiting, processing, monitoring, stopping

class TestExamplesAndStartStates(unittest.TestCase):
    def setUp(self):
        self.config_path = "fsm_config.json"

    def test_starting_example_transitions_to_waiting(self):
        result = starting.run()
        self.assertEqual(result, "Waiting")

    def test_waiting_example_transitions_to_processing(self):
        result = waiting.run()
        self.assertEqual(result, "Processing")

    def test_processing_example_transitions_to_monitoring(self):
        result = processing.run()
        self.assertEqual(result, "Monitoring")

    def test_monitoring_example_transitions_to_stopping(self):
        result = monitoring.run()
        self.assertEqual(result, "Stopping")

    def test_stopping_example_transitions_to_idle(self):
        result = stopping.run()
        self.assertEqual(result, "Idle")

    def test_idle_start_state_default(self):
        # Ensure FSM starts at Idle by default
        fsm, _ = load_fsm_from_json(self.config_path)
        self.assertEqual(fsm.get_state(), "Idle")

    def test_unknown_start_state_recovery(self):
        # If FSM starts in Unknown, triggering 'reset' should move to Idle
        fsm, _ = load_fsm_from_json(self.config_path, start_state_name="Unknown")
        fsm.trigger("reset")
        self.assertEqual(fsm.get_state(), "Idle")


if __name__ == "__main__":
    unittest.main()