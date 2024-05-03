import unittest
from motorinterface.motor import IdealSimulatedMotor


class TestMotor(unittest.TestCase):

    def test_speed(self):
        motor = IdealSimulatedMotor()
        motor.speed = 1.0
        assert motor.speed == 1.0

    def test_position(self):
        motor = IdealSimulatedMotor()
        motor.position = 1.0
        assert motor.position == 1.0

    def test_enabled(self):
        motor = IdealSimulatedMotor()
        motor.enabled = True
        assert motor.enabled == True

    def test_start(self):
        motor = IdealSimulatedMotor()
        motor.start()
        assert motor.enabled == True

    def test_stop(self):
        motor = IdealSimulatedMotor()
        motor.stop()
        assert motor.enabled == False


def main():
    unittest.main()


if __name__ == '__main__':
    main()
