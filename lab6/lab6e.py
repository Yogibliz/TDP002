#UPG 6e

import os
import argparse
copyright_text = ''


def insert_copyright(destination, copyright_text):
    # Öppna filen och läs innehållet
    with open(destination, 'r') as file:
        file_content = file.read()

    # Hitta alla förekomster av BEGIN COPYRIGHT och END COPYRIGHT
    begin_marker = 'BEGIN COPYRIGHT'
    end_marker = 'END COPYRIGHT'
    
    #Lists without using the list comprehensions. (Here as an explainer on how list comprehensions work.)
    
    # begin_positions = []
    # end_positions = []

    # for pos, _ in enumerate(file_content):
    #     if file_content.startswith(begin_marker, pos):
    #         begin_positions.append(pos)
    #     if file_content.startswith(end_marker, pos):
    #         end_positions.append(pos)
    
    
    #Gets the position of begin copyright and end copyright using enumerate.
    #If a line starts with begin_marker, the position of that line is added to begin_positions. 
    #If a line starts with end_marker, the position of that line is added to end_positions. 
    #These positions will later be used to insert copyright information into the file between the specified markers.
    begin_positions = [pos for pos, _ in enumerate(file_content) if file_content.startswith(begin_marker, pos)]
    end_positions = [pos for pos, _ in enumerate(file_content) if file_content.startswith(end_marker, pos)]


    #Insert copyright information between the markers.
    #Copy the file_content to a new variable.
    modified_content = file_content
    #Pairs upp the start and end positions into a tuple with zip.
    for begin_pos, end_pos in zip(begin_positions, end_positions):
        #Assigns the start_index as the position for the begin_marker + the length of the begin_marker so that it remains when adding the copyright information.
        start_index = begin_pos + len(begin_marker)
        #Adds the end index as the position for the end_marker since im going to use list splicing.
        end_index = end_pos
        #Assigns the modified content from the start to the start index, then the copyright text, then everything from the end index till the end of the file.
        #The + and - 1 are there to include the '' at the end and start of the respctive marker.
        modified_content = modified_content[:start_index + 1] + '\n"' + copyright_text + '"\n' + modified_content[end_index -1:]

    #Write the modified content to the file.
    with open(destination, 'w') as file:
        file.write(modified_content)

#If the input specifies a directory.
#Takes a directory, the file extension and a optional new extension.
def process_directory(directory, file_extension, new_extension=None):
    #Search for all the files in the root directory (the directory supplied by the user)
    for root, _, files in os.walk(directory):
        #Iterate through all the files in the current directory.
        for file_name in files:
            #Checks if the file ends with None or the specified file_extension.
            if file_extension is None or file_name.endswith(file_extension):
                #Get the full file path.
                destination = os.path.join(root, file_name)
                #Then insert copyright in that file.
                insert_copyright(destination, copyright_text)
                #If a new extension is supplied by the user, add that to the end of the filename.
                if new_extension:
                    #Use os.path.splittext to get the filename then add the new extension in the place of the old one.
                    new_destination = os.path.splitext(destination)[0] + new_extension
                    #Then rename the file from the old name + file extension, to the new file name + the new file extension.
                    os.rename(destination, new_destination)

def main():
    #Assigns argparse.Argumentparser to the variable parser.
    #Then uses it to add arguments for my program. This way the user input is read and applies to the functions and the user gets help with how to use the functions.
    parser = argparse.ArgumentParser()
    parser.add_argument('copyright_file', help='|Obligatoriskt| Sökväg till copyright-textfilen (Skapas innan körning av program med valfri copyright-text)')
    parser.add_argument('destination', help='|Obligatoriskt| Sökväg till målet (fil eller katalog) | Namn på fil eller katalog (om du står i katalogen där de befinner sig)')
    parser.add_argument('--file_extension', '-c', help='|Friviligt| Filtrerar efter filer med matchande filändelse (Ex: py, js, html, css ...)')
    parser.add_argument('--new_extension', '-u', help='|Friviligt| Ny filändelse, om filändelsen ska bytas ut efter filen uppdaterats. (Ex: c.py, c.js, c.html, c.css ... för att indikera att copyright infogats.)')
    #Assigns parse_args() to the variable args. This catches the user input and adds it to the args variable.
    args = parser.parse_args()
    #Example of parse_args() where args.copyright_file is a variable that is assigned the user input file.
    if args.copyright_file:
        try:
            with open(args.copyright_file, 'r') as copyright_file:
                copyright_text = copyright_file.read()
        except FileNotFoundError:
            print(f"Kunde inte hitta filen '{args.copyright_file}'.")
            return

    #Gets the arguments from the user input, in the order the arguments are written. (copyright_file, destination, (-c) file_extension, (-u) new_extension)
    #Then uses their values to run the functions.
    destination = args.destination
    file_extension = args.file_extension
    new_extension = args.new_extension

    if os.path.isfile(destination):
        insert_copyright(destination, copyright_text)
        if new_extension:
            os.rename(destination, os.path.splitext(destination)[0] + "." + new_extension)
    elif os.path.isdir(destination):
        process_directory(destination, file_extension, new_extension, copyright_text)
    else:
        print('Målet finns inte eller är varken en fil eller katalog.')

if __name__ == '__main__':
    main()