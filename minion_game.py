def minion_game(string):
    kevin_points = 0;
    stuart_points = 0;
    vowels = ["A", "E", "I", "O", "U"]
    for vowel in vowels:
        letter_index = [pos for pos, char in enumerate(string) if char == vowel]
        for position in letter_index:
            kevin_points += len(string) - position

    stuart_points = len(string) * (len(string) + 1)/2 - kevin_points

    if stuart_points > kevin_points:
        print "Stuart {}".format(stuart_points)
    elif stuart_points < kevin_points:
        print "Kevin {}".format(kevin_points)
    else:
        print "Draw"
