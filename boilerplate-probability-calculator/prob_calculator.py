import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, amount_to_draw):
        if amount_to_draw > len(self.contents):
            return self.contents

        drawn_balls = random.sample(self.contents, amount_to_draw)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0

    for _ in range(num_experiments):
        hat_to_experiment = copy.deepcopy(hat)
        drawn_balls = hat_to_experiment.draw(num_balls_drawn)
        success = all(
            drawn_balls.count(color) >= count for color, count in expected_balls.items()
        )
        if success:
            successful_draws += 1
    return successful_draws / num_experiments
