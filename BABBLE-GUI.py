from ast import main
from cProfile import label, run

from email import charset
from operator import truediv


import tkinter as tk
from tkinter.ttk import Button
from typing import ItemsView, final



def babbler():
    import random








    horrified=[" witness death ", " witness murder", " get aids ", " injured ", " witness crime ", " see a ghost ", " got assaulted ", " saw a car accident "]
    distressed=[" test ", " exam ", " financial struggles ", " being harassed ", " mental illness ", " testicular torsion "]
    angry=[" violent altercation ", " verbal altercation ", " victimized ", " wronged ", " misguided anger "]
    embarassed=[" wrong tone ", " bad social skills ", " argument ", " publicly shamed ", " cancelled "]
    aggressive=[" racist rant ", " self hatred ", " work anger ", " school anger ", " video game anger "]
    tired=[" stayed up all night ", " took medication ", " sick ", " drugs ", " no reason ", " aids related complications "]

    emotions = ["horrified", "distressed", "angry", "embarassed", "aggressive", "tired"]

    selectedemotion = random.choice(emotions)

    if selectedemotion == "horrified":
        finalemotion = random.choice(horrified)
    elif selectedemotion == "distressed":
        finalemotion = random.choice(distressed)
    elif selectedemotion == "angry":
        finalemotion = random.choice(angry)
    elif selectedemotion == "embarassed":
        finalemotion = random.choice(embarassed)
    elif selectedemotion == "aggressive":
        finalemotion = random.choice(aggressive)
    elif selectedemotion == "tired":
        finalemotion = random.choice(tired)





    government_worker=[" president ", " CIA Agent ", " CPS caseworker ", " secretary ", " FED governer ", " campagin manager ", " prime minister "]
    unemployeed=[" stay at home mom ", " full time student ", " stay at home dad "]
    sex_worker=[" onlyfans girl ", " prostitute ", " high class escort ", " porn star "] 
    crimminal=[" meth dealer ", " weed dealer ", " mob boss ", " street gang member ", " human trafficker ", " registered sex offender ", " hitman ", " murderer ", " serial killer ", " pirated movies ", " dark web administrator ", " Ku Klux Klan member "]
    law_enforcement=[" DEA agent ", " police officer ", " FBI agent ", " security guard ", " mall cop ", " game warden ", " prison guard ", " health inspecter ", " ESRB reviewer ", " SEC worker "]
    medical_proffessional=[" gynecologist ", " abortionist ", " vet ", " dentist ", " orthodontist ", " pediatrist ", " pediatrition ", " psychologist "]
    entertainer=[" twitch streamer ", " youtuber ", " lol cow ", " singer ", " rapper ", " dubstep DJ ", " e-girl ", " instagram dog account owner ", " social media activist ", " tutorial maker ", " stock guru ", " crypto guru ", " animal trainer ", " e-sports player ", " tik-tok influencer ", " fashion influencer ", " instagram ass models"]
    religious_expert=["priest", "pastor", "preacher", "televangalist", "scientologist"]
    wage_slave=[" amazon worker ", "tesla_worker", "mcdonalds_worker", "retail_worker", "walmart_employee", "animator", "artist"]
    non_profit=["animal_rescue", "rehab_worker"]
    tech_bro = [ "google worker ", " Microsoft Developer ", " crypto-currency Influencer", " Web developer", " wordpress website developer ", " AOL Employee ", " start-up CEO " ]
    degenerate = [" drop-shipper ", " Real estate trainers "]


    occupations = ["government worker", "unemployeed" ,"sex worker", "crimminal", "law enforcement", "medical proffessional", "entertainer", "religious_expert", "wage slave", "non profit" ,"tech bro", "degenerate"]


    selectedoccupation = random.choice(occupations)



    if selectedoccupation == "government worker":
        occupation = random.choice(government_worker)
    elif selectedoccupation == "unemployeed":
        occupation = random.choice(unemployeed)
    elif selectedoccupation == "sex worker":
        occupation = random.choice(sex_worker)
    elif selectedoccupation == "crimminal":
        occupation = random.choice(crimminal)
    elif selectedoccupation == "law enforcement":
        occupation = random.choice
    elif selectedoccupation == "medical proffessional":
        occupation = random.choice(medical_proffessional)  
    elif selectedoccupation == "entertainer":
        occupation = random.choice(entertainer)
    elif selectedoccupation == "religious_expert":
        occupation = random.choice(religious_expert)
    elif selectedoccupation == "wage slave":
        occupation = random.choice(wage_slave)
    elif selectedoccupation == "non profit":
        occupation = random.choice(non_profit)
    elif selectedoccupation == "tech bro":
        occupation = random.choice(tech_bro)
    elif selectedoccupation == "degenerate":
        occupation = random.choice(degenerate)




    if selectedoccupation == government_worker:
        finaloccupation = random.choice(government_worker)
    elif selectedoccupation == unemployeed:
        finaloccupation = random.choice(unemployeed)
    elif selectedoccupation == sex_worker:
        finaloccupation = random.choice(sex_worker)
    elif selectedoccupation == crimminal:
        finaloccupation = random.choice
    elif selectedoccupation == law_enforcement:
        finaloccupation = random.choice(law_enforcement)
    elif selectedoccupation == medical_proffessional:
        finaloccupation = random.choice(medical_proffessional)
    elif selectedoccupation == entertainer:
        finaloccupation = random.choice(entertainer)
    elif selectedoccupation == religious_expert:
        finaloccupation = random.choice(religious_expert)
    elif selectedoccupation == wage_slave:
        finaloccupation = random.choice(wage_slave)
    elif selectedoccupation == non_profit:
        finaloccupation = random.choice(non_profit)
    elif selectedoccupation == tech_bro:
        finaloccupation = random.choice(tech_bro)
    elif selectedoccupation == degenerate:
        finaloccupation = random.choice(degenerate)





    outdoors=[" a park ", " a mountian ", " a desert ", " camping "]
    residential=["apartment", "house", "mansion", "condo", "minimalist_house", "tiny_home"]
    commercial=[" department store", " corprate office ", " movie set "]
    industrial=[" airport ", " manufacturing plant ", " water treatment facility "]
    traveling=[" a plane ", " unknown location ", " a car ", " a train "]
    institutional=[" hospital ", " psychiatric ward ", " hospice facility ", " asylum ", " drug rehab "]
    government_building=[" national capital ", " pentagon ", " State capital ", " city hall "]
    educational_institution=[" elementary school ", " secondary school ", " high school", "prep school", "private_school", "college", "university"]

    settings = [outdoors,residential,commercial,industrial,traveling,institutional,government_building,educational_institution]

    selectedsetting = random.choice(settings)

    if selectedsetting == outdoors:
        finalsetting = random.choice(outdoors)
    elif selectedsetting == residential:
        finalsetting = random.choice(residential)
    elif selectedsetting == commercial:
        finalsetting = random.choice(commercial)
    elif selectedsetting == industrial:
        finalsetting = random.choice(industrial)
    elif selectedsetting == traveling:
        finalsetting = random.choice(traveling)
    elif selectedsetting == institutional:
        finalsetting = random.choice(institutional)
    elif selectedsetting == government_building:
        finalsetting = random.choice(government_building)
    elif selectedsetting == educational_institution:
        finalsetting = random.choice(educational_institution)

    w = "write a story from the perspective of a/n "
    f = " who feels "
    b = " because of "
    m = "make the story take place in"
    final = print(w + occupation + f + selectedemotion + b + finalemotion + m + finalsetting)


root = tk.Tk()


root.geometry("400x400")
root.title("BABBLE PROMPTER")




label = tk.Label(root, text="Babble Prompter", font=("Arial", 20))

run_babble = tk.Button(root,text="Generate", command = babbler, font=("Arial", 15))
outputer = tk.Text(root, height=10, width=30, font=("Arial", 15))





  









label.pack()

    
run_babble.pack()
outputer.pack()
run_babble.pack()








root.mainloop()
