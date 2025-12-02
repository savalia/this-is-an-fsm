# ==== test.py ====
# Unit tests for the FSM using unittest framework

import unittest
from loader import load_fsm_from_json  # Import the loader function from your FSM code

class TestFiniteStateMachineMultipleInitials(unittest.TestCase):
    def setUp(self):
        # Path to your FSM JSON configuration file
        self.config_path = "fsm_config.json"

    def test_start_from_default(self):
        """Test FSM starts from the default initial state."""
        fsm, _ = load_fsm_from_json(self.config_path)
        self.assertEqual(fsm.get_state(), "Idle")

    def test_start_from_processing(self):
        """Test FSM starts from a specified alternate initial state."""
        fsm, _ = load_fsm_from_json(self.config_path, start_state_name="Processing")
        self.assertEqual(fsm.get_state(), "Processing")

    def test_invalid_start_state_raises_error(self):
        """Test that an invalid start state raises a ValueError."""
        with self.assertRaises(ValueError):
            load_fsm_from_json(self.config_path, start_state_name="NonExistent")

    def test_valid_cycle_from_idle(self):
        """Test a complete valid cycle starting from Idle."""
        fsm, _ = load_fsm_from_json(self.config_path)
        fsm.trigger("start")
        self.assertEqual(fsm.get_state(), "Starting")
        fsm.trigger("ready")
        self.assertEqual(fsm.get_state(), "Waiting")
        fsm.trigger("process")
        self.assertEqual(fsm.get_state(), "Processing")
        fsm.trigger("stop")
        self.assertEqual(fsm.get_state(), "Stopping")
        fsm.trigger("reset")
        self.assertEqual(fsm.get_state(), "Idle")

    def test_invalid_event_goes_to_unknown(self):
        """Test that an invalid event sends FSM to Unknown state."""
        fsm, _ = load_fsm_from_json(self.config_path)
        fsm.trigger("invalid")
        self.assertEqual(fsm.get_state(), "Unknown")

    def test_recovery_from_unknown(self):
        """Test that FSM recovers from Unknown state with reset."""
        fsm, _ = load_fsm_from_json(self.config_path)
        fsm.trigger("invalid")
        fsm.trigger("reset")
        self.assertEqual(fsm.get_state(), "Idle")

    def test_empty_event_raises_error(self):
        """Test that an empty event string raises ValueError."""
        fsm, _ = load_fsm_from_json(self.config_path)
        with self.assertRaises(ValueError):
            fsm.trigger("")

    def test_non_string_event_raises_error(self):
        """Test that a non-string event raises ValueError."""
        fsm, _ = load_fsm_from_json(self.config_path)
        with self.assertRaises(ValueError):
            fsm.trigger(123)

if __name__ == "__main__":
    unittest.main()