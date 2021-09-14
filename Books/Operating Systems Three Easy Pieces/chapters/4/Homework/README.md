# Answers

## 1

Since all the processes have 100% chance of being CPU tasks. The use of the CPU will be 100%. The processor will always have a task to execute until process 0 and 1 are finished.

## 2

It takes 10 clocks. The process 0 runs first and, since all 4 tasks are CPU, it takes 4 clocks to run. The process 1 run after but only with 1 task of type IO which takes 5 clocks by default. Thus it takes 9 clocks to run execute all commands. 

_Even though the process takes 10 clocks, it's executing tasks or waiting in 9 of them. So looks like, we can discard the 10th clock_.

## 3

Now, it takes less clocks to run the program. Only 6. We are using the the process more efficiently now. By having the 1 task IO program running first, we can have the scheduler running the PID 1 at the same time that it waits for the PID 0 IO to complete.

## 4

It takes the exact same clocks to complete both tasks, since the CPU is "blocked" waiting for PID 0 IO to finish in order to move to the next process.

## 5

We go back to the previous behavior, where the scheduler switches to the next task while the PID 0 IO is not finished.

## 6

The scheduler switches the process to another process when an IO happens. It also schedules the process responsible for the IOto the end of the queue once the IO finishes. This is not as efficient as it could be. Probably, a better approach, since PID 0 consists of IO only tasks, would be to have process running immediately after the IO finishes.

## 7

Instead of 27 clocks, it took 18 now. That is due to the fact that PID 0, which consists of IO only tasks, was resumed as soon as the IO had finished.

## 8

