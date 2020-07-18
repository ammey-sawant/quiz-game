import time
Q = 1
score = 0
print("Welcome the quiz game .")
time.sleep(2)
sl = input("please select these levels : level 1 , level 2 , level 3 :")
if sl == "1" :
    print("1) English")
    print("2) Math")
    print("3) Histroy")
    print("4) Science") 
    ss = int(input("Please select these subject : 1) English2) Math3) Histroy 4) Science"))
    if ss == 1 :
        while Q <= 4 :
            if Q == 1 :
                print("_____water is _____elixir of life but ______water of this pond is poisonous.")
                ques = input("ans :")
                if "the,the,the" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
            if Q == 2 :       
                print("I am one year older than ____ (he/him).")
                ques = input("ans :")
                if "him" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
            Q = Q + 1
    if ss == 2 :
        while Q == 1 :
            if Q == 1 :
                print("How much is 2 + 2?")
                ques = input("ans :")
                if "4" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
                   
            if Q == 2 :
                print("177 + 378")
                ques = input("ans :")
                if "555" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)                    
            Q = Q + 1
            
    if ss == 3 :
        while Q <= 5 :
            if Q == 1 :
                print("1. Who is the founder of Maratha empire ?")
                ques = input("ans :")
                if ques == 'Chatrappti Shivaji Maharaj' or ques == 'Shivaji Maharaj'  :
                    print("correct ans")
                else :
                    print("Wrong ans")
                    
            if Q == 2 :
                print("172 -129")
                ques = input("ans :")
                if ques == '43' :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
                    
            if Q == 3 :
                print("27*30")
                ques = input("ans :")
                if ques == '810' :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
                    
            Q = Q + 1
            
    if ss == 4 :
        while Q <= 5 :
            if Q == 1 :
                print("What part of plant conducts photosynthesis ?")
                ques = input("ans :")
                if ques == 'Leaf' :
                    print("correct ans")
                else :
                    print("Wrong ans")
                    
            if Q == 2 :
                print("Where does our food collect after we chew swallow it ?")
                ques = input("ans :")
                if ques == 'It moves down your esophagus. Next, it enters your stomach. From your stomach, it moves down into your small intestine.' :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
                    
            if Q == 3 :
                print("Why is the sky blue ?")
                ques = input("ans :")
                if ques == 'The is surrounded by an atmosphere .' :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
            if Q == 4 :
                print("How far is the sun ?")
                ques = input("ans :")
                if "93 millon miles ." in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score) 
            if Q == 5 :
                print("How airplanes fly ?")
                ques = input("ans :")
                if "The different forces make flight possible" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)             
            Q = Q + 1
            
if sl == "2" :
    print("1) English")
    print("2) Math")
    print("3) Histroy")
    print("4) Science") 
    ss = int(input("Please select these subject : 1) English2) Math3) Histroy 4) Science"))
    if ss == 1 :
        print("Error : Question for English , level 2 are not available .")
    if ss == 2 :
        print("Error : Question for Maths , level 2 are not available .")
    if ss == 3 :
        while Q <= 5 :
            if Q == 1 :
                print("The 8th Century tripartite power struggle was among which of Following ?")
                ques = input("ans :")
                if ques == 'Chalukyas , Pallavas and Pandyas'   :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    
            if Q == 2 :
                print("Upanisads are books on :")
                print("Math")
                print("Science")
                print("Philosophy")
                ques = input("ans :")
                if ques == 'Philosophy' :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
                    
            if Q == 3 :
                print("In which language was Kesri , a newspaper started by Lokmanya tilak published ?")
                ques = input("ans :")
                if ques == 'मराठी' or ques == "Marathi" :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
            if Q == 4 :
                print("Do or Die was ome of the most powerful slogans of India`s freedom struggle , Who gave it ?")
                ques = input("ans :")
                if "Mahatma Gandhi" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score) 
            if Q == 5 :
                print("who founded the Deccan Education Society to impart teaching about India culture to India`s youth ?")
                ques = input("ans :")
                if "Lokmanya tilak" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score) 
                    
            Q = Q + 1
    if ss == 4 :
        while Q <= 1 :
            if Q == 1 :
                print("How rainbows are made?")
                ques = input("ans :")
                if ques == 'when lights hit the water droplets in air .'   :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("wrong ans")
                    print(score)
            Q = Q + 1                        
if sl == "3" :
    print("1) English")
    print("2) Math")
    print("3) Histroy")
    print("4) Science") 
    ss = int(input("Please select these subject :"))
    if ss == 1 :
        print("Error : Question for English , level 3 are not available .")
    if ss == 2 :
        print("Error : Question for Maths , level 3 are not available .")
    if ss == 3 :
        while Q <= 5 :
            if Q == 1 :
                print("Which among the following Kavya of Sanskrit, deal with court intrigues & access to power of Chandragupta Maurya  ?")
                print("1) Vishnu Guapta")
                print("2) Akbar")
                print("3) Mudrarakshasa")
                ques = input("ans :")
                if ques == 'Mudrarakshasa .'   :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    
            if Q == 2 :
                print("Which of the following is not correct :")
                print("1) Capital Maurya Empire - Pataliputra")
                print("2) Capital of the Videha kingdom - Mithila ")
                ques = input("ans :")
                if ques == 'Capital of the Videha kingdom - Mithila' :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
                    
            if Q == 3 :
                print("Which king start the organization of Kumbh fair at Allahabad ?")
                ques = input("ans :")
                if ques == 'Harshavardhana'  :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score)
            if Q == 4 :
                print("Who was the first Indian ruler who had territory outside India ?")
                ques = input("ans :")
                if "Kanishka" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score) 
            if Q == 5 :
                print("Who among the following was worshipped during Early Vedic Civilization ?")
                ques = input("ans :")
                if "Indra, Varuna and Surya" in ques :
                    print("correct ans")
                    score = score + 1
                    print(score)
                else :
                    print("Wrong ans")
                    print(score) 
                    
            Q = Q + 1    
            
        if ss == 4 :
            while Q <= 2 :
                if Q == 1 :
                    print("Who discovered neutron ?")
                    ques = input("ans :")
                    if ques == 'James chadwick':
                        print("correct ans")
                        score = score + 1
                        print(score)
                    else :
                        print("wrong ans")
                        print(score)    
                if Q == 2 :
                    print("Who discovered vaccine ?")
                    ques = input("ans :")
                    if ques == 'Edward jenner':
                        print("correct ans")
                        score = score + 1
                        print(score)
                    else :
                        print("wrong ans")
                        print(score)    
                        
                Q = Q + 1