import os

# The user selected level and the list with all levels.
selected_level = []
levels = []
# Input Declarations
key_up = 'w'
key_down = 's'
key_left = 'a'
key_right = 'd'
# Character Declarations
player_base = '@'
floor = ' '
box = 'o'
storage = '.'
player_on_storage = '+'
box_on_storage = '*'
wall = '#'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    #Uses 'cls' to clear the terminal window if os.name is nt, otherwise us 'clear'. This makes sure that it can run on both Windows and Unix based systems.

def did_player_win(level):
    #Checks if there are any boxes left, if there are no boxes in their base state, the player won the game.
    for line in level:
        for item in line: 
            if item[1] == box:
                return False 
    return True

def import_maps():
    for root, _, files in os.walk('sokoban_levels'):    #In the folder (sokoban_levels), look for directories (_) and files (files)
        for file_name in files: #get the file names out of the folder
            path = os.path.join(root, file_name)    #Concatenate (joins together / merges) the files out of the folder (sokoban_levels), into the the full length file path. Example: "sokoban_levels/level_1.sokoban"
            levels.append(path) #Append the full path to the levels list
    
def load_map(file_path, row=[]):    #Ask for the file_path and optionally the row in that path. This is used to get the map of choice later.
    with open(file_path, 'r', encoding='utf-8') as file:    #Open the file
        for line in file:   #Loop through the lines in the file
            x = 0   #x coordinate for each character in the line
            row = []
            for char in line.strip():   #Loops through all the characters in the current line
                if char != " " and char != "\n":    #If the character is not a space or a newline character, append the x coordinate and the character as a string to the row list.
                    row.append([x, str(char)])
                x += 1  #Update the x position for each character.
            if row:  # Only append the row if it's not empty
                selected_level.append(row)
            
def find_player():
    #Loops through the lines in the selected_level, then checks if item[1] (the character) for the positions is == player_base or player_on_storage.
    for line in selected_level:
        for item in line:
            #If either one of those is correct take item[0] (x coordinate of the position) and add it to the x variable. Then add the index of the line (the y position) to the y variable.
            if item[1] == player_base or item[1] == player_on_storage:
                x = item[0]
                y = selected_level.index(line)
                player = item[1]
    #The function then returns the x and y postion and the player icon that is assosiated with that position (@ or +).
    return [x, y , player]
            
def player_moveable(x, y, nx, ny):
    #Get the position of where the box is moving
    xx, yy = box_movement(x, y, nx, ny)
    #Get the position of the player
    position = get_symbol(nx, ny)
    #If the input makes the player position align with the position of a wall, return False
    if position == wall:
        return False
    #If the input makes the player position align with the position of a box, and the box is not movable, return False
    if position == box and box_moveable(xx, yy) == False:
        return False
    #If the input makes the player position align with the position of a box_on_storage, and the box_on_storage is not movable, return False
    if position == box_on_storage and box_moveable(xx, yy) == False:
        return False
    #If none of these are in the way, the player is moveable, so return True
    return True

def box_movement(x, y, nx, ny):
    #Checks if x is the same as the x that of the new location, if it is, the box is moving vertically.
    if x == nx: 
        xx = nx
        #If current vertical position is greater than the new location, the crate is moving up, so yy is set to the new space position (ny) - 1
        if y > ny: 
            yy = ny - 1
        #If current vertical position is less than the new location, the crate is moving down, so yy is set to the new space position (ny) + 1
        else:
            yy = ny + 1
    #Checks if y is the same as the y of the new location, if it is, the box is moving horizontally.
    if y == ny: 
        yy = ny
        #If current horizontal position is greater than the new location, the crate is moving to the left, so xx is set to the new space position (nx) - 1
        if x > nx:
            xx = nx - 1
        #If current horizontal position is less than the new location, the crate is moving to the right, so xx is set to the new space position (nx) + 1
        else: 
            xx = nx + 1
    
    return xx, yy 

def box_moveable(x, y):
    #Checks if the crate can move to the new destination. 
    position = get_symbol(x, y) 
    if position == floor: 
        return True
    #Im thinking you should be able to move from storage, so that you can push it to another storage point if needed.
    if position == storage: 
        return True
    return False

def get_symbol(x, y):   #This does not return the empty spaces ahead of the first character since item[0] is the x position with the first non-space character.
    #print(f"Getting symbol at coordinates x={x}, y={y}")
    #Checks so that the y value is that of the length of the selected level, this way we don't get any extra lines printed ahead as we would if
    #we were to change for item in selected_level[y] to [y - 1]. Since this would print the last line in the file ahead of the first one.
    #Loops through the y coordinate that is input, checks if the x coordinate item[0] (item[0] represents all the x values in the y line) == the x value that is input
    #If the x value matches, return the object, according to the Character declarations (item[1]). Otherwise return floor, since it's an empty space.
    if 0 <= y < len(selected_level):
        for item in selected_level[y]:
            if item[0] == x:
                return item[1]
    return floor

def get_max_y(map): #Get the max value for y
    max_y = len(map)
    return max_y

def get_max_x(map): #Get the max value for x
    max_x = 0
    for line in map:
        for item in line:
            x = item[0]
            if x > max_x:
                max_x = x
    return max_x

def show_map(map):  #Prints the x position at the first character found instead of the first blankspace, so if maps start with spaces it doesn't print those.
    clear_screen()
    max_x = get_max_x(map)
    max_y = get_max_y(map)
    for y in range(0, max_y + 1):  # +1 for y and x to account for range excluding the last number
        for x in range(0, max_x + 1):
            symbol = get_symbol(x, y)
            print(symbol, end="")
        print()

def sokoban_input():
    #Get user input for moves in the map
    move = input("\nMove [w] [a] [s] [d] or (q) to quit: ")
    return move.lower() #Return the user input as lowercase to make sure we don't have to handle uppercase in the key assignements.

