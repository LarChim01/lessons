import unittest
import runner_test
import TournamentTest

testRunTour = unittest.TestSuite()
testRunTour.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
testRunTour.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(testRunTour)


