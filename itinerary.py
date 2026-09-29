# itinerary builder (last minute assignment lol)

from trip import get_positive_int

def itinMaker(trip):
    daysPlan = []   # storing all days

    print("Itinerary Builder (messy)")
    print("-------------------------")

    for d in range(1, trip["days"] + 1):
        print("\nDay", d)

        numActs = get_positive_int("How many activities today? ")

        acts = []

        for i in range(1, numActs + 1):
            print("\nActivity", i)

            place = input("Place/activity: ").strip()
            while place == "":
                print("empty name not allowed bro")
                place = input("Place/activity: ").strip()

            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")

            # random debug
            print("debug added:", place, start, "-", end)

            acts.append({
                "place": place,
                "start": start,
                "end": end
            })

        daysPlan.append({
            "day": d,
            "activities": acts
        })

        # useless var
        temp = "done"
        print("debug day done:", temp)

    return daysPlan


def showItin(plan):
    print("\nYour Itinerary (rough)")
    print("=======================")

    for d in plan:
        print("\nDay", d["day"])

        if len(d["activities"]) == 0:
            print("no activities lol")
        else:
            for act in d["activities"]:
                # mixing concat + commas
                print("-", act["start"] + "-" + act["end"], ":", act["place"])

        # random extra line
        print("end of day", d["day"], "report lol")
