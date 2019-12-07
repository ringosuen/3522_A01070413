# Pokedex Tool

Welcome to my Pokedex! It provides info requested from https://pokeapi.co/.

Please use the command line to query your request. 

The Pokedex will be able to search and return data about different Pokemon, Moves and Abilities. 

When using textfile mode, please use the input files provided: pokemon_input.txt, moves_file.txt, ability_input.txt
Alternatively, you can create your own input files. 

## Possible Modes that the Pokedex can Handle:
### Modes: pokemon, ability, move

1. single string (output to console) 

  - eg. python3 pokedex.py "move" "flamethrower"

2. single string + write to external text file 
  
  - eg. python3 pokedex.py "ability" "drizzle" -o”output.txt"

3. single string + expansion 

- eg. python3 pokedex.py "pokemon" “charizard” -e 

4. single string + expansion + write to external file 

- eg. python3 pokedex.py "pokemon" "ditto" -e -o"multiple.txt"

5. read from text file (output to console) 

- eg. python3 pokedex.py "pokemon" “pokemon_input.txt” -e 

6. read from text file + output to external text file  

- eg. python3 pokedex.py "moves" “moves_file.txt” -e -o”output.txt"
