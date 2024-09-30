while True:
    line = input("Please Enter Your String: ")
    
    if line in ["quit", "q", "Quit"]:
        break
    
    reverse = line[::-1]
    
    print("Reversed:", reverse)

