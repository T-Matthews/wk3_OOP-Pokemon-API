import requests as r
import pprint
pp = pprint.PrettyPrinter(depth=4)

"""
Class "region" is not used in this game. I would like to come back and finish this, 
but for now the pokedex option is the only fleshed out one, the battle took FOREVER to finish. 
It is still vague as hell as to why someone wins, but its working i think.
"""

class region():
    def __init__(self):
        pass
    
    def select_region(self):
        pass
    def change_region(self):
        pass
    
    def check_gyms(self):
#does your pokedex have effective pokemon to fight the gym leaders in this region?
        pass



class pokedex():
    def __init__(self,region):
        self.mydex = {}
        #Evolution call used to store url needed for evolution API call later 
        #       on, figured I should store it to prevent a future call.
        self.evolution_call = {}
        self.region = region

#Nearly all of the options on the 'showscreen' require 1 pokemon. 
    def showscreen(self):
        if len(self.mydex) == 0:
            print('You have no Pokemon! Lets add one.')
            myPokedex.add_pokemon()
        while True:
            selection = int(input('\n Which of the following would you like to do?\n\t'+
                            '[1]Add a Pokemon\n\t[2]Remove a Pokemon\n\t[3]View '+
                            'Pokedex\n\t[4]Evolve Pokemon in your Pokedex\n\t[5]Battle\n\t[6]Quit\n\n'))
            if selection == 1:
                myPokedex.add_pokemon()#Complete
            elif selection == 2 and len(self.mydex)>0:
                myPokedex.rem_pokemon() #Complete
            elif selection == 3 and len(self.mydex)>0:
                myPokedex.view_pokedex()#Complete
            elif selection == 4 and len(self.mydex)>0:
                myPokedex.evolve_pokemon()#Complete
            elif selection == 5:
                if len(self.mydex)>1:
                    myPokedex.battle()#Complete
                else:
                    print('You need at least 2 pokemon to battle!')
            elif selection == 6:
                print('Gotcha! Lets go back to the title menu!')
                break
                
                
            elif selection ==2 or selection ==3 or selection ==4:
                print('You need at least one pokemon to do this! Go add a pokemon!')
            else:
                print('You need 2 or more pokemon to let them battle!')
        ui.run()


    def add_pokemon(self):
        while True:
            pokeadd = input('What pokemon would you like to add? This can be by name, or by number.\n\t')
            data = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokeadd.lower()}/')
            if data.status_code != 200:
                print('There was an error fetching this data. Please verify the name/ID number of your pokemon.\n')
                break
            else:
                data = data.json()
                new_dict = {
                    'Name':data['name'],
                    'height':data['height'],
                    'id':data['id'],
                    'moves':[x['ability']['name'] for x in data['abilities']],
                    'types':[x['type']['name'] for x in data['types']],
                    'hit-points':data['stats'][0]['base_stat'],
                    'attack' : data['stats'][1]['base_stat']
                }
                #following dictionary only to retain url needed for evolution later on.
                self.evolution_call[data['name'].title()]=data['species']['url']

                if new_dict['Name'].title() in self.mydex:
                    print('That pokemon is already in your pokedex!')
                else:
                    self.mydex[new_dict['Name'].title()] = new_dict
                    print(f'Excellent! {new_dict["Name"].title()} has been added to your Pokedex!')
                    break
        myPokedex.showscreen()        


    def rem_pokemon(self):
        while True:
            if len(self.mydex) ==0:
                print("You do not have any Pokemon to remove!")
                break
            else:
                print('CURRENT POKEMON:')
                for k in self.mydex:
                    print ("\t\t"+k)
                rem_po = input("\nWhich Pokemon would you like to remove from your Pokedex?\n(If you do not wish to remove, input 'none'.\n\t").title()
                if rem_po in self.mydex:
                    del self.mydex[rem_po]
                    del self.evolution_call[rem_po]
                    print(f'Sounds great, {rem_po.title()} has been removed from your Pokedex.')
                elif rem_po.lower() == 'none':
                    break
                else:
                    print('That Pokemon is not in your Pokedex!')

        myPokedex.showscreen()


    def view_pokedex(self):
        statsprint = int(input('\tDo you want a: \n\t[1]full stats printout \n\t[2]names list\n\t'))
        if statsprint ==1:
            pp.pprint(self.mydex)
        elif statsprint == 2:
            print('----- Your Pokemon -----')
            for k in self.mydex:
                print(f'\t{k.title()}')
        myPokedex.showscreen()


    def evolve_pokemon(self):
        
        while True:
            print('---CURRENT POKEMON---')
            for k in self.mydex:
                print(f'\t{k.title()}')
            evolve_p = input('Which of your pokemon would you like to evolve?\n\t')
            #Way too much code for the eevee edge case
            if evolve_p.title() in self.mydex and evolve_p.lower() == 'eevee':
                print('Thought you\'d trick me up with an extreme edge '+
                'case by evolving an Eevee?? Tough luck! Which evolution would you like?')
                eevee_evo = input('\n\t[1]Vaporeon\n\t[2]Jolteon\n\t[3]Flareon'+
                                    '\n\t[4]Espeon\n\t[5]Umbreon\n\t[6]Leafeon\n\t[7]Glaceon\n')
                if int(eevee_evo) == 1 or eevee_evo.title() == 'Vaporeon':
                    eevee_evo = 'Vaporeon'
                elif int(eevee_evo) ==2 or eevee_evo.title() == 'Jolteon':
                    eevee_evo = 'Jolteon'
                elif int(eevee_evo) ==3 or eevee_evo.title() == 'Flareon':
                    eevee_evo = 'Flareon'
                elif int(eevee_evo) ==4 or eevee_evo.title() == 'Espeon':
                    eevee_evo = 'Espeon'
                elif int(eevee_evo) ==5 or eevee_evo.title() == 'Umbreon':
                    eevee_evo = 'Umbreon'
                elif int(eevee_evo) ==6 or eevee_evo.title() == 'Leafeon':
                    eevee_evo = 'Leafeon'
                elif int(eevee_evo) ==7 or eevee_evo.title() == 'Glaceon':
                    eevee_evo = 'Glaceon'
                else:
                    print('Sorry! Thats not an evolution of Eevee!')
                    break
                    
                del self.mydex['Eevee']
                eevee_data = r.get(f'https://pokeapi.co/api/v2/pokemon/{eevee_evo.lower()}/').json()
                self.mydex[eevee_evo.title()] ={
                                        'Name': eevee_data['name'],
                                        'height':eevee_data['height'],
                                        'id':eevee_data['id'],
                                        'moves':[x['ability']['name'] for x in eevee_data['abilities']],
                                        'types':[x['type']['name'] for x in eevee_data['types']],
                                        'hit-points':eevee_data['stats'][0]['base_stat'],
                                        'attack' : eevee_data['stats'][1]['base_stat']
                }
                print(f'Congrats! Your Eevee evolved into a {eevee_evo}!')
                break

            elif evolve_p.title() in self.mydex:
                #From pokemon data, is a convoluted path to determine evolution path. 
                # Pokemon -> Species Data -> Evolution Chain Data, converted below.
                #Does not currently function for branching evolution pats
                species_data = r.get(self.evolution_call[evolve_p.title()]).json()
                evo_chain = r.get(species_data['evolution_chain']['url']).json()
                if evo_chain['chain']['species']['name'].title() == evolve_p.title() and evo_chain['chain']['evolves_to'][0]['species']['name']:
                    evo_name = (evo_chain['chain']['evolves_to'][0]['species']['name'])
                elif evo_chain['chain']['evolves_to'][0]['species']['name'].title() == evolve_p.title() and evo_chain['chain']['evolves_to'][0]['evolves_to'][0]['species']['name']:
                    evo_name = (evo_chain['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'])
                else:
                    print(f'Your {evolve_p.title()} cannot evolve further!')
                    break

                del self.mydex[evolve_p.title()]
                del self.evolution_call[evolve_p.title()]
                evo_data = r.get(f'https://pokeapi.co/api/v2/pokemon/{evo_name.lower()}/').json()
                self.mydex[evo_name.title()] ={
                                        'Name': evo_data['name'],
                                        'height':evo_data['height'],
                                        'id':evo_data['id'],
                                        'moves':[x['ability']['name'] for x in evo_data['abilities']],
                                        'types':[x['type']['name'] for x in evo_data['types']],
                                        'hit-points':evo_data['stats'][0]['base_stat'],
                                        'attack' : evo_data['stats'][1]['base_stat']
                }
                self.evolution_call[evo_data['name'].title()]=evo_data['species']['url']
                print(f'Congrats! Your {evolve_p.title()} evolved into a {evo_name.title()}!')
                break
            else:
                print('That didnt work! Check your spelling of that pokemon!')
                break
            
        myPokedex.showscreen()

    """
    My battling involves all pokemon in your pokedex. The rules of battle are as follows:
    1) +1 point given to a pokemon for a type advantage on any other pokemon
    2) -1 point for a 'has no effect' attack. 
            *Might remove this if ghosts just always win due to avoiding physical attacks.* 
    3) Tie-breaker arbitrarily goes to pokemon with first name in the alphabet.
    """       
   
    def battle(self):
        battlebook = {}
        for k in self.mydex:
            battlebook[k] = {
                    'tiebreaker': (self.mydex[k]['hit-points']+self.mydex[k]['attack']+self.mydex[k]['height']),
                    'types':self.mydex[k]['types'],
                    'points':0
        }
        total_types_in_battle = []
        types_in_battle = set()
        for i in battlebook:
            total_types_in_battle.extend(battlebook[i]['types'])
            types_in_battle.update(battlebook[i]['types'])
        type_urls = {}
        type_comp = {}
        type_data = r.get(f'https://pokeapi.co/api/v2/type/').json()
        for i in type_data['results']:
            if i['name'] in types_in_battle:
                type_urls[i['name']] = i['url']
            
        for k in type_urls:
            str = []
            wk = []  
            temp_data = r.get(type_urls[k]).json()
            
            for v in temp_data['damage_relations']['double_damage_to']: str.append(v['name'])
            for v in temp_data['damage_relations']['no_damage_to']: wk.append(v['name'])

            type_comp[k] = {'str':str,
                            'wk':wk    }
                    
                    
        for i in battlebook:
            my_type = battlebook[i]['types']
            points = 0
            for j in my_type:
                mystrengths = type_comp[j]['str'] 
                myweak = type_comp[j]['wk'] 
                if j in mystrengths:
                    points -=1
                if j in myweak:
                    points+=1
                for k in total_types_in_battle:
                    if k in mystrengths:
                        points+=1
                    if k in myweak:
                        points-=1
            battlebook[i]['points']= points
        scorecard = {}
        for k in battlebook:
            scorecard[k]=battlebook[k]['points']
        print(scorecard)
        winner = max(scorecard,key = scorecard.get)

        loser = min(scorecard,key = scorecard.get)
        if len(self.mydex) == 2:
            print(f'You release your two pokemon to the grassy plains you find yourself in. '+
            f'A cool breeze drifts leaves lazily through the air. \n{loser.title()} and {winner.title()} '+
            'begin playing! It\'s the dreamy afternoon you have been waiting for. But, Pokemon play can '+
            f'swiftly \nbecome edgy. {loser.title()} starts to bite with menace. Before you can react, you '+
            f'see blood starting to pool nearest to {loser.title()}. \n{winner.title()} looks down on his '+
            'recently demolished foe, before looking at you and grinning, far to widely. You hastily return \n'+
            f'{winner.title()} to his pokeball, not wanting to imaging him setting sights on you, his captor.\n\n------- {winner.upper()} WINS!!! --------')
        else:
            print('You\'ve finally done it. Your whole life, you have been consumed by the desire to defeat all '+
            'the pokemon gyms this world has to offer, and it has yet \nto sink in that the task has been completed;'+ 
            'that the goal has been achieved. As you return home, you release the fearsome pokemon that you have\n '+
            'trained along the way. As you make your way through the outskirts of town, locals begin leaving residences '+
            'to cheer you on. What an accomplishment, not achieved \nsince the 15th century when the fabled "Ash Catchum" '+
            'accomplished the feat. As the cheers grow, your pokemon begin getting nervous.\n\n'+
            'Fighting is one thing, but cheering crowds is new for them. Children reach out to pet your pokemon. '+
            'But children should know better. These are still wild beasts at heart. \nAnd all of a sudden they reminded '+
            'everyone of that fact. Men, women, children, fled the scene as the building anxiety in your pokemon erupts \n'+
            'into a bloodbath the likes of which have not been seen in the Kanto region. \n\n'+
            'Your pokemon, in the melee begin attacking each other, not knowing friend from foe. You run, not knowing '+
            'weather to turn yourself in, or try to protect the few \nremaining civilians. When you return, you see only '+
            f'one pokemon remaining, strongest of them all standing atop the pile. {winner.title()} stands above all those\n'+
            f'that had fallen, a testiment to her power as your strongest pokemon.\n\n------- {winner.upper()} WINS!!! --------')
        myPokedex.showscreen()


class UI():
    def __init__(self,Pokedex,Region):
        self.Pokedex = Pokedex
        self.Region = Region
    def run(self):
        flag=True
        while flag ==True:
            menu1 = (input('\t------- WELCOME -------\n\tWelcome! '+
                        'How would you like to proceed?\n\t'+
                        '[1]Enter a Region\n\t[2]Go to your pokedex\n\t'+
                        '[3]More info Please!\n\t[4]Quit\n\t'))
            if int(menu1) == 1:
                print('Sorry! Regions is still under development.')
            elif int(menu1) == 2:
                myPokedex.showscreen()
            elif int(menu1) == 3:
                print("Welcome to the world of Pokemon! The world has multiple"+
                    " regions, each region containing a unique set of pokemon. By "+
                    "choosing option 1, you can reduce the number of pokemon to "+
                    "only include those from the selected regions.")
            elif int(menu1) ==4:
                print("Good luck catching them all! See you later!")
                flag = False
            else:
                print("Please input a valid number from 1-4.")


mypokedex = {}          
myregion = region()
myPokedex = pokedex(myregion)
ui = UI(myPokedex,myregion)

ui.run()

