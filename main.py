user = input("What is your first name?")
print("Hello there,", user)

print(user,", today you will be playing as a high school student and your goal will be to stay out of trouble and to avoid getting arrested")

start = ""
while start != "BEGIN":
  start = input("To begin the game, type BEGIN.")

print("")
print("It is Monday morning, and you can hear your alarm ringing. You check your phone and see that it is 6am.")
print("")
print("If you wake up now, you will be able to have a shower, eat your breakfast and get completely ready, and leave the house early. However, if you hit snooze, you might wake up too late.")
print("")

option1 = input("If you want to wake up now, enter X. If you want to snooze, enter Y.")

if option1 == "Y":
  print("Goodnight.")
  print("")
  print("Two hours later...")
  print("")
  print("It is now 8am and school is almost in session, you no longer have time to shower and you have to eat breakfast on the run, get your lazy bum up.")
  print("")
  print("")
  print("")
  print("")
  print("You trip over a bag as you are running to school, you open the bag and there is a murder weapon inside!")
  print("")
  print("A witness reports you to the police, later you are arrested")
  print("")
  print("Sorry but you failed to stay out of trouble, damn you aren't very good at this, no offence")
  print("")
  print("")
  print("Refresh page to try again")
elif option1 == "X":
  print("Ok, have a good day at school,", user)
  print("")
  print("It might be your last")
  print("")
  print("...")
  print("")
  print("You make to to school without any problems")
  print("")
  print("*Good morning!,", user, "*")
  friend = input("what's your best friends name?")
  print(friend, ", good choice")
  option2 = input("To ignore your friend, enter X. To respond to your friend, enter Y.")
  if option2 == "X":
    print(friend,"will remember this")
    print("")
    print("")
    print("A few hours later...(afterschool)")
    print("")
    print("")
    print("The police are investigating a murder and they find the weapon in your bag")
    print("")
    print("Due to your unfriendly manners towards your friend, out of revenge, he planted the weapon in your bag.")
    print("")
    print("")
    print("You failed yet again to stay out of trouble for even a DAY, maybe next time just respond to your friend") 
  elif option2 == "Y":
    print("You respond to your friend with a friendly hello")
    print("")
    print(friend, "looks overjoyed")
    print("")
    print("you both walk into class happily")
    print("")
    print("*bell rings*")
    print("")
    print("*Hey", user, "wanna go out for lunch today*")
    print("")
    option3 = input("Enter X to accept. Enter Y to decline and share yours with them.")

    if option3 == "X":
      print("*Okay lets go to the mcDonalds one block away from here*")
      print("")
      print("You guys go down the block towards the mcDonalds and you run into a group of thugs that threaten to beat you up if you don't give them your money")
      print("")
      print("")
      print("Sorry, but you failed to stay out of trouble, if this wasn't your first time failing, I have a hint for you. How about you play it safe...Duh")
    elif option3 == "Y":
      print("")
      print("*Ay thanks, you're a lifesaver.")
      print("")
      print("*You both sit down for lunch.*")
      print("")
      print("Hey,", user)
      print("")
      print("*Can I tell you a secret?")
      print("")
      option4 = input("To listen to the secret, enter X. To not hear the secret, enter Y")
      if option4 == "Y":
        print("")
        print("You're short-tempered friend hates the fact that you won't listen to him.")
        print("")
        print("The police arrest your friend later that day for murder.")
        print("")
        print(friend, "confesses to the murder and says you were an accomplice out of petty revenge.")
        print("")
        print("CONGRATS, yet again you have failed to stay out of TROUBLE, how hard could it really be?")
      elif option4 == "X":
        print("")
        print("*Okay, so just before school started, I shot someone and ran away.*")
        print("")
        print("*Im really nervous because I don't want to go to jail, and what if someone saw me.*")
        print("")
        print("*What should I do?*")
        option5 = input("To tell the police, enter Y, to help him get away, enter X")
        if option5 == "X":
          print("")
          print("*Thanks man, I don't know how i'll ever repay you.*")
          print("")
          print("A search is sent out for", friend)
          print("")
          print("They find your friend and you hiding him, you get arrested for being an accomplice in the murder.")
          print("")
          print("REALLY, YOU THOUGHT IT WAS A GOOD IDEA TO HID A MURDERER, LMAO.")
        elif option5 == "Y":
          print("")
          print("The police arrest", friend)
          print("")
          print("The police thank you for helping them are reporting it to them.")
          print("")
          print("")
          print("You make it home safely with no problems what-so-ever.")
          print("")
          print("")
          print("Congrats, you have successfully made it thought the day without getting into trouble.")
          print("")
          print("")
          print("")
          print("THANK YOU FOR PLAYING ALL THE WAY THROUGH, IT MEANS A LOT")