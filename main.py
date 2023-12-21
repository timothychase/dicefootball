import random

input("\nDice Football by Timothy Chase")

team_user = input("\nEnter team name: ")
user_goalkeeper = input("Enter goalkeeper: ")
user_defender1 = input("Enter left-back: ")
user_defender2 = input("Enter centre-back: ")
user_defender3 = input("Enter centre-back: ")
user_defender4 = input("Enter right-back: ")
user_midfielder1 = input("Enter holding midfielder: ")
user_midfielder2 = input("Enter attacking midfielder: ")
user_winger1 = input("Enter left winger: ")
user_winger2 = input("Enter right winger: ")
user_striker1 = input("Enter striker: ")
user_striker2 = input("Enter striker: ")

input(f"\n{team_user} is {user_goalkeeper}, {user_defender1}, {user_defender2}, {user_defender3}, {user_defender4},"
      f" {user_midfielder1}, {user_midfielder2}, {user_winger1}, {user_winger2}, {user_striker1}, {user_striker2}")

team_opp = "Legends"
opp_goalkeeper = "Yashin"
opp_defender1 = "Carlos Alberto"
opp_defender2 = "Baresi"
opp_defender3 = "Beckenbauer"
opp_defender4 = "Maldini"
opp_midfielder1 = "Charlton"
opp_midfielder2 = "Platini"
opp_winger1 = "Matthews"
opp_winger2 = "Best"
opp_striker1 = "Pele"
opp_striker2 = "Maradona"

input(f"\nOpposition is {team_opp}")

input(f"\n{team_opp} is {opp_goalkeeper}, {opp_defender1}, {opp_defender2}, {opp_defender3}, {opp_defender4},"
      f" {opp_midfielder1}, {opp_midfielder2}, {opp_winger1}, {opp_winger2}, {opp_striker1}, {opp_striker2}")

input("\nKick Off!")

score = [0, 0]
goals_user = 0
goals_opp = 1


def roll_dice(num):
    return random.randint(1, num)


def assist():
    outcome = roll_dice(3)
    if outcome == 1:             # turnover
        outcome = roll_dice(5)
        if outcome == 1:
            input(f"{random.choice(striker)} ruled offside")
        elif outcome == 2:
            input("pass goes astray")
        elif outcome == 3:
            input("throw-in")
        elif outcome == 4:
            input(f"{random.choice(midfielder)} tackled")
        elif outcome == 5:
            input(f"{random.choice(midfielder)} gives away free-kick")
    elif outcome == 2:      # keep
        outcome = roll_dice(6)
        if outcome == 1:
            input(f"{random.choice(midfielder)} turns and keeps possession")
        elif outcome == 2:
            input(f"{random.choice(defender)} brings it out from the back")
        elif outcome == 3:
            input(f"{random.choice(midfielder)} passes it out to the wing")
        elif outcome == 4:
            input(f"{random.choice(midfielder)} passes short")
        elif outcome == 5:
            input(f"{random.choice(midfielder)} picks it up in midfield")
        elif outcome == 6:
            input(f"{random.choice(winger)} wins free-kick")
        assist()
    elif outcome == 3:      # move
        outcome = roll_dice(6)
        if outcome == 1:
            input(f"{random.choice(winger)} crosses")
        elif outcome == 2:
            input(f"{random.choice(midfielder)} passes into the area")
        elif outcome == 3:
            input(f"{random.choice(winger)} dribbles forward")
        elif outcome == 4:
            input(f"{random.choice(midfielder)} plays a through ball")
        elif outcome == 5:
            input(f"{random.choice(defender)} launches a long ball")
        elif outcome == 6:
            input(f"{random.choice(striker)} finds space in the area")
        attempt(score)


def attempt(g=list):
    outcome = roll_dice(4)
    if outcome == 1:
        input(f"{random.choice(striker)} shoots")
    elif outcome == 2:
        input(f"{random.choice(striker)} is one on one with the keeper")
    elif outcome == 3:
        input(f"{random.choice(striker)} heads towards goal")
    elif outcome == 4:
        input(f"{random.choice(striker)} meets it on the volley")
    outcome = roll_dice(12)
    if outcome in (1, 2):
        input("GOAL!!!")
        if who == team_user:
            g[goals_user] += 1
        elif who == team_opp:
            g[goals_opp] += 1
    elif outcome in (3, 4):
        outcome = roll_dice(3)
        if outcome == 1:
            input("rebound")
        elif outcome == 2:
            input("hits the post")
        elif outcome == 3:
            input("hits the bar")
        attempt(score)
    elif outcome in (5, 6):
        input("misses")
    elif outcome in (7, 8, 9):
        input(f"{goalkeeper} saves")
    elif outcome in (10, 11):
        input("corner")
        input(f"{random.choice(winger)} takes the corner")
        attempt(score)
    elif outcome == 12:
        input("penalty")
        input(f"{random.choice(striker)} takes the penalty")
        outcome = roll_dice(5)
        if outcome == 1:
            input("GOAL!!!")
            if who == team_user:
                g[goals_user] += 1
            elif who == team_opp:
                g[goals_opp] += 1
        elif outcome == 2:
            input("GOAL!!!")
            if who == team_user:
                g[goals_user] += 1
            elif who == team_opp:
                g[goals_opp] += 1
        elif outcome == 3:
            input("GOAL!!!")
            if who == team_user:
                g[goals_user] += 1
            elif who == team_opp:
                g[goals_opp] += 1
        elif outcome == 4:
            input("GOAL!!!")
            if who == team_user:
                g[goals_user] += 1
            elif who == team_opp:
                g[goals_opp] += 1
        elif outcome == 5:
            input("misses")
    return g


def who_has_ball():
    outcome = roll_dice(2)
    if outcome == 1:
        input(f"\n{team_user} have the ball")
        return team_user
    else:
        input(f"\n{team_opp} have the ball")
        return team_opp


counter = 0
while counter < 20:
    who = who_has_ball()
    if who == team_user:
        goalkeeper = opp_goalkeeper
        defender = [user_defender1, user_defender2, user_defender3, user_defender4]
        midfielder = [user_midfielder1, user_midfielder2]
        winger = [user_winger1, user_winger2]
        striker = [user_striker1, user_striker2]
    elif who == team_opp:
        goalkeeper = user_goalkeeper
        defender = [opp_defender1, opp_defender2, opp_defender3, opp_defender4]
        midfielder = [opp_midfielder1, opp_midfielder2]
        winger = [opp_winger1, opp_winger2]
        striker = [opp_striker1, opp_striker2]
    assist()
    print(f"{score[goals_user]} - {score[goals_opp]}")
    counter += 1


















