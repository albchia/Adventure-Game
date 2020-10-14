# Adventure-Game
A simple version of an old-fashioned text-based Adventure Game within Python.

This was one of the projects I realized during the Udacity Path "Intro to Programming" Nanodegree.

## Table of Contents
- [About the Project](#About-the-Project) 
- Contributing

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
> Usually, each function will print what happens after the player takes a certain choice, then offer another choice and call the specific function depending on the choice the >player makes.
