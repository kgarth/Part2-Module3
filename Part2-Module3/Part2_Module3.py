def main():
    time = 0 # Declare variable to capture current time
    passage_of_time = 0 # Declare variable to capture elapsed time
    clock = 24 # Set the variable for type of clock
    alarm = 0 # Declare variable to hold the result

    while True: # Keep looping until time entry is within specifications
        try:
            time = int(input('What time is it (24-clock): ')) 
            
            if time < 0 or time > 23: 
                raise ValueError() 
            
            while True: # Inner loop to check if the amount of elasped time is within specifications
                try:    
                    passage_of_time = int(input('How long until alarm goes off: '))
            
                    if passage_of_time < 0:
                        raise ValueError()
                    break

                except ValueError:
                    print('Hours entered must be positive whole number.')
            
            alarm = (time + passage_of_time) % clock # Calculate when the alarm goes off
            break

        except ValueError:
            print('Time entry must be a positive whole number between 0-23.')
            
        
        

    print('The alarm will go off at {} hundred hours.'.format(alarm)) # Print the results



if __name__=='__main__':main()
