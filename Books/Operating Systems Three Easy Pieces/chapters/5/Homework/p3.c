#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>

int main(int argc, char const *argv[])
{
    int x = 100;

    printf("(PID: %d) X=%d\n", (int) getpid(), x);


    // Close STDOUT descriptor
    close(STDOUT_FILENO);

    // Opens file descriptor
    open("./p3.output", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);

    int rc = fork();

    if (rc < 0)
    {
        fprintf(stderr, "Failed to create child process with fork()");
        exit(1);
    } else if (rc == 0)
    {
        printf("hello");
    } else 
    {
        wait(NULL);
        printf("goodbye");
    }

    
    return 0;
}

// As soon as we call `fork()`, the responsible to make it run or not is the scheduler. Since the process to choose
// which process will run or not, it's impossible to assert something determistic regarding which will run first (the child or the parent).
// Only with the `wait()` command, we can have some assurance about it.