def main():
    time = 0
    passage_of_time = 0
    clock = 24
    alarm = 0

    while True:
        try:
            time = int(input('What time is it (24-clock): '))
            passage_of_time = int(input('How long until alarm goes off: '))
            
            if time < 0 or time > 23:
                raise ValueError('Entry must be between 0-23')

            if passage_of_time < 0:
                raise ValueError('Entry must be 0 or greater.')

            alarm = (time + passage_of_time) % clock
            break
        except ValueError:
            print('All entries must be whole numbers.')

    print('The alarm will go off at {}.'.format(alarm))



if __name__=='__main__':main()
