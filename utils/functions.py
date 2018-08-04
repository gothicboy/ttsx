import random


def get_ticket():

    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    ticket = ''
    for _ in range(30):
        ticket = random.choice(s)

    return 'TK_'+ticket