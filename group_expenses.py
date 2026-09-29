# group expense splitter (last minute code lol)

from trip import get_positive_float

def grpExp(trip):
    print("Group Expense Splitter")
    print("----------------------")

    expList = []   # storing expenses

    for i in range(1, trip["travellers"] + 1):
        nm = input("Traveller " + str(i) + " name: ").strip()

        while nm == "":
            print("name empty not allowed bro")
            nm = input("Traveller " + str(i) + " name: ").strip()

        amt = get_positive_float("Money paid by " + nm + " (₹): ")
        expList.append({"name": nm, "paid": amt})

        # random debug
        print("added:", nm, amt)

    # total calc (manual loop, not sum)
    tot = 0
    for p in expList:
        tot = tot + p["paid"]

    fairShare = tot / len(expList)

    print("\nExpense Summary (rough)")
    print("----------------------")
    print("Total spent =", tot)
    print("Fair share per person =", fairShare)

    # who pays/gets
    for p in expList:
        diff = p["paid"] - fairShare

        if diff > 0:
            print(p["name"], "gets back", diff, "rs")
        elif diff < 0:
            print(p["name"], "pays", -diff, "rs")
        else:
            print(p["name"], "is settled lol")

        # extra random print
        print("debug check traveller:", p["name"])

    # useless variable
    x = 123
    print("end of function...ignore x =", x)

    return expList
