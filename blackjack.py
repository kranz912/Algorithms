import itertools


def create_deck():
    ranks = [str(x) for x in range(2,11)]
    ranks.append('K')
    ranks.append('Q')
    ranks.append('J')
    ranks.append('A')

    kinds = ['S','H','C','D']
    cards = dict()
    for k in kinds:
        for rank in ranks:
            if rank.isnumeric():
                cards[k+str(rank)]=int(rank)
            elif rank == 'Q' or rank == 'K' or rank == 'J':
                cards[k+str(rank)]=10
            else:
                cards[k+str(rank)]=11
    return cards


deck = create_deck()
#print(deck)
two_cardcombination = list(itertools.combinations(deck.keys(),2))
sum_21 =  []
sum_10 = []
for x in two_cardcombination:

    sum= deck[x[0]]+ deck[x[1]]
    if sum== 21:
        sum_21.append(x)
    if sum==10:
        sum_10.append(x)
print(len(sum_21)/len(two_cardcombination))

print(sum_10)
print(len(sum_10))

del deck['C10']
del deck['H4']
print(len(deck))
new_deck= []
for card in deck:
    if(deck[card]+14>21):
        new_deck.append(deck[card])
print(len(new_deck))
