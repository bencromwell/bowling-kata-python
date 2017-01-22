from array import array


class Game(object):

    def __init__(self):
        self.rolls = array('i')

    def roll(self, pins):
        self.rolls.append(pins)

    @property
    def score(self):
        total = 0
        frame_index = 0

        for frame in range(0, 10):
            if self.is_strike(frame_index):
                total += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                total += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                total += self.sum_of_balls_in_frame(frame_index)
                frame_index += 2

        return total

    def sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self.sum_of_balls_in_frame(frame_index) == 10

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]
