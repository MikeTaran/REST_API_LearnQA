class TestExample:
    def test_check(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "The length of the inputted phrase is more than 15 symbols"
