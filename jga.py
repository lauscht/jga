from good_guys import alex
from cool_girls import carina
from the_life import marriage, jga_test

carina.perform_live_experiments()
while not alex.has_well_observed():
    carina.perform_live_experiments()

(sharish, milk, porto, fourty_two, pfeffi) = \
 alex.get_position_of_drinks_by_color_ordering()

def alex_performs_magic():
    result = sharish * 1000
    result += milk * 400
    result += fourty_two * pfeffi
    result += porto
    return result

with (alex and carina) as married_couple:
    hint = alex_performs_magic() % marriage.date
    if not jga_test(hint):
        exit()

