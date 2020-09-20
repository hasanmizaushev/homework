def p_ace_diamond():
    P_Diamond = 13/52
    P_Ace_n_Diamond = (2/52)
    P_Ace_given_Dimond = P_Ace_n_Diamond / P_Diamond
    return P_Ace_given_Dimond


def p_ace_king():
    P_King = 4/52
    P_King_n_Ace = 8/52
    P_Ace_given_King = P_King_n_Ace / P_King
    return P_Ace_given_King


def p_ace_6():
    P_6 = 4 / 52
    P_6_n_Ace = 8 / 52
    P_Ace_given_6 = P_6_n_Ace / P_6
    return P_Ace_given_6


def p_ace_ace():
    P_Ace = 4 / 52
    P_Ace_n_Ace = 4 / 52
    P_Ace_given_Ace = P_Ace_n_Ace / P_Ace
    return P_Ace_given_Ace


def p_6_spade():
    P_Spade = 13 / 52
    P_Spade_n_6 = 1 / 52
    P_6_given_Spade = P_Spade_n_6 / P_Spade
    return P_6_given_Spade


