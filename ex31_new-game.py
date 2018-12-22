print("How much time do you have to get to the office?\n1. Less than 15min.\n2. Around 30min.\n3. No rush, more than 30min is fine.")
time_to_spare = input(">> ")

if time_to_spare == "1":
    print("Take an uber, you late bastard")
elif time_to_spare == "2":
    print("Is it raining or snowing outside?\n1. Yep.\n2. Nope.")
    rain = input(">> ")
    
    if rain == "1":
        print("Walk to 57th and 10th and get the M31 or M57.")
    elif rain == "2":
        print("Take a nice walk then.")
    else:
        print("Se não quer responder direito, se fode aí!")
elif time_to_spare == "3":
    print("Walk to 57th and 10th and get the M31 or M57.")
else:
    print("Se não quer responder direito, se fode aí!")