
class BestScore:

    def __init__(self):
        self.read_best_score()


    def read_best_score(self):
        with open(file="./best_score.csv", mode="r") as file:
            score = file.readlines()
        return score


    def write_best_score(self, best_score):
        with open(file="./best_score.csv", mode="w") as file:
            file.write(f"bestscore \n {best_score}")
