class InputManager:
    # Generic input manager that handles debouncing and state tracking.
    # Call getInput(key) to see if the key was *pressed this frame*.

    def __init__(self):
        # key states stored as: 0 = idle; 1 = pressed this tick; 2 = held
        self.states = {
            'green': 0,
            'red': 0,
            'left': 0,
            'right': 0
        }

    def _updateState(self, key, is_pressed):
        # Internal state machine:

        # 0 + press   → 1
        # 1 next tick → 2
        # 2 + release → 0

        # Return True ONLY on state == 1 (just pressed)

        state = self.states[key]

        # Transition from 1 → 2 automatically
        if state == 1:
            self.states[key] = 2

        # Handle press
        if is_pressed:
            if state == 0:
                self.states[key] = 1   # just pressed
                return True            # return True for this frame only
        else:
            # Handle release
            if state == 2:
                self.states[key] = 0

        return False  # not a new press this frame

    def getInput(self, keyname):
        # Pass keyname as a string:
        # - 'green'
        # - 'red'
        # - 'left'
        # - 'right'

        if keyname == 'green':
            is_pressed = force_sensor.force(port.A) >= 50
        elif keyname == 'red':
            is_pressed = force_sensor.force(port.B) >= 50
        elif keyname == 'left':
            is_pressed = button.pressed(button.LEFT)
        elif keyname == 'right':
            is_pressed = button.pressed(button.RIGHT)
        else:
            raise ValueError('Invalid key name for getInput()')

        return self._updateState(keyname, is_pressed)
