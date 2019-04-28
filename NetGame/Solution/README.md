# 4-in-a-row network game

A simple game of 4-in-a-row / Connect Four [(wikipedia)](https://en.wikipedia.org/wiki/Connect_Four), but played over the network!

# `smor` library

`smor` is a library for Simple Message-Oriented, Relayed communication. A quick tutorial on using it follows:

1. Import the client library:
    ```py
    import smor.client as sm
    ```

2. Before communicating, be sure to configure it:
    ```py
    sm.config(hostname)
    ```

    We have a server running at `lambda-lab.cf`, that can be used for this game.

`smor` uses "mailboxes" to pass around messages. Think of them as actual boxes which sit on the server, and you can `put` messages into them, or `get` messages out. Once you `get` the message it's gone from the box - you can't get it again so be sure to store it in a variable as long as you need it. Also messages are retrieved in the same order they are put in - First In, First Out.

The functions we have are:

  * `sm.get_one(msgbox)` - get one message from box named `msgbox`. 
    Returns `None` if there are no messages waiting.
  * `sm.get_all(msgbox)` - gets a list of all messages waiting in a box named `msgbox`.
  * `sm.put(msgbox, message)` - puts a message `message` into a box named `msgbox`. 
    The message can be a number, a boolean, a string, a list or a dictionary. 

For more information you can look at pretty much the same README at the `smor`'s repo [here](https://github.com/profMagija/smor).

# Communication

To keep everyone compatible, here is how the communication for the game goes:

Each game needs a `room_name`, a string identifying the game. The player will be asked for it, and both players need to use the same `room_name` to play the game. In further text, replace `room_name` with the actual room name.

First we need to check if we are the first player. We do this by attempting to read from `game/room_name/first`. 

  * If there is something there, we are the **second** player. 
    We need to signal to the first player that we are ready by writing something to the `game/room_name/second` mailbox.
  * If there is nothing there, we are the **first** player. 
    We need to "claim" our firstness by writing something to `game/room_name/first` (for the second player to find), and then wait for something to show up in `game/room_name/second` mailbox (by attempting to read from it until we get something).

Then we proceed with the game. The game goes by the rules of Connect Four. For sending the move to the other player use:
  * `game/room_name/move_first` mailbox if you are the first player
  * `game/room_name/move_second` mailbox if you are the second player

and read from the mailbox of the other player for receiving the move.

