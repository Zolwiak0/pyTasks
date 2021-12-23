from unittest import TestLoader, TestSuite, TextTestRunner
from tests.Scripts.test_LoginPage import test_LoginPage
from tests.Scripts.test_NewTask import test_NewTask

if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(test_LoginPage),
        test_loader.loadTestsFromTestCase(test_NewTask),

    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)