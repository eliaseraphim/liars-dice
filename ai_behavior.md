# AI Behavior - Liar's Dice
Author: Elia Deppe  
Email: elia.deppe7@gmail.com  

For the game of Liar's Dice the objective is to be the last player with any dice left. Losing dice is the result of either your bet being revealed to be a lie or calling a bet a lie, that turns out to be True. There are many different ways to play this game, but let's note a few key points.
- Avoiding lies / accusations is conducive to winning.
  - Since a player can only lose a dice if they are an accuser or an accused, this means staying out of those two parties ensures you do not lost that round. Therefore, it is in the player's best interest to stay out of this situation at all costs though this may not always be possible.
- Aggressive play is risky, but can be rewarding.
  - Since a lie will ultimately results from too many dice being called for a certain face, it is not possible to always avoid being in the two parties.
  - Playing aggressively allows you to up the ante to something that may not be too ridiculous, but will be in a few turns.
    - This could work out in the player's favor or backfire.

Since I do not wish to utilize machine learning and instead focus on algorithms, I will utilize specific behaviors to help describe the player and give motivation for their actions.

## Behaviors

### Simple

Simple will cover behaviors in which the player makes very simple decisions and will only call Liar if the chances are incredibly low.

#### Raise Count
> Raise Count behavior will have the CPU player always raise the count of the current face of the bet. 
>
> If the chance of said bet has less than 10% chance of being True, then instead they will: raise the face, and reset the count to 1.
> 
> This player will call liar if the previous bet has less than a 5% chance of being True.

#### Raise Face
> Raise Face effectively works the same as raise count, however instead of always raising the count, they will instead raise the face by one, and keep the count.
> 
> If the face is six, then they will simply increase the count by one.
> 
> This player will call liar only when it can no longer raise the face, and the previous bet has a 5% chance of being True.

#### Notes
> I could perhaps give some pathology to this behavior by modifying how much they raise the count by (a more aggressive player increasing the count by a higher amount or through an educated guess.)

### Calculating
> Calculating Players will utilize statistical analysis in order to raise the ante, or call the previous player a liar.

#### ...

This player 