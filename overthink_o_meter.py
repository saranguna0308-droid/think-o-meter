import os
import random
import sys
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def dramatic_pause(text, dots=3, delay=0.4):
    sys.stdout.write(text)
    sys.stdout.flush()
    for _ in range(dots):
        time.sleep(delay)
        sys.stdout.write(".")
        sys.stdout.flush()
    print()


def show_easter_egg():
    clear_screen()
    print("\n" + "=" * 64)
    print("  [NOISE CLEARED — A QUIET REMINDER FOR YOU]")
    print("=" * 64 + "\n")
    time.sleep(0.6)

    print(
        "First, I want to genuinely apologize for everything I did.\n"
        "I should never have hurt the good girl in you — the little\n"
        "baby inside you that I once promised I would always protect\n"
        "and take care of.\n"
    )
    time.sleep(0.9)

    print(
        "With or without me, never lose that pure heart. Always stay\n"
        "the strong, proud girl you are.\n"
    )
    time.sleep(0.8)

    print(
        "Take a deep breath, don't overthink or over-stress — everything\n"
        "is going to be alright. I truly wish you everything good in life.\n"
        "May you stay safe wherever you go, keep growing every single day,\n"
        "and achieve all your dreams — in fact, achieve even bigger than\n"
        "your dreams.\n"
    )
    time.sleep(0.9)

    print(
        "I'm not here to force anything or put any pressure on you;\n"
        "I just genuinely want to see you happy. And always remember —\n"
        "whenever you need someone safe to lean on, or whenever life\n"
        "feels heavy, I will always be right here for you."
    )
    print("\n" + "=" * 64 + "\n")


def run_diagnostic():
    clear_screen()
    print("=" * 56)
    print("   THINK-O-METER v1.0 | Brain Stress Diagnostic CLI")
    print("=" * 56 + "\n")

    dramatic_pause("Connecting to active brain cells")
    dramatic_pause("Scanning 2 AM memories & hypothetical scenarios")
    print()

    questions = [
        "1. Did you replay a 5-second conversation in your head 10 times today? (y/n): ",
        "2. When someone replies with just 'Ok' or 'Hmm', do you assume they're mad? (y/n): ",
        "3. Do you randomly remember awkward things from 3 years ago before sleeping? (y/n): ",
    ]

    yes_count = 0
    for q in questions:
        ans = input(q).strip().lower()
        if ans.startswith("y"):
            yes_count += 1

    print("\n" + "-" * 56)
    thought = input("In one word or phrase, what's currently on your mind?: ")

    # Capital letters (Ammu / AMMU) or extra spaces irunthalum catch pannum
    normalized = " ".join(thought.lower().strip().rstrip(".!?").split())
    secret_trigger = "ammu"

    if normalized == secret_trigger:
        show_easter_egg()
        return

    print("\n" + "-" * 56)
    dramatic_pause("Calculating mental CPU usage", dots=4, delay=0.35)

    overthink_score = min(99, 64 + (yes_count * 10) + random.randint(1, 9))
    diagnoses = [
        "47 Chrome tabs are open in your brain, and 3 of them are playing music you can't find.",
        "Your brain is currently running 14 imaginary arguments that will never happen.",
        "Warning: High RAM usage detected from over-analyzing things you cannot control.",
    ]
    prescriptions = [
        "Drink a full glass of water, put your phone face-down for 15 minutes, and breathe.",
        "Step away from the screen, stretch your shoulders, and touch some grass.",
        "Close the mental tabs. Future-you will handle it just fine.",
    ]

    print(f"\nOverthinking Level : {overthink_score}% (Critical)")
    print(f"Diagnosis          : {random.choice(diagnoses)}")
    print(f"Prescription       : {random.choice(prescriptions)}")
    print("\n" + "=" * 56 + "\n")


if __name__ == "__main__":
    run_diagnostic()