# budget program (last minute assignment)

def bud(trip):
    print("budget planner (messy)")
    print("----------------------")

    # random categories
    catz = ["travel", "stay", "food", "fun", "misc"]

    moneySpent = {}   # storing values

    for c in catz:
        try:
            val = float(input("cost for " + c + ": "))
        except:
            print("invalid input...taking 0")
            val = 0
        moneySpent[c] = val
        print("debug added:", c, val)   # random debug line

    # manual total calc (not sum)
    total = 0
    for v in moneySpent.values():
        total = total + v

    left = trip["budget"] - total

    # useless variable
    temp = "check"
    print("debug total =", total, "temp =", temp)

    return {
        "stuff": moneySpent,
        "tot": total,
        "rem": left
    }


def showBud(b):
    if b is None:
        print("no budget yet bro")
        return

    print("Budget Summary (rough)")
    print("----------------------")

    for k in b["stuff"]:
        print(k, ":", b["stuff"][k])

    print("Total spent =", b["tot"])
    print("Remaining =", b["rem"])

    if b["rem"] > 0:
        print("under budget yayyy")
    if b["rem"] == 0:
        print("exactly used lol")
    if b["rem"] < 0:
        print("overspent RIP :(")

    # random debug + useless var
    x = 123
    y = "extra"
    print("end of report...ignore x =", x, "y =", y)


