import pandas as pd

# Load dataset

data = pd.read_csv("places.csv")

print("=" * 65)
print("         DESIKA AI - Spiritual Travel Guide")
print("=" * 65)

while True:

 print("\n1. Search by State")
 print("2. Search by Place")
 print("3. Exit")

 choice = input("\nChoose an option: ").strip()

# -----------------------------
# Search State
# -----------------------------
 if choice == "1":

    state = input("\nEnter State Name: ").strip().lower()

    clean_state = data["State"].str.lower().str.replace(" ", "")

    result = data[
        clean_state == state.replace(" ", "")
    ]

    if not result.empty:

        print("\n" + "=" * 50)
        print(f"📍 Places in {result.iloc[0]['State']}")
        print("=" * 50)

        print(f"\nTotal Places Found: {len(result)}\n")

        for place in result["Place"]:
            print("•", place)

    else:

        print("\n❌ State not found.")

# -----------------------------
# Search Place
# -----------------------------
 elif choice == "2":

    place = input("\nEnter Place Name: ").strip().lower()

    clean_place = data["Place"].str.lower().str.replace(" ", "")

    result = data[
        clean_place == place.replace(" ", "")
    ]

    if not result.empty:

        row = result.iloc[0]

        print("\n" + "=" * 65)

        print("\nState:")
        print(row["State"])

        print("\nPlace:")
        print(row["Place"])

        print("\nReligion:")
        print(row["Religion"])

        print("\nPlace Type:")
        print(row["Place Type"])

        print("\nTourist Attractions:")
        print(row["Tourist Attractions"])

        print("\n🗺 Nearby Places:")
        print(row["Nearby Places"])

        print("\n" + "=" * 65)

    else:

        state_check = data[
            data["State"].str.lower().str.replace(" ", "") ==
            place.replace(" ", "")
        ]

        if not state_check.empty:

            print(f"\n⚠ {place.title()} is a State.")

            print("\nPlaces available:\n")

            for item in state_check["Place"]:
                print("•", item)

        else:

            print("\n❌ Place not found.")

            suggestions = data[
                data["Place"].str.lower().str.contains(place, na=False)
            ]

            if not suggestions.empty:

                print("\nDid you mean?\n")

                for item in suggestions["Place"]:
                    print("•", item)

# -----------------------------
# Exit
# -----------------------------
 elif choice == "3":

    print("\nThank you for using Desika AI.")
    print("Have a peaceful journey ")
    break

else:

    print("\n⚠ Please choose 1, 2 or 3.")
1
