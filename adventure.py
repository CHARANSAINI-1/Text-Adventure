import json
import sys

class GameEngine:
    def __init__(self, map_file):
        self.load_map(map_file)
        self.current_room = self.map_data[0]
        self.inventory = []

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            self.map_data = json.load(file)


    def go(self, target):
        room = self.current_room 
        if target in room['exits']:
            self.current_room = self.map_data[room['exits'][target]]
            print(f"You go {target}.")
            print("\n")
            room = self.current_room
            print("> ", room['name'])
            print("\n")
            print(room['desc'])
            print("\n")
            if 'items' in room and len(room['items']):
                print('Items:', ', '.join(room['items']))
            print("\n")
            print('Exits:', ' '.join(room['exits'].keys()))
            print("\n")
            # print items if exists
            
            
                    
            visited = True

        elif target == None:
            print("Sorry, You need to 'go' somewhere.")    
        elif target not in room['exits']:
            print(f"There's no way to go {target}.")

    def look(self):
        room = self.current_room
        print("> ", room['name'])
        print(room['desc'])
        print('Exits:', ', '.join(room['exits'].keys()))
        # print items if exists
        if 'items' in room and len(room['items']):
            print('Items:', ', '.join(room['items']))
        if self.inventory:
            print('Inventory:', ', '.join(self.inventory))
        visited = True  

    def get(self, target):
        room = self.current_room
        if 'items' in room and target in room['items']:
            self.inventory.append(target)
            room['items'].remove(target)
            print(f'You pick up the {target}.')
        elif target == None:
            print("Sorry, you need to 'go' somewhere.")    
        else:
            print(f"There's no {target} anywhere.") 

    def inventory1(self):
        if not self.inventory:
            print("You're not carrying anything.")
        else:
            print('Inventory:')
            for item in self.inventory:
                print(' ', item)

    def drop(self, target):
        room = self.current_room
        if 'items' not in room:
            room['items'] = []
        if target in self.inventory:
            self.inventory.remove(target)
            room['items'].append(target)
            print(f'You dropped the {target}.')
        elif target == None:
            print("Sorry, you need to 'drop' something.")    
        else:
            print(f"There's no {target} in your inventory.")             

    def quit(self):
        print("Goodbye!")                              

    def run(self):
        visited = False;
        
        while True:
            # Print room description
            if visited == False:
                room = self.current_room
                print("> ", room['name'])
                print('\n')
                print(room['desc'])
                print('\n')
                print('Exits:', ' '.join(room['exits'].keys()))
                print('\n')
                # print items if exists
                if 'items' in room and len(room['items']):
                    print('Items:', ' '.join(room['items']))
                if self.inventory:
                    print('Inventory:', ', '.join(self.inventory))
                visited = True
            
            # Get player input
            try:
                command = input('What would you like to do? ').lower().split()
            except EOFError:
                print("Use 'quit' to exit.")
                continue
            

            # Parser
            verb = command[0]
            target = ' '.join(command[1:]) if len(command) > 1 else None

              

            # Verbs
                # call the go function when the verb is 'east'
            if verb == "east":
                target='east'
                self.go(target)

                # call call the go function when the verb is 'west' 
            elif verb == "west":
                target='west'
                self.go(target)

                # call call the go function when the verb is 'north' 
            elif verb == "north":
                target='north'
                self.go(target)

                # call call the go function when the verb is 'south' 
            elif verb == "south":
                target='south'
                self.go(target)

                # call call the go function when the verb is 'northwest' 
            elif verb == "northwest":
                target='northwest'
                self.go(target)

                # call call the go function when the verb is 'northeast' 
            elif verb == "northeast":
                target='northeast'
                self.go(target)

                # call call the go function when the verb is 'southwest' 
            elif verb == "southwest":
                target='southwest'
                self.go(target)

                # call call the go function when the verb is 'southeast' 
            elif verb == "southeast":
                target='southeast'
                self.go(target)                        
            
            elif verb == 'go':
                self.go(target)

            elif verb == 'look':
                self.look()
 
            elif verb == 'inventory':
                self.inventory1() 

            elif verb == 'get':
                self.get(target)
                
            elif verb == 'drop':
                self.drop(target)              
            
            elif verb == 'quit':
                self.quit()
                break
            else:
                print("I don't understand that command.")
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <map_file>")
        return

    map_file = sys.argv[1]
    game = GameEngine(map_file)
    game.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye!")
        sys.exit(0)
               
        
    
