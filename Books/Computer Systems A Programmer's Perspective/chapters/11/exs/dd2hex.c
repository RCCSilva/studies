// Chapater 11 - Ex 11.3

#include <stdlib.h>
#include <stdio.h>

void main(int argc, char **argv) 
{
    unsigned short hex = (ushort) atoi(argv[1]);
    printf("0x%x\n", hex);
}