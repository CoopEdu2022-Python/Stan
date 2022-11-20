import random
class Citizen:
    def vote(self):
        return random.randint(0,len(players)-1)
    def select(self):
        return 'citizen'
class Mafia:
    def kill(self):
        return random.randint(0,len(players)-1)
    def vote(self):
        return random.randint(0,len(players)-1)
    def select(self):
        return 'mafia'
class Judge:
    def vote(self):
        return random.randint(0,len(players)-1)
    def select(self):
        return 'judge'
players=[]
for i in range(6):
    players.append(Citizen())
for i in range(3):
    players.append(Mafia())
players.append(Judge())
def game(players):
    while 1:
        select=[]
        vote=[]
        for player in players:
            if player.select()=='mafia':
                select.append(player.kill())
                print(select)
        if len(set(select))==len(select):
            print("Mafia kills %s" % (players[max(select)].select()))
            players.pop(max(select))
        else:
            killed=False
            for items in range(1,len(select)):
                i1=select[0]
                i2=select[items]
                if i1==i2:
                    print("Mafia kills %s" % (players[select[0]].select()))
                    players.pop(select[0])
                    killed=True
            if killed==False:
                print("Mafia kills %s" % (players[select[1]].select()))
                players.pop(select[1])
        mafia_live=False
        good_live=False
        for player in players:
            if player.select()=='citizen':
                good_live=True
            if player.select()=='mafia':
                mafia_live=True
            if player.select()=='judge':
                good_live=True
        if good_live==False:
            print("Mafia Wins")
            break
        elif mafia_live==False:
            print("Good Wins")
            break
        print("开始讨论")
        for player in players:
            vote.append(player.vote())
        print("投票结果",vote)
        if len(set(vote))==len(vote):
            print("Players vote to kill %s" % (players[max(vote)].select()))
            players.pop(max(vote))

        else:
            num=0
            c1=-10
            for x,y in enumerate(vote):
                if c1<=vote.count(num):
                    c1=vote.count(num)
                    c2=x
                num+=1
            print("Players vote to kill %s" % (players[c2].select()))
            players.pop(c2)
        mafia_live=False
        good_live=False
        for player in players:
            if player.select()=='citizen':
                good_live=True
            if player.select()=='mafia':
                mafia_live=True
            if player.select()=='judge':
                good_live=True
        if good_live==False:
            print("Mafia Wins")
            break
        elif mafia_live==False:
            print("Good Wins")
            break
        else:
            continue





game(players)

