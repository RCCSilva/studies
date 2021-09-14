## Compilation System

```c
#include <stdio.h>
int main() {
    printf("hello, world\n");
    return 0;
}
```

How does the system converts this source file into an executable one?

1. Preprocessing: Replaces the headers inside the text file. For example, "stdio.h" is replaced by the actual code
    + Input: hello.c (text file)
    + Output: hello.i (text file)

2. Compilation: Creates the assembly language program based on "hello.i". The output is a text file, "hello.s"

3. Assembly: Takes the assembly language program (text file) and translates it to machine code

4. Linking: Finally, since our program uses the `printf()`


## Hardware Organization

1. Buses: sends _words_ back and forth between devices.

2. IO Devices are connected to the IO Bus though a controller or adapter.

3. Main Memory: temporarily holds data in arrays of bytes.

4. Processor: executes commands placed in the main memory given the PC (program counter). Inside it, the ALU is responsible to perform simple arithmetic and logical operations: 1) load data from the main memory into a register; 2) store a register data inside the main memory; 3) perform an operation with two register's _words_ and store the result inside a register; 4) jump to a PC.

