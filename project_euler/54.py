
from collections import defaultdict

val2int = {
    **{ str(i): i for i in range(2, 10) },
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

def _get_rank(values, suits):
    counts = defaultdict(list)
    for val in set(values):
        counts[values.count(val)].append(val)
        
    if len(set(suits)) == 1:
        if min(values) == 10:
            return 10, 0  # royal flush
        if max(values) - min(values) == 4:
            return 9, max(values)  # straight flush
    if len(set(values)) == 2:
        if 4 in counts:
            return 8, counts[4][0]  # four of a kind
        if set(counts) == set([3, 2]):
            return 7, counts[3][0] * 15 + counts[2][0]  # full house
    if len(set(suits)) == 1:
        return 6, max(values)  # flush
    if len(set(values)) == 5 and max(values) - min(values) == 4:
        return 5, max(values)  # straight
    if 3 in counts:
        return 4, counts[3][0]  # three of a kind
    if 2 in counts:
        if len(counts[2]) == 2:
            return 3, max(counts[2]) * 15 + min(counts[2])  # two pairs
        if len(counts[2]) == 1:
            return 2, counts[2][0]  # one pair
    return 1, max(values)  # high card

def get_hand_rank(hand):
    # input: list of (strings of size 2)
    # output: rank of the hand, and value of the hand to be used in case of a tie
    #         plus values of all cards, ordered, to be used in lexicographical order
    values = [val2int[card[0]] for card in hand]
    suits = [card[1] for card in hand]
    rank = _get_rank(values, suits)
    return [*rank] + sorted(values)[::-1]

def get_winner(hand):
    hand1 = hand.split()[:5]
    hand2 = hand.split()[5:]
    rank1 = get_hand_rank(hand1)
    rank2 = get_hand_rank(hand2)
    return 1 if rank1 > rank2 else 2

example_hands = [
    '5H 5C 6S 7S KD 2C 3S 8S 8D TD',
    '5D 8C 9S JS AC 2C 5C 7D 8S QH',
    '2D 9C AS AH AC 3D 6D 7D TD QD',
    '4D 6S 9H QH QC 3D 6D 7H QD QS',
    '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D',
]

for hand in example_hands:
    print(f'Player {get_winner(hand)} wins')

with open('54_poker.txt', 'r') as fp:
    hands = fp.read()
    hands = hands.split('\n')[:-1]
    winners = list(map(get_winner, hands))
    print(winners.count(1))
