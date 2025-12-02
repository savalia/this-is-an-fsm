# tests/test_integration_fsm.py
import unittest
from loader import load_fsm_from_json

class TestFiniteStateMachineIntegration(unittest.TestCase):
    def setUp(self):
        self.config_path = "fsm_config.json"

    def test_start_from_default(self):
        fsm, _ = load_fsm_from_json(self.config_path)
        self.assertEqual(fsm.get_state(), "Idle")

    def test_start_from_alternate_initial(self):
        fsm, _ = load_fsm_from_json(self.config_path, start_state_name="Processing")
        self.assertEqual(fsm.get_state(), "Processing")

    def test_invalid_start_state_raises_error(self):
        with self.assertRaises(ValueError):
            load_fsm_from_json(self.config_path, start_state_name="NonExistent")

    def test_full_cycle_from_idle(self):
        fsm, _ = load_fsm_from_json(self.config_path)
        fsm.trigger("start")
        self.assertEqual(fsm.get_state(), "Starting")
        fsm.trigger("ready")
        self.assertEqual(fsm.get_state(), "Waiting")
        fsm.trigger("process")
        self.assertEqual(fsm.get_state(), "Processing")
        fsm.trigger("monitor")
        self.assertEqual(fsm.get_state(), "Monitoring")
        fsm.trigger("stop")
        self.assertEqual(fsm.get_state(), "Stopping")
        fsm.trigger("reset")
        self.assertEqual(fsm.get_state(), "Idle")

    def test_invalid_event_goes_to_unknown(self):
        fsm, _ = load_fsm_from_json(self.config_path)
        fsm.trigger("invalid")
        self.assertEqual(fsm.get_state(), "Unknown")

    def test_recovery_from_unknown(self):
        fsm, _ = load_fsm_from_json(self.config_path)
        fsm.trigger("invalid")
        fsm.trigger("reset")
        self.assertEqual(fsm.get_state(), "Idle")

if __name__ == "__main__":
    unittest.main()