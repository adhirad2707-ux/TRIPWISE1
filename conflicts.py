# time convert karne ka function 
def timeToMin(txt):
    try:
        h, m = txt.split(":")
        h = int(h)
        m = int(m)
        if h >= 0 and h <= 23 and m >= 0 and m <= 59:
            return h * 60 + m
    except:
        print("error in time:", txt)  # debug print
        return None
    return None


def check_time_conflicts(itinerary):
    probs = []   # conflicts list

    for d in itinerary:
        acts = d["activities"]

        # double loop (messy way)
        for i in range(len(acts)):
            for j in range(i + 1, len(acts)):
                a1 = acts[i]
                a2 = acts[j]

                s1 = timeToMin(a1["start"])
                e1 = timeToMin(a1["end"])
                s2 = timeToMin(a2["start"])
                e2 = timeToMin(a2["end"])

                if None in (s1, e1, s2, e2):
                    continue

                if s1 >= e1 or s2 >= e2:
                    # invalid times
                    continue

                # overlap check
                if s1 < e2 and s2 < e1:
                    probs.append(
                        "Day " + str(d["day"]) + ": " +
                        a1["place"] + " (" + a1["start"] + "-" + a1["end"] + ")" +
                        " clashes with " +
                        a2["place"] + " (" + a2["start"] + "-" + a2["end"] + ")"
                    )
                    print("debug conflict found!")  # random debug

    return probs
