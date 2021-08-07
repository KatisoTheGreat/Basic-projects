command = ""
started = False

while True:
  command = input("> ").lower() #Use the lower method here so that you don't have to repeat it in each step
  if command == "start":
    if started:
      print("The car has already started")
    else:
      started = True
      print("Car has started")
  elif command == "stop":
    if not started:
      print("The car has already stopped")
    else:
      started = False
      print("The car has stopped")
  elif command == "help":
    print("""
start - start the car
stop - stop the car
quit - to quit
    """)
  elif command == "quit":
    break
  else:
    print("Sorry I don't understand that command")
