#lives variables 
start_lives = 3
current_lives = start_lives

#answer variables 
answer_yes = ["Yes", "YEs", "YeS", "YES", "yes", "y"]
answer_no = ["No", "NO", "no", "n"]
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]
answer_d = ["D", "d"]
valid_answers = ["A", "a", "B", "b", "C", "c", "D", "d"] 


"""
Return a number of lives when the player choose one option at each stage
a number of lives decreases each time when the player choose wrong option
>>> Given prompt: A, B, C, D
choose 'wrong'
False
"""
#stage dictionaries
stage0_dict = {
    'prompt': "On the way to your grandmother's house you get lost in the forest. What do you do? \n", 
    'A': "A. continue on the same path \n",
    'B': "B. stay there and eat your grandmother's food \n",
    'C': "C. go right \n",
    'D': "D. go left \n",
    'death': "The wolf came along and ate you when you were busy stealing your grandmother's food. \n",
    'wrong': answer_b
}

stage1_dict = {
    'prompt': "While continuing in the forest you hear a noise to your left. What do you do? \n",
    'A': "A. go right away from the noise \n",
    'B': "B. walk faster \n",
    'C': "C. go left and investigate the noise \n",
    'D': "D. continue on the same path and be alert \n",
    'death': "You get distracted by a squirrel that made the noise and the wolf eats you for making bad decisions. \n",
    'wrong': answer_c
}

stage2_dict = {
    'prompt': "While walking you come across a wolf in the forest. You... \n",
    'A': "A. run away \n",
    'B': "B. give the wolf your grandmothers food and then run away \n",
    'C': "C. throw a stick for the wolf to fetch and then run away \n",
    'D': "D. do nothing \n",
    'death': "The wolf eats you for being too slow. \n",
    'wrong': answer_d
}

stage3_dict = {
    'prompt': "You arrive at your grandmother's house. However, your grandmother looks a little different. What do you do? \n",
    'A': "A. assume she's just getting old and saying nothing \n",
    'B': "B. scream for help and run away \n",
    'C': "C. run away \n",
    'D': "D. ask what's wrong and refuse to come inside \n",
    'death': "Your grandmother takes her hat off to reveal she's the wolf and eats you for making bad decisions. \n",
    'wrong': answer_a
}

stage4_dict = {
    'prompt': "You see a hunter in the forest while running away or refusing to go inside. You... \n",
    'A': "A. ask him to help you \n",
    'B': "B. hide behind him \n",
    'C': "C. ignore him \n",
    'D': "D. offer him food in exchange for help \n",
    'death': "The wolf catches up to you and eats you for making bad decisions. \n",
    'wrong': answer_c  
}

stage5_dict = {
    'prompt': "The hunter shoots the wolf and offers to escort you back home. What do you do? \n",
    'A': "A. thank him for his help and accept the escort \n",
    'B': "B. accept the escort \n",
    'C': "C. give him the rest of your grandmother's food as a thank you and accept the escort  \n",
    'D': "D. deny the escort and try to find your way home by yourself \n",
    'death': "You get lost in the woods again and catch hyperthermia and die. \n",
    'wrong': answer_d   
}

stage_idx = 0
stages = [stage0_dict, stage1_dict, stage2_dict, stage3_dict, stage4_dict, stage5_dict]


def lose_life():
    global current_lives
    current_lives = current_lives - 1
    

def wrong_answer_prompt(stage_dict):
    wrong_answer = stage_dict.get('wrong')
    global death_valid_answers
    global new_answer
    #remove the wrong answer from the prompt message
    if wrong_answer == answer_a: 
        new_answer = input(str(stage_dict.get('prompt')) + str(stage_dict.get('B')) + str(stage_dict.get('C')) + str(stage_dict.get('D'))) 
        death_valid_answers = ["B", "b", "C", "c", "D", "d"] 
    elif wrong_answer == answer_b: 
        new_answer = input(str(stage_dict.get('prompt')) + str(stage_dict.get('A')) + str(stage_dict.get('C')) + str(stage_dict.get('D')))
        death_valid_answers = ["A", "a", "C", "c", "D", "d"] 
    elif wrong_answer == answer_c: 
        new_answer = input(str(stage_dict.get('prompt')) + str(stage_dict.get('A')) + str(stage_dict.get('B')) + str(stage_dict.get('D'))) 
        death_valid_answers = ["A", "a", "B", "b", "D", "d"] 
    else: 
        new_answer = input(str(stage_dict.get('prompt')) + str(stage_dict.get('A')) + str(stage_dict.get('B')) + str(stage_dict.get('C'))) 
        death_valid_answers = ["A", "a", "B", "b", "C", "c"] 
    return death_valid_answers and new_answer

def game(stage_dict):
    wrong_answer = stage_dict.get('wrong')
    global current_lives 
    global stage_idx
    answer = input(str(stage_dict.get('prompt')) + str(stage_dict.get('A')) + str(stage_dict.get('B')) + str(stage_dict.get('C')) + str(stage_dict.get('D')))
    #end the game if the level index is out of range
    if stage_idx == 5:
        print("You made it to the end with " + str(current_lives) + " lives! Congratulations! \n")
        stage_idx = 0
        current_lives = 3        
        play() 
    else:
        if current_lives == 0:
            #end the game is lives are 0 
            print("Sorry, you're dead for real this time. Start again.")
            #reset the stage index and lives 
            stage_idx = 0
            current_lives = 3
            #repeat the function to ask if you want to play
            play()
            
            """
            if the player chooses one of wrong_answer in dictionaries
            - repeat the prompt without giving wrong_answer the player chose before
            - loose life
            - stage_idx must be the same
            
            else:
            - stage_idx increases by 1
            - life remains the same
            """
                        
        else:
            if answer in valid_answers:
                if answer in wrong_answer:
                    #decrease lives if the wrong answer is given
                    lose_life()  
                    #do not give the player another chance to answer if lives = 0 
                    if current_lives == 0:
                        #end the game is lives are 0 
                        print("Sorry, you're dead for real this time. Start again.")
                        #reset the stage index and lives 
                        stage_idx = 0
                        current_lives = 3
                        #repeat the function to ask if you want to play
                        play()                        
                    else:
                        #give the player another chance to answer
                        print("Oh no! " + stage_dict.get('death') + " Try again. You have " + str(current_lives) + " more lives.")
                        wrong_answer_prompt(stages[stage_idx])
                        #check that the answer is valid with the new options
                        while new_answer not in death_valid_answers: 
                            print("Opps! Sorry that wasn't a valid answer, try again!")
                            wrong_answer_prompt(stages[stage_idx]) 
                        #increase stage index for the next level
                        stage_idx += 1
                        #print the updated lives count
                        print("Lives: " + str(current_lives))
                        #repeat the function for the next level 
                        game(stages[stage_idx])                            
                else:
                    #print current lives count
                    print("Lives: " + str(current_lives))
                    #increase stage index for the next level
                    stage_idx += 1
                    #repeat the function for the next level
                    game(stages[stage_idx])
            else: 
                print("Opps! Sorry that wasn't a valid answer, try again!")
                game(stages[stage_idx])


def play(): 
    global stage_idx 
    answer = input("Would you like to play a game? Yes/No \n")
    if answer in answer_yes: 
        stage_idx = 0
        game(stages[stage_idx])
    elif answer in answer_no:
        print("Okay then...")
    else: 
        print("Sorry, we didn't understand that.")
        play()


#the global code
print("Lives: " + str(start_lives))
play()