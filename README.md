# What's the project about?

This is a simple project that asks the user to input the size of their t-shirt and also what they want to printed on their t-shirts, allowing them to create a custom t-shirt.

## How is this different from other similar projects?

The best thing about this project is that it only allows valid input for example when the code asks this:

```
What size of t-shirt do you want?(S/M/L/XL/XXL): 
```

or this:

```
Press y to confirm and n to rechoose your order. Press q to quit
```

You can only give the asked inputs and not any other inputs making the program less vulnerable to idiots who will try to write 4.8 in the input when the t-shirt's size is asked or give small pp in the input if they are asked to confirm their order.

In case if you by mistake give any other unexpected input the program crashes... just joking it will tell you to :

```
Please choose correct size (S/M/L/XL/XXL).
```

or:

```
Choose only 'y'/'n'/'q' for yes, no and quit respectively: 
```

and then redirect you to the line which will ask you to give the valid input.

## What do I want to achieve from this?

I am a newbie in the programming world and I love to experiment. This is one of such experiments. If you have come here somehow and you are also a newbie, you are welcome to make changes and create a PR.

## Some general things that will come to your mind while reading my code:

### Why the code is so garbage?

Yeah I know it's garbage, but what do you expect from a newbie? If you think it's garbage please consider improving it so that I can learn by your more efficient code. :)

### Is there any problem?

**Yes!** there is one and I have left it for the reader to solve.*(I am not lazy, I just don't like to work.)*

***The problem is :***

Even after confirming an order the program instead of quitting restarts itself. I know I ~~f#cked~~ messed somewhere in the while loop, but I can't figure out where *(Actually I did, but I want someone to contrbiute to my code :])*. Feel free to make changes in the code and send me a PR.:]
