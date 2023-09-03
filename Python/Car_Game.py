usr_input=input("> ").lower()#Get user input
started = False#Set started to False
while True:
    if usr_input == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
        usr_input=input("> ").lower()
    elif usr_input == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif usr_input == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif usr_input == "quit":
        break
    else:
        print("I don't understand that...")
        usr_input=input("> ").lower()