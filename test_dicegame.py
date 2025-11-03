# test_dicegame.py
# Unit tests for DiceGame assignment

import unittest
from main import Die, DiceGame

#This class test if the Die class is created correctly.
#It basically checks if the die returns a legit number. For example, a six face die 
#should not give you a number outside 1-6.
class TestDie(unittest.TestCase):
    def test_roll_within_bounds(self):
	#create a Die object with 6 sides
        die = Die(sides=6)

        #this will repeat the test 100 times
        for _ in range(100):
            #roll the Die and get the number facing up
            roll = die.roll()
            #check if the number is from 1 to 6. assertIn checkes if the number
            #is contained in the range of 1 to 6.
            self.assertIn(roll, range(1, 7))

#This class test the the dice gaming logic.
class TestDiceGame(unittest.TestCase):
    #Create a DiceGame object
    def setUp(self):
        self.game = DiceGame()

    #This will test if the logic in evaluate_roll() to determine a Win is correct.
    #You get a Win when total is 7 or 11.
    def test_evaluate_win(self):
        #Check if total is 7 or 11, evaluate_roll() will return "Win"
	#assertEqual() checks if evaluate_roll() return "Win"
        for total in [7, 11]:
            self.assertEqual(self.game.evaluate_roll(total), "Win")

    #This will test if the logic in evaluate_roll() to determine a Lose is correct.
    def test_evaluate_lose(self):
	#Check if total is 7 or 11, evaluate_roll() will return "Lose"
        #assertEqual() checks if evaluate_roll() return "Lose"
        for total in [2, 3, 12]:
            self.assertEqual(self.game.evaluate_roll(total), "Lose")

    #This will test if the logic in evaluate_roll() to determine a Roll Again is correct.
    def test_evaluate_roll_again(self):
	#Check if total is 4, 5, 6, 8, 9 or 10, evaluate_roll() will return "Roll Again"
        #assertEqual() checks if evaluate_roll() returns "Roll Again"
        for total in [4, 5, 6, 8, 9, 10]:
            self.assertEqual(self.game.evaluate_roll(total), "Roll Again")

       
    #This tests if Die object is created without specifying number of sides, the default number of side is 6.
    def test_die_default_sides(self):
        die = Die()
        self.assertEqual(die.sides, 6)

    #This tests if play_round() return 4 values of proper data type. play_round() return 4 varaibles  
    #roll1, roll2, total, result which are of type int, int, int, str
    def test_play_round_output_structure(self):
        result = self.game.play_round()
        #test if 4 values returned
        self.assertEqual(len(result), 4)
        #test first return value is of int --- roll1
        self.assertIsInstance(result[0], int)
        #test second return value is of int --- roll2
        self.assertIsInstance(result[1], int)
        #test third return value is of int --- total
        self.assertIsInstance(result[2], int)
        #test fourth return value is of type string --- result
        self.assertIsInstance(result[3], str)
    
    #This tests if two rolls are independently generating random numbers.
    #This will catch errors such as one die always return a unique number.
    def test_two_dice_independent(self):
        roll1_list = []
        roll2_list = []

	#try 50 games
        for _ in range(50):
            roll1, roll2, _, _ = self.game.play_round()
	    #This saves all the numbers returned by each die.
            roll1_list.append(roll1)
            roll2_list.append(roll2)
        #Test if unique return numbers from each die are more than 1
        #Less likely for 50 trials you always get one same number. If so, likely somewhere there is a bug.
        self.assertGreater(len(set(roll1_list)), 1)
        self.assertGreater(len(set(roll2_list)), 1)

    # --- Students: Add 3 more test cases below ---


class TestMoreDiceGame(unittest.TestCase):
    def setUp(self):
        self.game = DiceGame()

    def test_play_round_total_matches_sum(self):
        r1, r2, total, _ = self.game.play_round()
        self.assertEqual(total, r1 + r2)

    def test_custom_die_sides_bounds(self):
        d10 = Die(sides=10)
        for _ in range(100):
            self.assertIn(d10.roll(), range(1, 11))

    def test_many_rounds_results_valid(self):
        allowed = {"Win", "Lose", "Roll Again"}
        for _ in range(100):
            r1, r2, total, result = self.game.play_round()
            self.assertIn(total, range(2, 13))
            self.assertIn(result, allowed)

if __name__ == '__main__':
    unittest.main()
