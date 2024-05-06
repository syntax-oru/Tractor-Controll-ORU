try:
    import utime as time
except ImportError:
    import time as time
from math import pi

class Motor:
    """
    Interface for a motor object.

    Attributes:
        speed (float): The speed of the motor in radians per second.
        position (float): The current position of the motor in radians.
        enabled (bool): True if the motor is enabled, False otherwise.
    """

    def __init__(self) -> None:
        ...

    @property
    def speed(self) -> float:
        """
        The speed of the motor in radians per second.
        """
        ...

    @speed.setter
    def speed(self, value: float) -> None:
        ...

    @property
    def position(self) -> float:
        """
        The current position of the motor in radians.
        """
        ...

    @position.setter
    def position(self, value: float) -> None:
        ...

    def start(self) -> None:
        """
        Starts the motor.

        Enables motor.

        Parameters:
            None

        Returns:
            None
        """
        ...

    def stop(self) -> None:
        """
        Stops the motor.

        Sets speed to 0 and disables motor.

        Parameters:
            None

        Returns:
            None
        """
        ...

    @property
    def enabled(self) -> bool:
        """
        Check if the motor is enabled.

        Returns:
            bool: True if the motor is enabled, False otherwise.
        """
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...

class IdealSimulatedMotor(Motor):
    """
    IdealSimulatedMotor is a simulated motor that behaves ideally.\n
    Without friction and without acceleration.
    """

    def __init__(self) -> None:
        self._speed: float = 0.0
        self._position: float = 0.0
        self._on: bool = False
        self._previous_time: float = time.time()

    def _update_position(self) -> None:
        current_time = time.time()
        elapsed_time = current_time - self._previous_time
        self._position += (self._speed * elapsed_time) % (2 * pi)
        self._previous_time = current_time

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        self._update_position()
        self._speed = value

    @property
    def position(self) -> float:
        self._update_position()
        return self._position

    @position.setter
    def position(self, value: float) -> None:
        self._position = value

    @property
    def enabled(self) -> bool:
        return self._on

    @enabled.setter
    def enabled(self, value: bool) -> None:
        if value is True:
            self.start()
        else:
            self.stop()

    def start(self) -> None:
        self._on = True

    def stop(self) -> None:
        self._on = False
        self.speed = 0.0