def destroy_object(x, y, obj=''):
    #Remove object from position.
    if obj == '':   #If obj is not provided, get the position of the object.
        obj = get_symbol(x, y)
    selected_level[y].remove([x, obj])  #Select the object that is provided by the function call or the function default, then remove the object at that position.
    #This destory works because we always replace what is removed because the character is moving to a new spot instead of getting entirely removed.

def create_object(dx, dy, obj):
    #Create object at position.
    for item in selected_level[dy]: #Loop through the y coordinate until it finds the x coordinate
        if item[0] > dx:    #One the x coordinate is larger than the input x coordinate it stops
            selected_level[dy].insert(selected_level[dy].index(item), [dx, obj])    #Where it stops it inserts the item at the new x coordinate.
            break   #Just too make sure it exits the loop once it's done.

def move(x, y, nx, ny, obj):    #Take the current x, y postions | the new x, y positions | the object that should be moved.
    #The function which will move everything
    target = get_symbol(nx, ny)   #First we get the position that we are trying to move.
    xx, yy = box_movement(x, y, nx, ny) #We get the box movement since it already has its own move function.

    destroy_object(x, y)    #Destroy the object that which is moved, so that it later can be created where it's supposed to be.

    if obj in [player_base, player_on_storage]: #Checks if the object that is defined is the player.
    # Moving the player, making sure the player is a + when on a storage space    
        player = player_base

        if target == storage:   #If the player moves on top of storage, change the storage/player object into player_on_storage
            destroy_object(nx, ny)
            player = player_on_storage

        if target == box:   #If the player moves "on top" of a box, push it in the direction dictated by box_movement.
            move(nx, ny, xx, yy, box)   #Move the box from the new x and y (for the player), to the new position that the box_movement determined.

        if target == box_on_storage: #If the player moves on top of storage, change the storage/player object into player_on_storage even in this case, since the box will be pushed out of the storage. (Handled just to make sure it works even if the box is on a storage spot)
            move(nx, ny, xx, yy, box_on_storage)    #Move the box_on_storage from the new x and y (for the player), to the new position that the box_movement determined.
            player = player_on_storage
            
        if obj == player_on_storage: #If the object is player_on_storage, make sure to leave a storage point behind after walking off of it. So that we don't remove the storage by walking on it.
            create_object(x, y, storage)

        create_object(nx, ny, player)   #When walking of the storage we want to be returned into player_base, so it's the default.

    if obj in [box_on_storage, box]:    #Checks if the object that is defined is the box.
    # Moving the boxes, making sure the boxes become a * when on a storage space
        crate = box
        if target == storage and obj == box:    #If the box is moved on to the target position, and the target position is a storage spot, destory the storage and insert a box_on_storage
            destroy_object(nx, ny)
            crate = box_on_storage 
        
        if target == storage and obj == box_on_storage: #If the box is moved on to the target position, and the target position is a storage spot, still keep it a box_on_storage. (This is in case of 2 storages next to eachother)
            destroy_object(nx, ny)
            crate = box_on_storage

        create_object(nx, ny, crate)    #When moved of of a storage spot, return to a box.

def sokoban_game():
    clear_screen()
    level = False   #Start level as False, since the player hasn't yet select a level to play.
    while not level:    #While no level is picked. Try to ask for a user input of 1 or 2. 
        try:
            level = int(input("What level do you want to play (1 or 2): ")) #Get the user input and convert it to an int, so that they can't input a float etc.
        except:
            print("Unexpected level number, try again.")    #In case the user enters a value that is not an integer, try again.
            level = False  
        if level > len(levels):
            print("Unexpected level number, try again.")    #In case the user enters a value that is larger than the amount of maps available, try again.
            level = False
        elif level < 0:
            print("Unexpected level number, try again.")    #In case the user enters a value that is less than the amount of maps available, try again.
            level = False
            
    level = int(level) - 1  #Making sure the input corresponds with the index in the list.

    load_map(levels[level]) #Load the level that was picked by the user.
    show_map(selected_level)    #Show the map that was loaded.
    
    
    while True: #While true (player hasn't won), ask for user movement input.
        key = sokoban_input()   #The print for which keys to use.
        
        x, y, player = find_player()    #Get the current player position and icon
        
        #Based on what key the user presses move in a direction, if the player is moveable otherwise it does nothing.
        #Example: if key == key_up and player_moveable(x, y, x, y - 1) then move(x, y, x, y - 1, player). 
        #This means if the key entered, is the key_up bound in declarations (w) and the player can move to that position, then move the player 1 step up.
        if key == key_up and player_moveable(x, y, x, y - 1):
            move(x, y, x, y - 1, player)
        if key == key_down and player_moveable(x, y, x, y + 1):
            move(x, y, x, y + 1, player)
        if key == key_left and player_moveable(x, y, x - 1, y):
            move(x, y, x - 1, y, player)
        if key == key_right and player_moveable(x, y, x + 1, y):
            move(x, y, x + 1, y, player)
        #If the user input is q, then quit the game.
        if key == 'q':
            quit()
            
        show_map(selected_level)    #Show the new map state after every move.
        if did_player_win(selected_level):  #Check if the player has won after every move by using the did_player_win function. The function is a boolean which returns True or False depending if there are any boxes left.
            clear_screen()
            print("You won! Good Job :3")   #If the player won, give them a congratulation message.
            break   #Break out of the game loop
        
    quit()  #After breaking out of the game loop, quit the program.

#Test
def main():
    import_maps()   #Import the maps.
    sokoban_game()  #Run the game.    
if __name__ == '__main__':  #Makes sure that the main function is ran as long as the code is run as a program.
    main()