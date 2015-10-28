import unittest

from megaawesome.core import MegaAwesome


class test_timetravel(unittest.TestCase):

    def runTest(self):
        ma = MegaAwesome()
        self.assertTrue(ma.time_travel())
