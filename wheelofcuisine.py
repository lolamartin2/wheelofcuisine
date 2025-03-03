import random
import time
import sys
import os

FILENAME = "cuisines.txt"

# Full list of cuisines (for resetting or first-time setup)
FULL_CUISINES_LIST = [
    "🥧 BRITISH", "🍝 ITALIAN", "🥖 FRENCH", "🥘 SPANISH", "🦞 PORTUGUESE", "🥗 GREEK", "🍢 TURKISH", "🥨 GERMAN", "🥟 POLISH", "🍣 JAPANESE",
    "🍜 CHINESE", "🍱 KOREAN", "🍛 THAI", "🍲 VIETNAMESE", "🍛 INDIAN", "🥘 PAKISTANI", "🥘 BANGLADESHI", "🥥 SRI LANKAN",
    "🍢 MALAYSIAN", "🍢 FILIPINO", "🥥 INDONESIAN", "🍜 BURMESE",
    "🥙 LEBANESE", "🍢 PERSIAN", "🥙 ISRAELI", "🍲 MOROCCAN", "🍢 EGYPTIAN", "🥙 IRAQI",
    "🍛 ETHIOPIAN", "🍛 ERITREAN", "🥘 NIGERIAN", "🍛 GHANAIAN", "🍛 SOMALI", "🥩 SOUTH AFRICAN",
    "🥘 JAMAICAN", "🥘 TRINIDADIAN", "🥘 CUBAN",
    "🍔 AMERICAN", "🌮 MEXICAN", "🥩 BRAZILIAN", "🥩 ARGENTINIAN", "🥔 PERUVIAN",
    "🥘 RUSSIAN", "🍖 GEORGIAN", "🥘 AFGHAN", "🍛 NEPALESE", "🍜 TIBETAN"
]

# Create file if it doesn't exist or is empty
if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write("\n".join(FULL_CUISINES_LIST))  # Write full list
    print("🆕 Created a new cuisine list.")

# Ask if user wants to reset
choice = input("Type 'reset' to start fresh, or press ENTER to continue: ").strip().lower()
if choice == "reset":
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write("\n".join(FULL_CUISINES_LIST))
    print("✅ Cuisine list reset!")

# Load cuisines from file
with open(FILENAME, "r", encoding="utf-8") as file:
    cuisines = [line.strip() for line in file.readlines()]

while True:
    print("\n🎡 Welcome to the WHEEL OF CUISINE, let's SPIN THAT WHEEL! 🎡 ")

    for _ in range(10):  
        fake_choice = random.choice(cuisines)
        sys.stdout.write(f"\r 😋 {fake_choice} 🤤" + " " * 20)  
        sys.stdout.flush()
        time.sleep(0.2)

    sys.stdout.write("\r" + " " * 50 + "\r")  
    sys.stdout.flush()

    final_choice = random.choice(cuisines)
    final_choice2 = random.choice(cuisines)
    res = input(f"== TONIGHT'S CHOICE IS ==\n 🎉 {final_choice} 🎉 (Type 'no' or 'ok') ")

    if res.lower() == "no":
        print(f"Ok picky, tonight you will be eating {final_choice2}")
        cuisines.remove(final_choice2)
    elif res.lower() == "ok":
        cuisines.remove(final_choice)

        # SAVE PROGRESS: Write remaining cuisines to file
        with open(FILENAME, "w", encoding="utf-8") as file:
            file.write("\n".join(cuisines))

        print(f"Enjoy your meal! 🍽️ There are {len(cuisines)} cuisines left to try!")
    else:
        print("I am not that sophisticated, please type either 'no' or 'ok'. Try again!")

    input("\nPress ENTER to spin the wheel again! 🎡")





