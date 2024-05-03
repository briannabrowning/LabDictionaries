def list_names (students):                # create a function
  for index, people in enumerate(students, start=1):      # starts a loop. enumerate creates the index and people pairs
    print(f"{index}: {people['name']}")                 # index is the position the name is in the list

def get_new_students ():
  new_student = {}                     # create black dictionary
  new_student["name"] = input("Please input a name for the student: ")  # prompt new name
  new_student["hometown"] = input("Next please input their hometown: ")  # prompt hometown
  new_student["favorite_food"] = input("Last please input their favorite food: ") #prompt fav food
  return new_student                      # return the result

students = [
    {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
  ]


while True:                              # need a loop
  option = input("Please select which action you'd like to do: add, view, or quit ")
  if option == "add":
    new_student = get_new_students()      # define that new_students is going to use the new dictionary
    students.append(new_student)          # add the new student to the current dictionsary
  elif option == "view":
    list_names(students)
    index = input("Which student would you like to learn more about? Enter a number 1-4: ")    #prompt the user to enter an index
    if index.isdigit():      # ensure user enters a digit
      index = int(index) - 1    # user enters the number they need and it will count back
      if 0 <= index < len(students):   # ensures user has entered a value greater than or equal to 0 and less than the list length
        selected_student = students[index]   #selectes the students from the indicated index & assigned the variable
        category = input(f"Student {index} is {selected_student}. What would you like to know? ")   # indicate which student was chosen
        if category == "hometown":
          print(f"{selected_student['name']} is from {selected_student['hometown']}")
        elif category == "favorite food":
          print(f"{selected_student['name']}'s favorite food is {selected_student['favorite food']}")
        else:
          print("Please enter a valid category.")
  elif option == "quit":
    break
  else:
    print("Invalid option. Please enter add, view, or quit ")