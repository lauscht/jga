from the_life import life, Life

class Alex(Life):
    opaque = 1
    white = 2
    red = 3
    yellow = 4
    green = 5

    _ = opaque * 10**3
    _ += white *4* 10**2
    _ += red
    _ += yellow*green

    print(_)

    def has_well_observed(self):
        return True

    def __and__(self, other):
        return life

    def get_position_of_drinks_by_color_ordering(self):
        return self.opaque, self.white, self.red, self.yellow, self.green

alex = Alex()

