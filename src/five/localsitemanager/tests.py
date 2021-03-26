import unittest

from Testing.ZopeTestCase import FunctionalDocFileSuite
from Testing.ZopeTestCase import ZopeDocFileSuite


def test_suite():
    return unittest.TestSuite([
        ZopeDocFileSuite('localsitemanager.txt',
                         package="five.localsitemanager"),
        FunctionalDocFileSuite('browser.txt',
                               package="five.localsitemanager")
    ])


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
