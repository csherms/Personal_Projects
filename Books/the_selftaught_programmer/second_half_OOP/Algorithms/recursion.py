def bottles_of_beer(bob):
  """Prints 99 bottles of beer on the wall lyrics"""
  if bob < 1:
    print("No more bottles of beer on the wall, no more bottles of beer.")
    return
  tmp = bob
  bob -= 1
  print("""{} Bottles of beer on the wall! 
           {} Bottles of beer! Take one down, pass it around, 
           {} bottles of beer on the wall!""".format(tmp, tmp, bob))
  bottles_of_beer(bob)
  
bottles_of_beer(99)