# Ben Hohnstedter
# Ich wollte dieses RPG-Game objektorientiert umsetzen.
# Da ich es in meinem Ausbildungsbetrieb durch den Umgang mit PHP so gelernt habe.
# -> Mit Online-Recherche und viel ausprobieren, wie man das im Python Kontext loest, habe ich es hinbekommen.
# Mir ist auch bewusst, dass man wahrscheinlich noch viel mehr anpassen und verbessern kann, ich bin aber erstmal froh, dass es ueberhaupt funktioniert.


class Player:
   def __init__(self):
       self._items = []
       self._current_room = 'Hall'


   #getter
   @property
   def items(self):
       return self._items


   @property
   def current_room(self):
       return self._current_room


   #setter
   def add_item(self, item):
       self._items += [item]


   def set_current_room(self, current_room):
       self._current_room = current_room


   #methods
   def show_status(self, dungeon):
       print('\n---------------------------')
       print('Status:')
       print('You are in the ' + self.current_room)
       print('Inventory : ' + str(self.items))
       if 'item' in dungeon.rooms[self.current_room]:
           print('You see a ' + dungeon.rooms[self.current_room]['item'])
       else:
           print('No item found!')
       print('---------------------------')


   def move(self, action, dungeon):
       if action[1] in dungeon.rooms[self.current_room]:
           self.set_current_room(dungeon.rooms[self.current_room][action[1]])
           print('\nYou entered: ' + self.current_room + '!')
       else:
           print('\nYou can\'t go that way!')
      
   def get_item(self, action, dungeon):
       if 'item' in dungeon.rooms[self.current_room] and action[1] in dungeon.rooms[self.current_room]['item']:
           self.add_item(action[1])
           print('\nYou got: ' + action[1] + '!')
           del dungeon.rooms[self.current_room]['item']
       else:
           print('\nYou can\'t get ' + action[1] + '!')
       return dungeon.rooms




class Dungeon:
   def __init__(self):
       self._rooms = {
           'Hall' : {
               'south' : 'Kitchen',
               'east' : 'Dining Room',
               'item' : 'key',
           },
           'Kitchen' : {
               'north' : 'Hall',
               'item' : 'monster',
           },
           'Dining Room' : {
               'west' : 'Hall',
               'south' : 'Garden',
               'item' : 'potion',
           },
           'Garden' : {
               'north' : 'Dining Room',
               'item' : 'treasure',
           },
       }


   #getter
   @property
   def rooms(self):
       return self._rooms
  
   #setter
   def set_rooms(self, rooms):
       self._rooms = rooms


class Game:
   def __init__(self, player, dungeon):
       self.player = player
       self.dungeon = dungeon


   def main(self):
       self.show_instructions()
       self.player.show_status(self.dungeon)
       self.show_commands()
       self.player_action()


   def show_instructions(self):
       #print main menu and the commands
       print('\nWelcome to  your own RPG Game\n=============================\n\nGet to the Garden with a key and a potion.\nAvoid the monsters!')


   def show_commands(self):
       print('\n---------------------------')
       print('Commands:\n- go [direction]\n- get [item]\n- show commands/status')
       print('---------------------------')


   def player_action(self):
       game_over = False
       while game_over == False:
           action = input('\nChoose your next action:\n---> ')
           if action != '':
               action = action.lower().split()
               match action[0]:
                   case 'exit':
                       game_over = True
                   case 'show':
                       if action[1] == 'commands':
                           self.show_commands()
                       elif action[1] == 'status':
                           self.player.show_status(self.dungeon)
                       else:
                           print('\nYou can\'t show that!')
                   case 'go':
                       self.player.move(action, self.dungeon)
                   case 'get':
                       lootet_dungeon_room = self.player.get_item(action, self.dungeon)
                       self.dungeon.set_rooms(lootet_dungeon_room)


           #fussgesteuerte Schleife ;)
           if 'item' in self.dungeon.rooms[self.player.current_room] and 'monster' in self.dungeon.rooms[self.player.current_room]['item']:
               print('\n---------------------------')
               print('A monster has got you... GAME OVER!')
               print('---------------------------')
               game_over = True


           if self.player.current_room == 'Garden' and 'key' in self.player.items and 'potion' in self.player.items:
               print('\n---------------------------')
               print('\nYou escaped the house... YOU WIN!')
               print('---------------------------')
               game_over = True


playing = True
while playing:
   game = Game(Player(), Dungeon())
   game.main()
   try_again = input('\nWould you like to try again? [YES/NO]\n---> ').lower()
   if try_again == 'yes':
       print('\n---Next Game---')
   else:
       playing = False
