// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Given R0, R1 and R2, we'll multiply R0 and R1 in a loop. Each iteration, I'll add R0 to a @sum
// value  R1 times. Starting with i = 0, we'll iterate until "i" gets equals to R1 which means that,
// we have added R0 with itself "R1 times".
// After the loop, finally, we'll move the value of @sum to R2 and finish the program with 
// an eternal loop.

    @i
    M = 0

    @sum
    M = 0

(LOOP)
    @i
    D = M

    @R1
    D = D - M

    @END
    D; JGE

    @R0
    D = M

    @sum
    M = M + D // Updates the Sum with D which holds the The Data of R1

    @i
    M = M + 1

    @LOOP
    0; JMP
(END)
    @sum
    D = M

    @R2
    M = D

    @END
    0; JMP