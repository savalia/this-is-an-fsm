# tests/test_unit_fsm.py
import unittest
from state import State
from fsm import FiniteStateMachine

class TestFiniteStateMachineUnit(unittest.TestCase):
    def setUp(self):
        # Create dummy states for unit testing
        self.idle = State("Idle")
        self.processing = State("Processing")
        self.unknown = State("Unknown")

        # Define transitions
        self.idle.add_transition("process", self.processing)
        self.processing.add_transition("reset", self.idle)
        self.unknown.add_transition("reset", self.idle)

        # Create FSM
        self.fsm = FiniteStateMachine(self.idle, self.unknown)

    def test_initial_state(self):
        self.assertEqual(self.fsm.get_state(), "Idle")

    def test_valid_transition(self):
        self.fsm.trigger("process")
        self.assertEqual(self.fsm.get_state(), "Processing")

    def test_invalid_transition_goes_to_unknown(self):
        self.fsm.trigger("invalid")
        self.assertEqual(self.fsm.get_state(), "Unknown")

    def test_recovery_from_unknown(self):
        self.fsm.trigger("invalid")
        self.fsm.trigger("reset")
        self.assertEqual(self.fsm.get_state(), "Idle")

    def test_empty_event_raises_error(self):
        with self.assertRaises(ValueError):
            self.fsm.trigger("")

    def test_non_string_event_raises_error(self):
        with self.assertRaises(ValueError):
            self.fsm.trigger(123)

if __name__ == "__main__":
    unittest.main()