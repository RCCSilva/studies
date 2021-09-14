# UNIX Api

## `fork()`

Creates a copy of the current process, taking into account the current state of the running process. Hence, it does not start from the entry point, but from the __return__ of the `fork()` command.

## `wait()`

Can be used to __wait__ for the __child__ process to return before running the rest of the code.

## `exec()`

Executes another program. Not by running a new process, but by loading all the static data that it is needed to run the called program in the resource's (heap, stack, other memory spaces) of the current resource. This new program does not return to the old one (it was overwritten).

For example, if we have a program called A and program A executes another program called B, A is transformed into B as if it was never there. The only remains of program A are the `argv` parameters passed to program B.