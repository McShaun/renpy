# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character('Josue', color="#c8ffc8")
define n = Character('Narrator', color="#fd536b")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg neighborhood

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    play music "audio/MantraStudio.mp3"

    n "There once was a place,"
    n "Between somewhere"
    n "and somewhere else."
    n "Quite frankly it was in the middle of nowhere."
    n "It was in a rural run-down little town"
    n "Nearly an hour from any city you might have heard of."
    n "But in this place, was a crazy crew of misfortunate misfits."
    n "Teenagers, who had nothing to do"
    n "So they made their own fun."
    n "This is the story of.."
    n "The story of how they.."

    show josue

    j "WAIT, WHAT?!? Who are you? Who was that talking to you just now?"

    hide josue

    n "Oh sorry, that was me. I was just.."

    show josue

    j "Don't tell my story.."
    j "That's my job."

    hide josue

    n "Right.."
    n "I was just.."

    show josue

    j "Whatever. Just get to the good part."
    j "Show em that street where we had an accident."

    hide josue

    scene bg street
    with fade

    play music "audio/libertines.mp3"

    n "You mean this street?"

    show josue

    j "NOOO! Not this one!"

    hide josue

    scene bg joslin

    n "oh you mean this one right?"

    show josue

    j "Yeah. This place"
    j "This place is crazy."

    hide josue

    n "more to come soon..."

    # This ends the game.

    return
