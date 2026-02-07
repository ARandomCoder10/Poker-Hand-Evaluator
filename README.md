# Poker Hand Evaluator
A real-time poker assistant that evaluates the user's current hand based on the cards entered at each stage of the round.
Designed to aid novice players understand the criteria and relative weight of each hand.

## Technologies
- Python

## Status
- Development: started 2022 (age 14) - now completed
- Maintenance: started 2023 - ongoing minor refinements

## Post-Developement Algorithm Optimisations
- Stops asking for card suits when the possibility of a flush has disappeared
- Terminates card input when one of following unimprovable hands is determined:
  - Royal Flush
  - Four of a Kind with Ace Kicker
  - Four of a Kind (Aces) with King Kicker
- Added the following humourous messages to the pre-flop depending on the cards entered:
  - High Card: 7 with 2 Kicker - '7-Deuce :(', an informal term for the worst pre-flop
  - Pair: Aces - 'Pocket Rockets!', an informal term for the best pre-flop)
