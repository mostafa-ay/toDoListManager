print("Hello this is your to-do list manager","\033[33m", end=".")
print()
toDoList = []
def printList():
  print ()
  for item in toDoList:
    print(item)
while True:
  print()
  reply = input ("do you want to remove, add or view your to do list?")
  if reply == "view":
    printList()
  elif reply == "add":
    item = input("what do you want to add?")
    toDoList.append(item)
    printList()
  elif reply == "remove":
    item = input("what do you want to remove")
    if item in toDoList:
      toDoList.remove(item)
      printList()
    else:
      print(f"{item} was not in the list")
    printList()