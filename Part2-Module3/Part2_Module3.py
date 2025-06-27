def main():
    time = 0
    passage_of_time = 0
    clock = 24
    alarm = 0

    while True:
        try:
            time = int(input('What time is it (24-clock): '))
            
            if time < 0 or time > 23:
                raise ValueError()

        except ValueError:
            print('Time entry must be a positive whole number between 0-23.')
            
        try:    
            passage_of_time = int(input('How long until alarm goes off: '))
            
            if passage_of_time < 0:
                raise ValueError()

        except ValueError:
            print('Hours entered must be positive whole number.')

        alarm = (time + passage_of_time) % clock
        break
        

    print('The alarm will go off at {}.'.format(alarm))



if __name__=='__main__':main()
