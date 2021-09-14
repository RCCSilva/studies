# Chapter 4

## The Process

OS abstract the running program in what is called "process". A process is a piece of instructions that lays still until the OS take it into action. To do that, uses two tools: 1) mechanisms: set of methods / protocols that "[...] implement a needed piece of functionality." (p. 27), like the __context switch__ which enables the capability to stop and restart a program; 2) __policies__: set of algorithms which take the decisions in the OS. For example, to determine what will run, there is a "scheduling policy".

### Machine State

What resources does the running program need in order to achieve its goal?

- Memory (a.k.a. address space): not only holds variables of the program, but also the program itself.
- Register
- Program Counter

### How does a program start?

1. Load the bytes from the disk or SSD into the system's memory.
2. Allocate memory to the program's stack and initialize variables (e.g. `argc` and `argv`)
3. Allocate memory to the heap and, in the future, make sure tha it is as large as the program needs it to be. At least until, the system runs out of physical memory.
4. Initialize tasks:
    + IO: __file descriptors__ (?) `stdin`, `stdout` and `standard error`.

Finally, the OS transfers the control over the CPU to the newly running application by calling an entry point. In C programs, it's the `main()` function.

### What states can a program have?

1. Running: executing instructions in the processor.
2. Ready: it's waiting to be executed, because the OS choose to not run it right now.
3. Blocked: the process is waiting for some event (usually IO) in order to resume it's process.