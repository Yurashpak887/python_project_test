import itertools
import random
import shelve
import pickle
shuf = False


class CardDeck:
    rank_32 = [7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    rank_52 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['\u2660',
             '\u2665',
             '\u2666',
             '\u2663']



    def creating_deck(self):
        self.cards = list(itertools.product(CardDeck.rank_36, CardDeck.suits))
        return self.cards


    def __repr__(self):

        return self.cards

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards


    def __getitem__(self, index):
        if isinstance(index, int):
            try:
                return self.cards[index]
            except IndexError:
                raise IndexError("enter a valid number")

    def __add__(self, other_card):
        for i in CardDeck().rank_52:
            if i == other_card:
                print("Ok's")
                random_suits = random.choice(CardDeck().suits)
                print(random_suits)
                c = []
                c.append(other_card)
                c.append(random_suits)

        print(c)

        if c in self.cards:
            print("No!")
        else:
            self.cards = self.cards + c


    def __sub__(self, del_cards):
        for card in del_cards:
            print(card)
            self.cards.remove(card)

    def __contains__(self, card):
        return card in self.cards

    def __eq__(self, card):
        if isinstance(card, CardDeck):
            return self.cards == card.cards
        return NotImplemented

    def __bool__(self):
        if shuf is True and bool(self.cards):
            return True
        else:
            return False

    def save(self, name):
        f = shelve.open('filename')
        f[name] = self.cards
        f.close()

    def load(self, deck_name):
        file = shelve.open('filename')
        print(file[deck_name])

    def picle_save(self, name_of_class):
        with open('data.pickle', 'wb') as f:
            pickle.dump(name_of_class, f)

    def picle_open(self):
        with open('data.pickle', 'rb') as f:
            data_new = pickle.load(f)
            print(data_new.__repr__())


class SmallDeck(CardDeck):
    def __init__(self):
        self.cards = list(itertools.product(CardDeck.rank_32, CardDeck.suits))

class ClassicDeck(CardDeck):
    def __init__(self):
        self.cards = list(itertools.product(CardDeck.rank_52, CardDeck.suits))



a = ClassicDeck()

print(a.save("Nn"))
print(a.load("Nn"))

with open('data.pickle', 'wb') as f:
    pickle.dump(a, f)

with open('data.pickle', 'rb') as f:
    data_new = pickle.load(f)
    print(data_new.__repr__())