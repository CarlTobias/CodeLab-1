print("\nExercise 7\n")

travel = ["United Kingdom", "France", "Italy", "Sweden", "Maldives"]
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

sortedtravel = sorted(travel)
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] +  "\n- " + travel[3] + "\n- " + travel[4] + "\n")

rsortedtravel = sorted(travel, reverse=True)
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

travel.reverse()
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

travel.reverse()
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

travel.sort()
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")

travel.sort(reverse = True)
print("I would like to go to these places:" +
      "\n- " + travel[0] + "\n- " + travel[1] + "\n- " +
      travel[2] + "\n- " + travel[3] + "\n- " + travel[4] + "\n")
