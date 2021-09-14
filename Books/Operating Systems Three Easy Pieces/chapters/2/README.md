# Chapter 2

What makes it possible to run programs in a simple way?

## Operation System (OS): 

The body of software that makes it easy to run programs. It handles the resources of each running application (memory, devices, etc.), by __virtualizing__ the physical hardware in a general purpose, ease to use "virtual of itself" (often called __virtual machine__).

The OS, overhaul, works like a __resource manager__, exposing APIs to the running programs in order to allocate memory, access the filesystem and others.

### CPU

If we run the `cpu` program, we can see that it's possible to have multiple instances of the same application running as if they are running simultaneously. The responsible for this __illusion__ is the OS making sure that we have as many (almost)  __virtual__ resources to run our program (CPU, memory, etc.).

```shell script
./cpu "A" & ./cpu "B" & ./cpu "C"
```

### Memory

It is the same for the memory, as you can see while running the `memory.c` program. Make sure to disable the ASLR in your machine (Address Space Layout Randomization) with the fallowing command: `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`. And don't forget to enable it again after the test: `echo 2 | sudo tee /proc/sys/kernel/randomize_va_space`.

```shell script
./memory & ./memory
```

### Concurrency

Tha capability to run multiple programs and even multiple threads of the same program at the same time. The OS is able to run each application as if it had its own CPU.

```shell script
./thread 1000
```

### Persistence

"The software in the operating system that usually manages the disk is called the file system; it is thus responsible for storing any files the user creates in a reliable and efficient manner on the disks of the system." (p. 11)


