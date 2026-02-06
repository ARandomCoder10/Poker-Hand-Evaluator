#Poker Hand Evaluator
#
# 1      ROYAL FLUSH  |  10,   J,    Q,    K,    A   |  SAME SUIT
# 2   STRAIGHT FLUSH  |   x,  x+1,  x+2,  x+3,  x+4  |  SAME SUIT
# 3   FOUR OF A KIND  |   x,   x,    x,    x,    -   |  DIFF. SUITS
# 4       FULL HOUSE  |   x,   x,    x,    y,    y   |  DIFF. SUITS
# 5            FLUSH  |   -,   -,    -,    -,    -   |  SAME SUIT
# 6         STRAIGHT  |   x,  x+1,  x+2,  x+3,  x+4  |  DIFF. SUITS
# 7  THREE OF A KIND  |   x,   x,    x,    -,    -   |  DIFF. SUITS
# 8         TWO PAIR  |   x,   x,    y,    y,    -   |  DIFF. SUITS
# 9             PAIR  |   x,   x,    -,    -,    -   |  DIFF. SUITS
# 10       HIGH CARD  |   x,   -,    -,    -,    -   |  DIFF. SUITS

# ╗═║╔╝╚
# ♣♠♥♦
# ╔═════╗
# ║ 1 0 ║
# ║  ♣  ║
# ╚═════╝

