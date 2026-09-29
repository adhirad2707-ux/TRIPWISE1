def get_positive_int(prompt):

    while True:

        try:

            value = int(input(prompt))

            if value > 0:
                return value

            print("Please enter a positive number.")

        except ValueError:

            print("Please enter a valid whole number.")


def get_positive_float(prompt):

    while True:

        try:

            value = float(input(prompt))

            if value > 0:
                return value

            print("Please enter a positive amount.")

        except ValueError:

            print("Please enter a valid number.")


def create_trip():

    print("\nTRIP SETUP")
    print("-" * 30)

    destination = input("Destination: ").strip()

    while not destination:

        print("Destination cannot be empty.")
        destination = input("Destination: ").strip()

    days = get_positive_int("Number of days: ")

    travellers = get_positive_int(
        "Number of travellers: "
    )

    budget = get_positive_float(
        "Total trip budget (₹): "
    )

    print("\nTrip type:")
    print("1. Relaxing")
    print("2. Sightseeing")
    print("3. Adventure")
    print("4. Mixed")

    types = {
        "1": "Relaxing",
        "2": "Sightseeing",
        "3": "Adventure",
        "4": "Mixed"
    }

    while True:

        choice = input("Choose trip type: ").strip()

        if choice in types:

            trip_type = types[choice]
            break

        print("Choose a number from 1-4.")

    return {
        "destination": destination,
        "days": days,
        "travellers": travellers,
        "budget": budget,
        "trip_type": trip_type
    }