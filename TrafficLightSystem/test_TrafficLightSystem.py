import unittest, time
from unittest.mock import patch
import unittest.mock
from threading import Thread, Event
from TrafficLightSystem import *

@patch('builtins.print')
class TestTrafficLight(unittest.TestCase):

    def test_tarffic_light(self, mock_print):

        trafficLight = TrafficLight()
        trafficLight.cycle = 1
        trafficLight.start1()

        excepted_calls = [
            unittest.mock.call("GO AHEAD"),
            unittest.mock.call("GO AHEAD"),
            unittest.mock.call("GO AHEAD"),
            unittest.mock.call("GO AHEAD"),
            unittest.mock.call("GO AHEAD"),

            unittest.mock.call("STOP"),
        ]


        mock_print.assert_has_calls(excepted_calls, any_order=False)


if __name__ == "__main__":
    unittest.main()
