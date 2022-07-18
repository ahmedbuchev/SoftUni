def winning_ticket(tickets):

    winning_symbols = ['@', '#', '$', '^']
    left_side = ticket[:10]
    right_side = ticket[10:]
    if not len(ticket) == 20:
        return "invalid ticket"
    for winning_symbol in winning_symbols:
        for repetition in range(10, 5, -1):
            winning_symbol_repetition = winning_symbol * repetition
            if winning_symbol_repetition in left_side and winning_symbol_repetition in right_side:
                if repetition == 10:
                    return f'ticket "{ticket}" - {repetition}{winning_symbol} Jackpot!'
                return f'ticket "{ticket}" - {repetition}{winning_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [el.strip() for el in input().split(", ")]
for ticket in tickets:
    print(winning_ticket(tickets))





