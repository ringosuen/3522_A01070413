# Pokedex Tool

Welcome to my Pokedex! It grabs info from

Please use the command line to query your request. 

The Pokedex will be able to search different Pokemon, Moves and Abilities. 

## Possible Modes that the Pokedex can Handle:

1. single string (output to console) 

  - eg. python3 pokedex.py "pokemon" "ditto"

2. single string + write to external text file 
  
  - eg. python3 pokedex.py "pokemon" "ditto" -o”output.txt"

single string + expansion 

python3 pokedex.py "pokemon" “charizard” -e 

single string + expansion + write to external file 

eg. python3 pokedex.py "pokemon" "ditto" -e -o"multiple.txt"

read from text file (output to console) 

eg. python3 pokedex.py "pokemon" “pokemon_input.txt” -e 

read from text file + output to external text file  

python3 pokedex.py "pokemon" “moves_file.txt” -e -o”output.txt"
