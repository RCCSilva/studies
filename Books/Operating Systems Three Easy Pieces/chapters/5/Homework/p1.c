#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
    int x = 100;

    printf("(PID: %d) X=%d\n", (int) getpid(), x);

    int rc = fork();

    if (rc < 0)
    {
        fprintf(stderr, "Failed to create child process with fork()");
        exit(1);
    } else if (rc == 0)
    {
        printf("(PID: %d) Child process x=%d\n", (int) getpid(), x);
        x += 100;
        printf("(PID: %d) Child process x=%d\n", (int) getpid(), x);
    } else 
    {
        printf("(PID: %d) Main process x=%d\n", (int) getpid(), x);
        x += 100;
        printf("(PID: %d) Main process x=%d\n", (int) getpid(), x);
    }

    
    return 0;
}

// The child process has the same variable values of the parent until the last create the former.
// After that, each process has its own variables and if one of them update the value of a "shared" variable
// this is only valid in the current process.