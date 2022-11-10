x = input("Please, enter a month to see the season: \n")
if x in range(1, 2) or x in ("January", 12, "February", "December"):
    print("Winter")
elif x in range(3, 5) or x in ("March", "April","May"):
    print("Spring")
elif x in range(6, 8) or x in ("June", "July","August"):
    print("Summer")
elif x in range(9, 11) or x in ("September", "October","November"):
    print("Fall")
else:
  print("WTF?")