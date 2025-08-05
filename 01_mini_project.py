import random

print("Welcome to guessing game !")

start = int(input("Please enter starting number:"))

end = int(input("Please enter ending number:"))

runm = random.randint(start,end)

attempt =0

while True:
    attempt =attempt+1
    print(runm)
    g = int(input("Enter your guess"))    
        
    if g<start or g>end:        
        print(f"guess under {start} to {end}",attempt)

    elif g < runm:
        print("Guess is  low,attempt:",attempt)        

     
    elif g>runm:        
        print("Guess is  Hight,attempt:",attempt)        

    else:        
        print("You WIN : ",attempt)
                
    
