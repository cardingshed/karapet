import random
from redeal import *
from redeal import dds
from redeal.global_defs import Seat, Suit, Card, Rank, Strain

# This is a human readable example to demonstrate the use of deal and dds
# The deal is a 'success' if the contract cannot be beaten on perfect defence.
# The random seed is set to enable reproduction of the observed value 0.484
# my article from which this example is taken.  Change this seed value to rerun
# the sim with different outcomes.

random.seed(1)
predeal = {Seat['N']: H('AK9 QJT98 QJT 32'), Seat['S']: H('QJT AK765 AK9 K4')}
dealer = Deal.prepare(predeal)

success = 0
i = 0
for i in range(1000):
    sim = dealer()
    if (sim.dd_tricks("6HS")>= 12):
        success += 1
        i += 1
    else:
        i += 1
print(success/1000)
