#!/usr/bin/python

import card_set
import random
import time
import sys

plus_one =  [ '2', '3', '4', '5', '6' ]
minus_one = [ '10', 'J', 'Q', 'K', 'A' ]

class Trainer(object):

    def __init__(self, secs_to_wait, stop_percentage):
        self.deck = card_set.Deck(6)
        self.count = 0
        self.secs_to_wait = secs_to_wait
        self.stop_percentage = stop_percentage

    def go(self):
        while len(self.deck.card_list) > 0:
            card = self.deck.deal()
            if card.value in plus_one:
                self.count += 1
            elif card.value in minus_one:
                self.count -= 1
            print 'Card: %s Decks left: %s' % (card, len(self.deck.card_list) /
                                              52.0)
            if self.secs_to_wait:
                if random.random() < self.stop_percentage:
                    return
                time.sleep(self.secs_to_wait)
            else:
                user = raw_input('? ')
                if user == 'c':
                    print 'Count: ' + str(self.count)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) == 3:
        delay = float(argv[1])
        stop_percentage = float(argv[2])
    else:
        delay = None
        stop_percentage = 0

    t = Trainer(delay, stop_percentage)

    try:
        while len(t.deck.card_list):
            t.go()
            my_count = raw_input("Count? ")
            if int(my_count) == t.count:
                print 'Right, it was ' + str(my_count)
            else:
                print 'Wrong, it was ' + str(t.count)

    except KeyboardInterrupt:
        pass
    finally:
        print '\nCount so far was: ' + str(t.count)

if __name__ == '__main__':
    main()
