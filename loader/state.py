# state.py
# ==== FSM Implementation with Multiple Initial States Support and Embedded Code Review Comments ====
import json
import unittest

class State:
    def __init__(self, name, on_enter=None, on_exit=None):
        # Code review comment -> Added validation to ensure state name is a non-empty string.
        if not isinstance(name, str) or not name.strip():
            raise ValueError("State name must be a non-empty string.")
        self.name = name
        self.on_enter = on_enter
        self.on_exit = on_exit
        self.transitions = {}  # Code review comment -> Dictionary to store event-to-next_state mapping.

    def add_transition(self, event, next_state):
        # Code review comment -> Added validation for event name and next_state type.
        if not isinstance(event, str) or not event.strip():
            raise ValueError("Event name must be a non-empty string.")
        if not isinstance(next_state, State):
            raise TypeError("next_state must be a State instance.")
        self.transitions[event] = next_state

    def get_next_state(self, event):
        # Code review comment -> Returns None if event not found, which is handled in FSM trigger method.
        return self.transitions.get(event)

    def enter(self):
        # Code review comment -> Executes on_enter callback if callable.
        if callable(self.on_enter):
            self.on_enter(self)

    def exit(self):
        # Code review comment -> Executes on_exit callback if callable.
        if callable(self.on_exit):
            self.on_exit(self)