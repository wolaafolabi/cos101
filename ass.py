def a():
 displacement = float(input("what is your displacement?"))
 time = float(input("what is your time?"))
 velocity= displacement/time
 print(velocity)

def b():
 distance = float(input("what is your distance?"))
 time = float(input("what is your time?"))
 speed= distance/time
 print(speed)

def c():
 mass = float(input("what is your mass?"))
 acceleration = float(input("what is your acceleration?"))
 force= mass*acceleration
 print(force)

def d():
 speed = float(input("what is your speed?"))
 time = float(input("what is your time?"))
 distance= speed*time
 print(distance)

def e():
 velocity = float(input("what is your velocity?"))
 time= float(input("what is your time?"))
 displacement= velocity*time
 print(displacement)

def main():
    choice = input("what do you want to do?")
    if choice == "a":
      a()
    elif choice == "b":
      b()
    elif choice =="c":
      c()
    elif choice == "d":
      d()
    elif choice == "e":
      e()
    else:
     input("invalid input")

if __name__ == "__main__":
 main()