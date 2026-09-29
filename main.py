
# tripwise program (hope it works)

from trip import create_trip
from itinerary import itinMaker
from conflicts import check_time_conflicts
from group_expenses import grpExp   
from report import show_summary
from utils import pause


def main():
    print("=" * 40)
    print("TRIPWISE-my trip planner thing")
    print("=" * 40)

    trip = create_trip()

    # just making empty variables
    itinerary = []
    bud = {}
    grp_exp = []

    while True:
        print("\n" + "-" * 40)
        print("MAIN MENU (choose what's needed)")
        print("-" * 40)

        print("1.Itinerary")
        print("2.Budget")
        print("3.Conflicts")
        print("4.Group Expenses")
        print("5.Summary")
        print("6.Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            itinerary = itinMaker(trip)
            print("\n--- Your Itinerary ---")
            print(itinerary)
            pause()

        elif choice == "2":
            import budget

            if hasattr(budget,'budget_planner'):
                bud = budget.budget_planner(trip)

            elif hasattr(budget,'budget'):
                bud = budget.budget(trip)

            if hasattr(budget,'show_budget'):
                budget.show_budget(bud)

            else:
                print(bud)

            pause()

        elif choice=="3":
            if not itinerary:
                print("make itinerary first bro")

            else:
                conflicts = check_time_conflicts(itinerary)

                if conflicts:
                    print("conflicts found!!")

                    for c in conflicts:
                        print("->", c)

                else:
                    print("no conflicts lol")

                pause()

        elif choice=="4":
            grp_exp = grpExp(trip)
            pause()

        elif choice=="5":
            show_summary(trip, itinerary, bud, grp_exp)
            pause()

        elif choice=="6":
            print("ok bye thanks for using")
            break

        else:
            print("wrong choice dude (1-6 only)")

if __name__ == "__main__":
    main()
