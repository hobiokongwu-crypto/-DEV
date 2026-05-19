import random

while True:
    anointed = input("What is thou name, young warrior?: ").upper()

    if anointed.isalpha():
        # Good Job!!
        print(f"Welcome {anointed}, let us make way to Valhalla, brother!")
        break # Tis leaves the loop
    else:
        # Error message and loop restarts
        print("Error: Invalid Input!. Please use just letters this time, cool?")

# Initial stats
mc_hp = 100 # player_hp = mc_hp
boss_hp = 200
boss_posture = 50 # If this hits 0, U beat him!

print("--BATTLE LOGIC: PYTHON EDITION--") # Thx Sekiro😮‍💨
print("Rules: Parry beats attack. Attack beats stagnation. Dodge saves HP.")

while mc_hp > 0 and boss_posture > 0:
    #1. BOSS DECIDES AN ACTION
    boss_action = random.choice(["Heavy Attack", "Quick Swipe", "Idle"])

    #2. PLAYER'S INPUT
    print(f"\nBoss is preparing: {boss_action}")
    choice = input("Your move (A = Attack, P = Parry, D = Dodge, H = Healing Gourd):").upper()

    #3. THE ACTUAL COMBAT LOGIC(My potential "engine")
    if choice == "P":
        if boss_action == "Heavy Attack":
            mc_hp -= 3 * 10
            print("🩸🩸🩸DUMBASS, YOU GOT HIT!!!")
        else:
             if boss_action == "Quick Swipe":
                 boss_posture -= 2 * 10
                 print("🎆PERFECT PARRY! Boss posture damaged!")
            
    # Next time add if/else/elif statements for if the player attacks during a quick swipe
    # or when the player heals during idle, heavy attack, quick swipe and etc...        
    elif choice == "A":
        if boss_action == "Idle":
            boss_posture -= 2 * 10
            print("⚔️Critical Hit! Boss takes knockback.")
        else:
            if boss_action == "Quick Swipe":
                mc_hp -= 10
                boss_posture -= 10
                print("So you don't have arms to be blocking eyyy??😒😒😒")
            else:
                 if boss_action == "Heavy Attack":
                      mc_hp -= 5 * 10
                      print("🩸🩸🩸Only the Trinity can save you now.")
                 else:
                     if choice == "H":
                         mc_hp += 10
                         print("❤️‍🩹YOU HEALED! Now go get ur get back, son.")

    elif choice == "D":
        print("💨Congrats! You dodged.")
        

        
    print(f"Stats: MC's HP:{mc_hp} |Boss's Posture: {boss_posture}")

#4.END OF GAME
if boss_posture <= 0:
    print(f"\nBEAST FELLED - {anointed} IS THE VICTOR!!!")
else:
    if mc_hp <= 0:
         print("THOU HAST FALLEN")