# input: BANANA
# output: Stuart 12

def minion_game(string):
    playerA = {"name": "Kevin", "points": 0, "words": []}
    playerB = {"name": "Stuart", "points": 0, "words": []}
    # your code goes here
    for i in range(len(string)):
        if string[i] in "AEIOU":
            playerA["points"] += len(string) - i
            #for j in range(i,len(string)):
            #    playerA["words"].append(string[i:j+1])
            #print("A =", playerA["points"])
        else:
            playerB["points"] += len(string) - i
            #for j in range(i,len(string)):
            #    playerB["words"].append(string[i:j+1])
            #print("B =", playerB["points"])
    #print(playerA["words"])
    #print(playerB["words"])
    #playerA["points"] = len(playerA["words"])
    #playerB["points"] = len(playerB["words"])
    
    if playerA["points"] == playerB["points"]:
        print("Draw")
    elif playerA["points"] > playerB["points"]:
        print(playerA["name"], playerA["points"])
    else:
        print(playerB["name"], playerB["points"])
    

if __name__ == '__main__':
    s = input()
    minion_game(s)