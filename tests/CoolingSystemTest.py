import unittest
from CoolingSystemObserverHelper import CoolingSystemObserverHelper
from TypeACoolingSystem import TypeACoolingSystem
from TypeBCoolingSystem import TypeBCoolingSystem
from TypeCCoolingSystem import TypeCCoolingSystem
from ICoolingSystem import ICoolingSystem


class BaseTestCases:

    class CoolingSystem(unittest.TestCase):

        def setUp(self):
            self.room_cs_observer = CoolingSystemObserverHelper()
            self.room_cs.attach(self.room_cs_observer)
            self.room_cs.start()

        def tearDown(self):
            self.room_cs.stop()

        def test_auto_turn_off_event(self):
            # Prepare
            desired_room_temperature = 22
            self.room_cs._current_room_temperature = 24
            self.room_cs.set_desired_room_temperature(desired_room_temperature)
            # Action
            self.room_cs.turn_on()
            # Results
            events = self.room_cs_observer.wait_for_events("AUTO_TURN_OFF", 10)
            self.assertIn("AUTO_TURN_OFF", events)

        def test_set_desired_temperature(self):
            # Prepare
            desired_room_temperature = 22
            self.room_cs._current_room_temperature = 24
            self.room_cs.set_desired_room_temperature(desired_room_temperature)
            # Action
            self.room_cs.turn_on()
            # Results
            event = self.room_cs_observer.wait_for_one_event("AUTO_TURN_OFF", 10)
            self.assertEqual(desired_room_temperature, event["current_room_temperature"])


class TypeACoolingSystemTest(BaseTestCases.CoolingSystem):
    def setUp(self):
        self.room_cs = TypeACoolingSystem("room_1")
        super().setUp()


class TypeBCoolingSystemTest(BaseTestCases.CoolingSystem):
    def setUp(self):
        self.room_cs = TypeBCoolingSystem("room_2")
        super().setUp()


class TypeCCoolingSystemTest(BaseTestCases.CoolingSystem):
    def setUp(self):
        self.room_cs = TypeCCoolingSystem("room_3")
        super().setUp()


if __name__ == '__main__':
    unittest.main()
