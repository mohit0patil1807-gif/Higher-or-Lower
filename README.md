# Higher Lower Game

A command-line implementation of the popular "Higher or Lower" follower guessing game, built in Python.

## Overview

The Higher Lower Game challenges players to test their pop culture knowledge by comparing the Instagram follower counts of well-known public figures, celebrities, and global brands. In each round, players must decide whether option A or option B has more followers. A correct guess earns a point and advances the game to the next round, while an incorrect guess ends the run.

## Live Demo

An interactive browser-based demo of the game is available here:
https://appbrewery.github.io/python-day14-demo/

## How to Play

1. Run the game using Python.
2. The game displays the first entity (A) with their name, description, and country of origin.
3. The game displays a second entity (B) alongside the "VS" banner.
4. When prompted:
   - Type `A` if you believe entity A has more followers.
   - Type `B` if you believe entity B has more followers.
5. If your answer is correct:
   - Your score increases by 1.
   - Entity B becomes the new entity A.
   - A new entity B is randomly selected from the dataset.
6. If your answer is incorrect:
   - The game terminates immediately and reveals your final score.

## Features

- Dynamic Comparison: Randomly pairs notable personalities, athletes, artists, and organizations from around the world.
- Seamless Progression: The winner from position B seamlessly transfers to position A in consecutive rounds.
- ASCII Graphics: Integrated terminal ASCII art for the game title and confrontation banner.
- High Replayability: Extensive dataset featuring dozens of entries with follower counts in millions.
- Pure Python: Built entirely with Python's standard library with zero external package dependencies.

## Project Structure

- `main.py`: Contains the main game loop, user input handling, scoring mechanics, and winner evaluation.
- `game_data.py`: Contains the list of dictionaries holding entity profiles (name, follower count, description, country).
- `art.py`: Contains the ASCII art logos for the game header and the VS divider.
- `README.md`: Project documentation and instructions.

## Prerequisites

- Python 3.6 or higher
- Git (optional, for cloning)

No external libraries or pip installations are required.

## Installation and Execution

1. Clone this repository or download the source files:
   ```bash
   git clone https://github.com/mohit0patil1807-gif/Higher-or-Lower.git
   cd Higher-or-Lower
   ```

2. Run the game script:
   ```bash
   python main.py
   ```

## Example Gameplay

```text
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Cristiano Ronaldo, Footballer, from Portugal
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Kim Kardashian, Reality TV personality and businesswoman, from United States
Who has more followers? Type 'A' or 'B' A
Yor are right! your current score is 1
```

## Acknowledgments

- This project was created as part of Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp" (Day 14).
- Interactive web demo provided by The App Brewery: https://appbrewery.github.io/python-day14-demo/
