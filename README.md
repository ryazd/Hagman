# Hangman is a popular yet grim puzzle game. A cruel computer hides a word from you, which you try to guess letter by letter. If you fail, you'll be “hanged”. If you win, you'll survive. You’ve probably played the game at least once or twice.

## Example 1:

H A N G M A N  # 8 attempts  
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > play

------
Input a letter: > h

---h--  
Input a letter: > K  
Please, enter a lowercase letter from the English alphabet.

---h--  
Input a letter: > t

--th--  
Input a letter: > o

--tho-  
Input a letter: > +  
Please, enter a lowercase letter from the English alphabet.

--tho-  
Input a letter: > K  
Please, enter a lowercase letter from the English alphabet.

--tho-  
Input a letter: > h  
You've already guessed this letter.

--tho-  
Input a letter: > K  
Please, enter a lowercase letter from the English alphabet.

--tho-  
Input a letter: > n

--thon  
Input a letter: > q  
That letter doesn't appear in the word.  # 7 attempts

--thon  
Input a letter: > y

-ython  
Input a letter: > h  
You've already guessed this letter.

-ython  
Input a letter: > p  

You guessed the word python!  
You survived!  
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > results  
You won: 1 times.  
You lost: 0 times.  
Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > exit