def main():
    from os import name, system
    from contextlib import suppress

    def clear():
        # cls for Windows, clear for Unix/Mac/Linux
        system('cls' if name == 'nt' else 'clear')

    def title_display():
        print('''╔═════ TEXAS HOLD'EM ═══════════════════╗
║| ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ |║
║|   ___   ___   _     ____  ___    ╔════════ ♦
║|  | |_) / / \ | |_/ | |_  | |_)   ║ HAND    
║|  |_|   \_\_/ |_| \ |_|__ |_| \   ║ CHECKER ║
║|     ----                         ╚═════════╝
║| ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ |║
╚═══════════════════════════════════════╝
''')

    def key():
        print('''╔═══
║ INPUT KEY
║ ----
║ RANKS ║ J, Q, K & A for each of the special ranks
║ SUITS ║ C: ♣ | S: ♠ | H: ♥ | D: ♦
║ EXIT  ║ X at any time to restart''')

    def pres_check(prompt):
        a = ''
        while not a:
            with suppress(KeyboardInterrupt):
                a = input(f'{prompt}: ')
        return a

    def pic_ranks(rank):
        match rank:
            case 11:
                rank = 'J'
            case 12:
                rank = 'Q'
            case 13:
                rank = 'K'
            case 14:
                rank = 'A'
            case _:
                rank = str(rank)
        return rank

    def append_rank(ranks, rank):
        ranks[0].append(rank)
        if rank not in ranks[1]:
            ranks[1].append(rank)
            ranks[2].append(0)  # To count
        ranks[2][ranks[1].index(rank)] += 1
        return ranks

    def append_suit(suits, suit):
        suits[0].append(suit)
        if suit not in suits[1]:
            suits[1].append(suit)
            suits[2].append(0)  # To determine if flush-well
        suits[2][suits[1].index(suit)] += 1
        return suits

    while True:
        # 1 INPUTS
        ranks = [
            [], [], [], []
        ]  # [[all ranks], [present ranks], [how many of each rank], [rest of ranks]]
        suits = [
            [], [], [], []
        ]  # [[all suits], [present suits], [how many of each suit], [rest of suits]]

        # ♣♠♥♦
        lets, exit, no_of_cards, displayed = 'bcdefgh', False, 0, False
        flush_note = '''║ The program will now stop asking for suits as
║ the possibility of a flush has now disappeared.'''
        title_display()

        # For the four stages = Pre-Flop (2), Flop (3), Turn (1) & River (1)
        for stage in range(4):

            # 1.1 Entering the ranks & suits for each card
            set = '''║ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗
║ ║  b  ║ ║  c  ║ ║  d  ║ ║  e  ║ ║  f  ║ + g G
║ ║  B  ║ ║  C  ║ ║  D  ║ ║  E  ║ ║  F  ║ + h H
║ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝
║'''
            key()

            hand, best = '', False

            print('\n╔═══')
            match stage:
                case 0:
                    print('║ PRE-FLOP')
                    places = 2
                case 1:
                    print('║ FLOP')
                    places = 3
                case 2:
                    print('║ TURN')
                    places = 1
                case 3:
                    print('║ RIVER')
                    places = 1

            # For every card in each stage
            for i in range(places):
                no_of_cards += 1
                print('║ ----')  # Fo' show

                while True:
                    # 1.2.1 Ranks
                    while True:
                        no_flush = bool(suits[2]) and 8 - no_of_cards + max(suits[2]) < 5

                        if no_flush and not displayed:
                            print(f'║ NOTE\n{flush_note}\n║ ----')
                            displayed = True

                        rank, valid = pres_check('║ Rank').upper(), True
                        match rank:
                            case 'J':
                                rank = 11
                            case 'Q':
                                rank = 12
                            case 'K':
                                rank = 13
                            case 'A':
                                rank = 14  # 14 qualifies in end of Straight & High Card
                            case 'X':
                                exit = True
                                break
                            case _:
                                if rank.isnumeric():
                                    prompt = '║ ----\n║ INVALID\n║ advice\n║ (follow the above key for special ranks)\n║ ----'
                                    if int(rank) >= 2 and int(rank) <= 10:
                                        rank = int(rank)
                                    else:
                                        if (int(rank) >= 11 and int(rank) <= 14) or int(rank) == 1:
                                            prompt = prompt.replace('advice', 'You may have meant R for name.')
                                            if int(rank) == 1 or int(rank) == 14:
                                                single = 'A'
                                                word = 'Ace'
                                            else:
                                                match rank:
                                                    case '11':
                                                        single = 'J'
                                                        word = 'Jack'
                                                    case '12':
                                                        single = 'Q'
                                                        word = 'Queen'
                                                    case '13':
                                                        single = 'K'
                                                        word = 'King'
                                            prompt = prompt.replace('R', single)
                                            prompt = prompt.replace('name', word)
                                            print(prompt)
                                            valid = False
                                else:
                                    prompt = prompt.replace('advice', 'Please enter a proper rank.')
                                    print(prompt)
                                    valid = False

                        if valid:
                            if ranks[0].count(rank) == 4:
                                print(
                                    '║ ----\n║ INVALID\n║ This rank has already been entered 4 times.\n║ ----'
                                )
                            else:
                                assume_suit = ranks[0].count(rank) == 3
                                # If the suits of 3 cards of the same rank have been entered, the last one is assumed
                                break

                    if exit:
                        break

                    # 1.2.2 Suits
                    if not assume_suit and not no_flush:
                        # if the rest of cards to be entered can result in a flush, it's flush-valid

                        # 1.2.2 Suits
                        while True:
                            suit = pres_check('║ Suit').upper()
                            if suit not in ('C', 'S', 'H', 'D', 'X'):
                                print(
                                    '║ ----\n║ INVALID\n║ Please enter one of the above options.\n║ ----'
                                )
                            else:
                                break

                        match suit:
                            case 'C':
                                suit = '♣'
                            case 'S':
                                suit = '♠'
                            case 'H':
                                suit = '♥'
                            case 'D':
                                suit = '♦'
                            case 'X':
                                exit = True
                                break

                        # 1.2.3 Checking & adding the values
                        new = True
                        for i in range(len(ranks[0])):
                            if ranks[0][i] == rank and suits[0][i] == suit:
                                print(
                                    '║ ----\n║ INVALID\n║ This card has already been entered.\n║ ----'
                                )
                                new = False
                                break

                        if new:
                            ranks = append_rank(ranks, rank)
                            suits = append_suit(suits, suit)
                            break

                    else:

                        if assume_suit:
                            if stage != 3:
                                text = f'''║ ----
║ NOTE
║ Due to this rank being entered 4 times,
║ the final suit of this set has been processed.
{flush_note}'''

                                if i == places - 1:
                                    with suppress(KeyboardInterrupt):
                                        input(
                                            f'{text}\n║ ----\n║ Press ENTER to continue\n║ ----')
                                    # If at final place, will disappear before can be read
                                else:
                                    print(text)

                                displayed = True

                            ranks = append_rank(ranks, rank)

                            marker = ''  # To catch the already-entered suits...
                            count = 0
                            for i in range(len(ranks[0])):
                                if ranks[0][i] == rank:
                                    marker += suits[0][i]
                                    count += 1
                                    if count == 3:
                                        break

                            for suit in '♣♠♥♦':
                                if suit not in marker:  # ...to find the missing one
                                    suits = append_suit(suits, suit)

                            break

                        else:
                            ranks = append_rank(ranks, rank)
                            break

                if exit:
                    break

            if exit:
                clear()
                break

            # 2 Detection
            details, ranks[3], suits[3] = '', ranks[0][:], suits[0][:]

            if stage:

                # 2.1 Four of a Kind
                if 4 in ranks[2]:
                    hand, details, hand_cards = 'FOUR OF A KIND', ranks[1][
                        ranks[2].index(4)], 4

                    for let in lets[:4]:
                        # For the cards: ranks
                        set = set.replace(f' {let} ',
                                          '1 0') if details == 10 else set.replace(
                            let, pic_ranks(details))
                        # For the cards: suits
                        set = set.replace(let.upper(),
                                          suits[3][ranks[3].index(details)])
                        suits[3].pop(ranks[3].index(details))

                        # *Removed try-except because such thing already handled in validation

                        ranks[3].remove(details)

                # 2.2 Full House
                elif max(ranks[2]) == 3 and (2 in ranks[2]
                                             or ranks[2].count(3) == 2):
                    hand, hand_cards = 'FULL HOUSE', 5
                    threes, twos = [], []

                    for i, rank in enumerate(ranks[1]):
                        # 2.2.1.1 Threes
                        if ranks[2][i] == 3:
                            threes.append(rank)

                        # 2.2.1.2 Twos
                        elif ranks[2][i] == 2:
                            twos.append(rank)

                    # 2.2.2 Details
                    details = [max(threes)]

                    #              If there are two 3-of-a-kinds
                    details.append(min(threes) if not twos else
                                   max(twos))  # Get the last of the threes
                    details = tuple(details)

                    # For the cards: the first three
                    for let in lets[:3]:
                        # Ranks
                        set = set.replace(f' {let} ',
                                          '1 0') if details[0] == 10 else set.replace(
                            let, pic_ranks(details[0]))
                        # Suits
                        try:
                            set = set.replace(let.upper(),
                                              suits[3][ranks[3].index(details[0])])
                            suits[3].pop(ranks[3].index(details[0]))
                        except IndexError:
                            set = set.replace(let.upper(), '-')

                        # To eliminate for other cards
                        ranks[3].remove(details[0])

                    # For the cards: the last two
                    for let in lets[3:5]:

                        # Ranks
                        set = set.replace(f' {let} ',
                                          '1 0') if details[1] == 10 else set.replace(
                            let, pic_ranks(details[1]))
                        # Suits
                        try:
                            set = set.replace(let.upper(),
                                              suits[3][ranks[3].index(details[1])])
                            suits[3].pop(ranks[3].index(details[1]))  # Elimination

                        except IndexError:
                            set = set.replace(let.upper(), '-')

                        # To eliminate for kicker
                        ranks[3].remove(details[1])

                # 2.3 Flush
                elif max(suits[2]) >= 5:
                    hand, details, hand_cards = 'FLUSH', suits[1][suits[2].index(
                        max(suits[2]))], 5

                    # 2.4 Straight Flush & Royal Flush
                    suit_ranks = []

                    # Finding those with the flush suit
                    for i, suit in enumerate(suits[3]):
                        if suit == details:
                            suit_ranks.append(ranks[3][i])

                    suit_ranks.sort()  # -- Sorts
                    suit_ranks.reverse()  # into descending order
                    # -------------------- to find highest straight flush

                    # 2.4.0 The Ace Case
                    # Ace is special because if present & relevant to the hand, it can only result in two possibilities:

                    # checking for royal & straight flush where ace is needed
                    royal_check = suit_ranks[:5] == [14, 13, 12, 11, 10]
                    str_flu_check = suit_ranks[:2] == [14,
                                                       5] and 4 in suit_ranks and 3 in suit_ranks and 2 in suit_ranks

                    if 14 in suit_ranks and (royal_check or str_flu_check):
                        ranks[3], suits[3] = [], []

                        # ...a Royal Flush
                        if royal_check:
                            hand = f'ROYAL {hand}'
                            # For the cards
                            for i, let in enumerate(lets[:4]):
                                set = set.replace(let, pic_ranks(suit_ranks[:4][i]))
                                set = set.replace(let.upper(), details)
                            set = set.replace(' f ', '1 0')
                            set = set.replace('F', details)

                            for i, rank in enumerate(ranks[0]):
                                if not (suits[0][i] == details and rank in (14, 13, 12, 11, 10)):
                                    ranks[3].append(rank)
                                    suits[3].append(suits[0][i])

                            details = (14, details)

                        # ...or a 5-High Straight
                        elif str_flu_check:
                            hand = f'STRAIGHT {hand}'
                            print(hand)
                            for i, let in enumerate(lets[:5]):
                                set = set.replace(let, pic_ranks((5, 4, 3, 2, 14)[i]))
                                set = set.replace(let.upper(), details)

                            for i, rank in enumerate(ranks[0]):
                                if not (suits[0][i] == details and rank in (5, 4, 3, 2, 14)):
                                    ranks[3].append(rank)
                                    suits[3].append(suits[0][i])

                            details = (5, details)

                    else:

                        # To maximise efficiency, run through the least amount of ranks
                        for rank in suit_ranks[:len(suit_ranks) - 4]:
                            if rank - 1 in suit_ranks and rank - 2 in suit_ranks and rank - 3 in suit_ranks and rank - 4 in suit_ranks:

                                if rank == 14:
                                    hand = f'ROYAL {hand}'
                                    # For the cards
                                    for i, let in enumerate(lets[:4]):
                                        set = set.replace(let, pic_ranks(suit_ranks[:4][i]))
                                        set = set.replace(let.upper(), details)
                                    set = set.replace(' f ', '1 0')
                                    set = set.replace('F', details)

                                else:
                                    hand = f'STRAIGHT {hand}'

                                    # For the cards
                                    for i, let in enumerate(lets[:5]):
                                        # Ranks
                                        match rank - i:
                                            case 10:
                                                set = set.replace(f' {let} ', '1 0')
                                            case 1:
                                                set = set.replace(let, 'A')
                                            case _:
                                                set.replace(let, pic_ranks(rank - i))
                                        # Suits
                                        set = set.replace(let.upper(), details)

                                # To eliminate for other cards
                                for i, rank_1 in enumerate(ranks[0]):
                                    if not (suits[0][i] == details and (
                                            rank_1 in (rank, rank - 1, rank - 2, rank - 3, rank - 4) or (
                                            rank == 5 and rank_1 == 14))):
                                        ranks[3].append(rank_1)
                                        suits[3].append(suits[0][i])

                                details = (rank,
                                           details) if hand == 'STRAIGHT FLUSH' else details
                                break

                print(hand)
                # 2.3 Flush [continued]
                if hand == 'FLUSH':

                    # Finding the related flush ranks
                    flush_ranks = suit_ranks[:5]

                    # For the cards
                    for i, let in enumerate(lets[:5]):
                        set = set.replace(let.upper(), details)
                        set = set.replace(
                            f' {let} ', '1 0') if flush_ranks[i] == 10 else set.replace(
                            let, pic_ranks(flush_ranks[i]))
                        # Elimination
                        suits[3].pop(ranks[3].index(flush_ranks[i]))
                        # To find the exact suit space to make sure that all the cards are still accurate
                        ranks[3].remove(flush_ranks[i])

                    details = (flush_ranks[0], details)

                # 2.5 Straight
                elif not hand and len(ranks[1]) >= 5:

                    # 2.5.1 Sorting into descending order
                    sort_ranks = ranks[1][:]
                    sort_ranks.sort()  # ------ Sorts
                    sort_ranks.reverse()  # --- into descending order
                    # ------------------------- to find highest straight
                    if 14 in ranks[1]:
                        sort_ranks.append(1)  # For a 5-High Straight

                    # 2.5.2 Through each rank
                    for rank in sort_ranks[:len(sort_ranks) - 4]:
                        if rank - 1 in sort_ranks and rank - 2 in sort_ranks and rank - 3 in sort_ranks and rank - 4 in sort_ranks:
                            hand, details, hand_cards = 'STRAIGHT', rank, 5

                            # for the cards & elimination
                            for i, let in enumerate(lets[:5]):

                                # Ranks
                                match rank - i:
                                    case 10:
                                        set = set.replace(f' {let} ',
                                                          '1 0')
                                    case 1:
                                        set = set.replace(let, 'A')
                                    case _:
                                        set = set.replace(let, pic_ranks(rank - i))

                                # Suits
                                try:
                                    set = set.replace(let.upper(),
                                                      suits[3][ranks[3].index(14 if rank - i == 1 else rank - i)])
                                    suits[3].pop(ranks[3].index(rank - i))
                                except IndexError:
                                    set = set.replace(let.upper(), '-')
                                ranks[3].remove(rank - i)

                            break

            # 2.5 High Card, (Two) Pair, Three of a Kind
            if not hand:
                match max(ranks[2]):

                    # 2.5.1 Three of a Kind
                    case 3:
                        hand, details, hand_cards = 'THREE OF A KIND', ranks[1][
                            ranks[2].index(3)], 3

                        # Cards
                        for let in lets[:3]:
                            set = set.replace(f' {let} ',
                                              '1 0') if details == 10 else set.replace(
                                let, pic_ranks(details))
                            try:
                                set = set.replace(let.upper(),
                                                  suits[3][ranks[3].index(details)])
                                suits[3].pop(ranks[3].index(details))  # Elimination
                            except IndexError:
                                set = set.replace(let.upper(), '-')
                            ranks[3].remove(details)  # Elimination

                    # 2.5.2 Pair & Two Pair
                    case 2:
                        # 2.5.2.1 Pair
                        if ranks[2].count(2) == 1:
                            hand, details, hand_cards = 'PAIR', ranks[1][ranks[2].index(
                                2)], 2

                            for let in lets[:2]:
                                # Card ranks
                                set = set.replace(f' {let} ',
                                                  '1 0') if details == 10 else set.replace(
                                    let, pic_ranks(details))
                                # Card suits
                                try:
                                    set = set.replace(let.upper(),
                                                      suits[3][ranks[3].index(details)])
                                    suits[3].pop(ranks[3].index(details))  # Elimination
                                except IndexError:
                                    set = set.replace(let.upper(), '-')
                                ranks[3].remove(details)  # Elimination

                        # 2.5.2.2 Two/Three Pair
                        else:
                            hand, diff_ranks, hand_cards = 'TWO PAIR', ranks[1][:], 4
                            diff_ranks.sort()  # --- Sorted
                            diff_ranks.reverse()  # - in descending order
                            # ----------------------- to find highest pairs in the case of a Three Pair
                            for rank in diff_ranks:
                                if ranks[3].count(rank) == 2:
                                    if not details:
                                        details = [rank]

                                        # Cards: ranks
                                        for let in lets[:2]:
                                            set = set.replace(
                                                f' {let} ', '1 0') if rank == 10 else set.replace(
                                                let, pic_ranks(rank))
                                            # Cards: suits
                                            try:
                                                set = set.replace(let.upper(),
                                                                  suits[3][ranks[3].index(rank)])
                                                suits[3].pop(ranks[3].index(rank))  # Elimination
                                            except IndexError:
                                                set = set.replace(let.upper(), '-')
                                            ranks[3].remove(rank)  # Elimination

                                    elif len(details) == 1:
                                        details.append(rank)

                                        # Cards: ranks
                                        for let in lets[2:4]:
                                            set = set.replace(
                                                f' {let} ', '1 0') if rank == 10 else set.replace(
                                                let, pic_ranks(rank))
                                            # Cards: suits
                                            try:
                                                set = set.replace(let.upper(),
                                                                  suits[3][ranks[3].index(rank)])
                                                suits[3].pop(ranks[3].index(rank))
                                            except IndexError:
                                                set = set.replace(let.upper(), '-')
                                            ranks[3].remove(rank)

                                    else:
                                        details = tuple(details)
                                        break

                    # 2.5.3 High Card
                    case 1:
                        hand, details, hand_cards = 'HIGH CARD', max(ranks[3]), 1

                        # Cards: ranks
                        set = set.replace(' b ',
                                          '1 0') if details == 10 else set.replace(
                            'b', pic_ranks(details))
                        # Cards: suits
                        try:
                            set = set.replace('B', suits[3][ranks[3].index(details)])
                            suits[3].pop(ranks[3].index(details))
                        except IndexError:
                            set = set.replace('B', '-')

                        ranks[3].remove(details)
                        details = pic_ranks(details)

            kicker = ''
            # 3 Card Display & Kicker
            if hand_cards < 5:
                kicker = pic_ranks(max(ranks[3])) if ranks[3] else kicker

                for let in lets[hand_cards:5]:
                    # Cards: suits
                    try:
                        set = set.replace(let.upper(),
                                          suits[3][ranks[3].index(max(ranks[3]))])
                        suits[3].pop(ranks[3].index(max(ranks[3])))
                    except IndexError:
                        set = set.replace(let.upper(), '-')
                    except ValueError:
                        set = set.replace(let.upper(), '-')

                    # Cards: ranks
                    try:
                        set = set.replace(f' {let} ',
                                          '1 0') if max(ranks[3]) == 10 else set.replace(
                            let, pic_ranks(max(ranks[3])))
                        ranks[3].remove(max(ranks[3]))
                    except IndexError:
                        set = set.replace(let, '-')
                    except ValueError:
                        set = set.replace(let, '-')

            # The unimportant cards but still to display as part of a full hand
            if ranks[3]:
                for i in range(len(ranks[0]) - 5):
                    # Cards: ranks
                    set = set.replace(lets[i + 5], pic_ranks(ranks[3][0]))
                    ranks[3].pop(0)
                    # Cards: suits
                    try:
                        set = set.replace(lets[i + 5].upper(), suits[3][0])
                        suits[3].pop(0)
                    except IndexError:
                        set = set.replace(lets[i + 5].upper(), '')

            if 'h' in set:  # If there are still unnecessary ones
                set = set.replace('+ h H', '')
            if 'g' in set:
                set = set.replace('+ g G', '')

            # 4 Details

            # Checking through the combos that cannot be improved or altered, not matter what
            if stage != 3 and (hand == 'ROYAL FLUSH' or
                               (hand == 'FOUR OF A KIND' and (  # Royal Flush
                                       kicker == 'A' or
                                       (details == 14 and kicker == 'K')
                               )  # Four of a Kind: <As with A Kicker
                               )):  # Four of a Kind: As with K Kicker
                best = True

            # 4.1 Straight, Flush, Straight Flush
            if 'STRAIGHT' in hand or hand == 'FLUSH':
                details = f'{pic_ranks(details[0])}-High {details[1]}' if 'FLUSH' in hand else f'{pic_ranks(details)}-High'

            # 4.2 Pair, Three of a Kind, Four of a Kind
            elif hand == 'FOUR OF A KIND' or hand == 'THREE OF A KIND' or hand == 'PAIR':
                details = pic_ranks(details) + 's'

            # 4.3 Two, Pair, Full House
            elif hand == 'FULL HOUSE' or hand == 'TWO PAIR':
                details = f'{pic_ranks(details[0])}s - {pic_ranks(details[1])}s'
                details = details.replace(
                    '-', 'over') if hand == 'FULL HOUSE' else details.replace(
                    '-', '&')

            # 5 Final Display & Finish
            if best:
                break
            else:
                clear()
                title_display()
                print(f'╔═══\n║ {hand}\n║ ----')
                print(set)
                # full_hand = [hand, details, kicker]

                if stage == 0:
                    # 5.1 7-Deuce
                    if details == '7' and kicker == '2':
                        print('║ - 7-Deuce :(')
                    # 5.2 Pocket Rockets
                    elif hand == 'PAIR' and details == 'As':
                        print('║ - Pocket Rockets! :D')
                    else:
                        print(f'║ - {details} with {kicker} Kicker'
                              if kicker else f'║ - {details}')
                else:
                    print(f'║ - {details} with {kicker} Kicker'
                          if kicker else f'║ - {details}')
                print('\n------\n')

        if not exit or best:
            # At the end
            clear()
            title_display()

            print(f'╔═══\n║ {hand}\n║ ----')
            print(set)
            # full_hand = [hand, details, kicker]
            print(f'║ - {details} with {kicker} Kicker'
                  if kicker else f'║ - {details}')

            if best:
                print(
                    '\n----\nThis hand cannot be improved, so now the program will stop.\n----'
                )
            else:
                print('\n----')

            with suppress(KeyboardInterrupt):
                input('Press ENTER to start again')
            clear()

if __name__ == '__main__':
    main()