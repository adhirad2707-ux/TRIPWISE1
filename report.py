from conflicts import check_time_conflicts


def show_summary(
    trip,
    itinerary,
    budget,
    group_expenses
):

    print("\n" + "=" * 55)
    print("                  TRIPWISE SUMMARY")
    print("=" * 55)

    print(
        f"Destination : {trip['destination']}"
    )

    print(
        f"Duration    : {trip['days']} day(s)"
    )

    print(
        f"Travellers  : {trip['travellers']}"
    )

    print(
        f"Trip type   : {trip['trip_type']}"
    )

    print(
        f"Budget      : ₹{trip['budget']:.2f}"
    )

    print("\nITINERARY")
    print("-" * 55)

    if itinerary:

        for day in itinerary:

            print(f"Day {day['day']}:")

            for item in day["activities"]:

                print(
                    f"  {item['start']}-"
                    f"{item['end']} | "
                    f"{item['place']}"
                )

    else:

        print("Itinerary not created yet.")

    print("\nBUDGET")
    print("-" * 55)

    if budget:

        print(
            f"Estimated cost: "
            f"₹{budget['total']:.2f}"
        )

        print(
            f"Difference from budget: "
            f"₹{budget['remaining']:.2f}"
        )

    else:

        print("Budget not created yet.")

    print("\nTIME CHECK")
    print("-" * 55)

    if itinerary:

        conflicts = check_time_conflicts(
            itinerary
        )

        if conflicts:

            print(
                f"{len(conflicts)} "
                f"conflict(s) detected."
            )

        else:

            print("No time conflicts detected.")

    else:

        print(
            "Create an itinerary "
            "to check conflicts."
        )

    print("=" * 55)