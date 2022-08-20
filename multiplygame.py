#multiplication quiz
import random,time
import pyinputplus as pyip

while True:
    gamemode = pyip.inputNum('Game mode (1 or 2):\n 1. 10s countdown \n 2. 10 questions \n 3. Exit \n')   
    """ask user what game mode they want to play
    game 1 selection, 20s timer starts and questions are answered rapidly. When time.time() gets to current time + 20 (initiated before the loop), the questions stop. 
    game 2, asks 10 multiplication questions randomly from 0-14 and stores number of correct answers before giving a time and % """
    if gamemode == 2:
        qs = 10
        correct = 0
        start = time.time()
        for questionNum in range(qs):
            a = random.randint(0,14)
            b = random.randint(0,14)
            answer = pyip.inputNum(f'{questionNum}) {a} x {b} = ', blank=True)
            if answer == a*b:
                print('Correct, well done!')
                correct += 1
                continue
            else:
                print('Incorrect.')
                continue
        end = time.time()
        perc = correct/0.1
        time_t = int(end-start)
        end = input(f'{correct} correct answers ({perc}%) in {time_t}s. \nType quit to exit. \nPress enter to try again.\n')
        if end == "quit":
            break

    elif gamemode == 1:
        correct = 0
        questionNum = 0
        end_time = time.time() + 20
        print('20 second timer starts now, enter ""quit"" to exit')
        while time.time() < end_time:
            questionNum +=1
            a = random.randint(0,14)
            b = random.randint(0,14)
            answer = pyip.inputNum(f'{questionNum}) {a} x {b} = ', blank=True, allowRegexes=r'quit')
            #pyip module allows for input validation and regex of quit allows user to write quit to end loop
            if answer == 'quit':
                break
            elif answer == a*b:
                print('Correct well done!')
                correct += 1
                continue
            else:
                print('Incorrect!')
                continue
        perc = correct/0.1
        end = input(f'{correct} correct answers ({perc}%). \nType quit to exit. \nPress enter to try again\n')
        if end == "quit":
            break 

    elif gamemode == 3:
        print('Exiting...')
        quit()
        
