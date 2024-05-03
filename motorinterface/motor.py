try:
    from utime import time
except ImportError:
    from time import time
from math import pi


class Motor:
    def __init__(self) -> None:
        ...

    @property
    def speed(self) -> float:
        ...

    @speed.setter
    def speed(self, value: float) -> None:
        ...

    @property
    def position(self) -> float:
        ...

    @position.setter
    def position(self, value: float) -> None:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

    @property
    def enabled(self) -> bool:
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...


class IdealSimulatedMotor(Motor):
    def __init__(self) -> None:
        self._speed = 0.0
        self._position = 0.0
        self._on = False
        self._previous_time = time()

    def _update_position(self) -> None:
        current_time = time()
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
