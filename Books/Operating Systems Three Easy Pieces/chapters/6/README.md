# Chapter 6

How to create a process?

## Simple solution: limited direct execution

As the "direct execution" states, the OS just loads the program and let it run directly in the CPU. But how is the OS able to control it after it starts running? How to control which resources the running application can or cannot access? How the "limited" plays it role?

### Restrict Operations

Applications run in a __processor mode__ called __user mode__. While running in the mode, the program cannot attempt to issue an IO request. If so, it would likely be killed by the OS. In order to achieve this goal, it needs to move to another processor mode: __kernel mode__. Code that is running in this mode can have access to any restricted operation that it likes.

But the running application cannot run itself in __kernel model__. No. That would expose all the system to malicious behavior (reading the memory of other process, reading unauthorized files, etc.). In order to have access to privileged operations, the application must execute a __system call__. A __system call__ enables the kernel to expose restricted operations without completely exposing itself. By carefully placing values in registers or in the stack and executing a special __trap command__, the system jumps to __kernel mode__ where it load the values placed inside the memory or register. After verifying if the process has authorization to call the specific command, it executes it. Once it's done, the kernel loads the caller program back into memory, registers, PC, etc. and give it control over the CPU where it can resume operations in __user mode__.

### Switching Between Processes

How is the OS able to have control over the CPU? By definition, once it gives control to a process it cannot stop it until some sort of trap instruction is executed. Given that, without any help from the hardware, the OS would only be able to gain control if and only if the running process "wants it" (cooperative approach). This solution leads to some problems: 1) What would the OS do if a program halts or goes into a infinite loop? 2) The OS has passive approach over the handling of processes.

In contrast to the cooperative approach, we have the non-cooperative approach. With some help given by the hardware, the OS is able to set a __timer interrupt__. In boot time, it is able to set a __interrupt handler__, which is called in periodic periods. Thus the OS has a periodic control over the CPU and it can decide to resume the running program, interrupt it, start a new process, etc.

To switch processes, the OS basically runs a low assembly code called __context switch__. The program saves the registers of the running program in the Kernel stack and loads the soon-to-be-executing registers, PC and stack. Finally, by calling a return-from-trap instruction, the system starts running the other process.

Take into account that switching processes require __two__ save/load of registers. First, the kernel saves the registers of the running process A in the kernel stack when "switching" from the running program to the OS. Second, if the OS decides to switch context, it explicitly saves the registers of the running process A in the memory inside the designed structured of the process. Finally, it loads the registers of process B __inside the kernel stack__  and, by doing that, the current state of the system is as if the trap was called from the new process B.
