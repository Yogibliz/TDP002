import random

def create_deck():
    deck = []   #Empty starting list
    hearts = ["♥"] * 13   #Makes sure hearts go from 1-13
    spades = ["♠"] * 26   #Spades go from 1-26
    jokers = [("J1", 27), ("J2", 27)]  #Converts the numbers in the ranges (1-13) and (14-26) (doesn't include last number) from integers to strings.
    
    hearts_numbers = [f"{hearts[i]}{i + 1}" for i in range(13)] #Prints out the value of hearts
    spades_numbers = [f"{spades[i]}{i + 1}" for i in range(13, 26)] #Prints out the value of spades, but only in the range 13, 26 since 1-13 are supposed to be hearts.
    
    deck = hearts_numbers + spades_numbers + jokers #Adds the correct ranges for everything into the deck list.
    return deck

def shuffle_deck(deck):
    shuffled_deck = deck.copy() #Make a copy of the deck. This copy will hold the value of random.shuffle() which would otherwise return a None value.
    random.seed(13)
    random.shuffle(shuffled_deck)
    return shuffled_deck

def move_card(deck, from_index, to_index):
    card = deck.pop(from_index)
    deck.insert(to_index, card)
    return deck

def find_card(deck, spot):
    spot_index = deck.index(spot)
    return spot_index

def split_deck(deck, index1, index2):
    slice_list = deck[index1 : index2]
    return slice_list

def merge_deck (deck, index1, index2):
    #Merges the deck in the order C, B, A. Depending on which joker comes first in the list the C, B and A parts are different thus we make sure
    #to still shuffle it in the correct order.
    if index1 < index2:
        merged_deck = deck[index2 + 1:] + deck[index1:index2 + 1] + deck[:index1]
    elif index2 < index1:
        merged_deck = deck[index1 + 1:] + deck[index2:index1 + 1] + deck[:index2]
    
    return merged_deck

def get_keystream_value(deck):
    #Card_value(card) gives the the value of the card as an integer.
    #deck[0] accesses the first card in the deck, card_value(deck[0]) then uses the value of the first number.
    #deck[card_value(deck[0]) - 1] is then used to index the shuffled deck. 
    #The -1 is there because the list starts with number 1 instead of 0 and we want to get the value from the first index in the list.
    keystream_val = card_value(deck[card_value(deck[0]) - 1])
    return keystream_val

def remove_card(deck, index):
    deck.pop(index)
    return deck

def card_value(card):
    if card == ("J1", 27) or card == ("J2", 27):
        return 27
    return int(card[1:])    #Start from index 1 instead of 0, since the first index is a symbol

def generate_keystream(deck, length):
    keystream = ""
    while len(keystream) < length:  #Loops through everything while the length is still larger than the length of keystream
        for _ in range(length):
            # Move joker A and B
            #Moves Joker-1 ("J1") from its current position to its current position + 1, % len(deck) is used to move the joker 1 step below the top card should it pass out of bounds
            deck = move_card(deck, find_card(deck, ("J1", 27)), (find_card(deck, ("J1", 27)) + 1) % len(deck))
            #Moves Joker-2 ("J2") from its current position to its current position + 2, % len(deck) is used to move the joker 2 steps below the top card should it pass out of bounds    
            deck = move_card(deck, find_card(deck, ("J2", 27)), (find_card(deck, ("J2", 27)) + 2) % len(deck))
            
            # Shuffle and rearrange the deck
            #Makes sure it splits the deck correctly even if J2 is before J1 in the list and vice versa.
            index_j1 = find_card(deck, ("J1", 27)) #Get the new position of Joker-1 (("J1", 27)) #Use double parenthesis because it's in a paranthesis in the list.
            index_j2 = find_card(deck, ("J2", 27)) #Get the new position of Joker-2 (("J2", 27))
            
            merge_deck(deck, index_j1, index_j2)
            
            keystream_value = get_keystream_value(deck)

            #If the card value is not 27 (a Joker) add a new character to the keystream string, the new character is calculated by the value of the card - 1 (to account for the 0-25 range)
            #Then we add the value of ord("A") so that it gets the correct letter value.
            if keystream_value != 27:
                keystream += chr(keystream_value - 1 + ord("A"))    #We add the value of ord("A") because the the user input message will have that value after using chr().
        
    #Makes sure that the keystream is the same length as the message and otherwise cuts it down to the length of the message.
    split_deck(keystream, 0, length)

    return keystream

def solitaire_keystream(message, length):
    deck = create_deck()
    shuffled_deck = shuffle_deck(deck)
    keystream = generate_keystream(shuffled_deck, length)
    
    message = message.upper()   #Converts the message to uppercase
    ciphertext = "" #Initiates an empty string
    for i in range(len(message)):   #Loops through all the characters in the user input message
        if not message[i].isalpha():    #If the message contains a non alphabet character (A-Z) add it to ciphertext
            ciphertext += message[i]
        else:
            #Calculates the value for the current character based of the the keystream value at the same position
            shift = ord(keystream[i]) - ord("A")
            
            #Calculates the value of the current letter and adds the value of the keystream letter in the same position (shift).
            #Then modulo 26 is there to make sure that if the value goes above 26 it starts over from 1.
            #Then ord("A") is added to convert this mess back in to a letter.
            shifted_char = chr(((ord(message[i]) - ord("A") + shift) % 26) + ord("A"))
            ciphertext += shifted_char
    return ciphertext

def solitaire_decrypt(message, length):
    deck = create_deck()    #Creates the deck again, since it's always the same
    shuffled_deck = shuffle_deck(deck)  #Shuffles it up, the same way as usual, since there is a random seed.
    keystream = generate_keystream(shuffled_deck, length)   #Gets the keystream
    
    #Don't need to convert the message to uppercase this time, since the message input will already be uppercase.
    plaintext = ""  #Start with an empty string to assign the value

    for i in range(len(message)):   #Loops through all the characters in the user input message
        if not message[i].isalpha():    #If the message contains a non alphabet character (A-Z) add it to plaintext
            plaintext += message[i]
        else:
            #Calculates the value for the current character based of the the keystream value at the same position
            shift = ord(keystream[i]) - ord("A")
            
            #Calculates the value of the current letter and removes the value of the keystream letter in the same position (shift), since we want to undo the shift that is done when encrypting.
            #Then modulo 26 is there to make sure that if the value goes above 26 it starts over from 1.
            #Then ord("A") is added to convert this mess back in to a letter.
            shifted_char = chr(((ord(message[i]) - ord("A") - shift) % 26) + ord("A"))
            plaintext += shifted_char

    return plaintext

#Test everything
message_input = str(input("Write anything: "))  #User input message
key_length = len(message_input) #The length of the message, since the encryption and decryption both require the messages length.
encrypted_message = solitaire_keystream(message_input, key_length)  #Defines the encrypted message
decrypted_message = solitaire_decrypt(encrypted_message, key_length)    #Defines the decrypted message

print("Encrypted message: ", encrypted_message) #Prints the Encrypted message
print("Decrypted message: ", decrypted_message) #Prints the Decrypted message