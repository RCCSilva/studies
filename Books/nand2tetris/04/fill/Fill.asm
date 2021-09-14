// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@8181
D = A

@TOTAL_PIXELS
M = D

@isblack
M = 0

(LOOP)
    @24576
    D = M

    @PRINT_BLACK
    D; JGT

    @PRINT_WHITE
    D; JEQ

    @LOOP
    0; JMP

(PRINT_BLACK)
    @isblack
    D = M
    @LOOP
    D; JGT //if screen is already black, jump to loop
    
    @isblack
    M=1

    @SWAP_SCREEN_COLOR
    0; JMP

(PRINT_WHITE)
    @isblack
    D = M
    @LOOP
    D; JEQ //if screen is already bwhite, jump to loop
    
    @isblack
    M = 0

    @SWAP_SCREEN_COLOR
    0; JMP

(SWAP_SCREEN_COLOR)
    @i
    M = 0

    (SWAP_SCREEN_COLOR_LOOP)
        @i
        D = M

        @TOTAL_PIXELS
        D = D - M

        @SWAP_SCREEN_COLOR_END
        D; JGE

        @SCREEN
        D = A

        @i
        A = D + M

        M = !M

        @i
        M = M + 1

        @SWAP_SCREEN_COLOR_LOOP
        0; JMP

    (SWAP_SCREEN_COLOR_END)

    @LOOP
    0; JMP

