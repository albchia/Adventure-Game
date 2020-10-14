# Adventure-Game
A simple version of an old-fashioned text-based Adventure Game within Python.

This was one of the projects I realized during the Udacity Path "Intro to Programming" Nanodegree.

## Table of Contents
- [About the Project](#About-the-Project) 
- [Contributing](#Contributing)

## About the Project
Title: _"Adventure Game"_

> GitHub: link - https://github.com/albchia/Adventure-Game.git

This is the second project made during Udacity classroom on "Intro to Programming".

#### Project Overview
This project is a simple version of an old-fashioned text-based adventure game: 
- The game will present some scenarios, asking you to make one of the two choices by entering 1 or 2.
- The game gives players a description of what is happening, and then asks them to make a choice.
- Something different happens depending on the choice the player made.
- The game also includes some `random factors`, so the game is a little bit different each time.
- The game has _conditions_ for winning and losing.
- When the game is over, it asks if the player wants to play again.

#### Project Instructions
Feel free to customize text, properties, conditions, factors and scenarios so long as you follow the following rules.
For inspiration, you can try playing around with `random factors` and `text`.

**1. Print descriptions of what is happening for the player**: one thing the will need to do is to print messages for the player to describe what is happening.

**2. Introduce the `time.sleep` to pause between printing descriptions**: add `time.sleep` function to create suspance between the print.

**3. Give the player some choices**: up till now, the program prints the introduction of the game, with short pauses in between each sentence. Another important element of any good Adventure Game is _choice_. To do this, you will need to get some `input` from the player and then change what happens depending on what the input is.

> For example, each time we make a choice something happens, and we are offered 2 choices again till we win or loose:
> - If the player knocks to the door of the _house_, what happens?
> - If the player enters in the _cave_, what happens?

We will deal with subsequent choices after the first choice in the upcoming steps.

**4. Make sure the player gives a valid input**: up to here the program prints a description of the game world to the players, giving them a choice and prints what happens depending on their choice.

An important thing to notice is that if the players enter something different from 1 or 2, _the game keeps asking them for a 1 or 2_, because we dont' want to accept `invalid input`.

**5. Add `functions` and `refactor` your code**: if you haven't done already, it is time to define some `functions` and moving some `code` into those functions.
> Examples are `print_pause` functions.
> It is also possible to use functions in a game where you can define a function for each place the player can go:
>> - def fight():
>> add code
>> - def cave():
>> add code
>> - def field():
>> add code
>
> That way, when a player chooses to go to one of these places, you can simply call the function that displays the descriptions and choices for that place.
> 
Usually, each function will print what happens after the player takes a certain choice, then offer another choice and call the specific function depending on the choice the player makes. In the end, you would have a `play_game` or `main()` function, which starts the game.

**6. Use `randomness` in your game**: another key feature is the `randomness` or _chance_. There are all sorts of ways you could use `randomness` in your game:
- The _enemy_ creature is selected `randomly` each time they play. Sometimes it could be a pirate, a dragon, a troll, a wicked fairie.
- You could do something similar to randomize which _weapons_ or magical items the player encounters.
- You could include, for example, a _combat simulation_...

All of these can be done using Python's `random module`, the `random.choice` and the `random.randint` functions. For example, at the start of the game, you can set the `random enemy creature`. Be creative.

**7. Create `win` and `lose` conditions**: eventually, the game should come to an end -and tell the players if they have won or lost-.

**8. Check if the players want to play again**: when Python gets to the end of the `script`, it will exit back to the terminal. But that is not a good player experience. Instead, it would be better that the game ask the player whether they want to play again.

**9. Check your `style` with `pycodestyle`**: be sure to check the program using `pycodestyle` and then fix any issues.

**10. Test your code**: before submitting your project, be sure to test it.

## Contributing
This repository is the project created by myself during the Udacity Program.
Therefore, pull requests will not be accepted.

> For details, check out [CONTRIBUTING.md](CONTRIBUTING.md).
