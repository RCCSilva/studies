#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char const *argv[])
{
    int x = 100;

    printf("(PID: %d) X=%d\n", (int) getpid(), x);


    // Close STDOUT descriptor
    close(STDOUT_FILENO);

    // Opens file descriptor
    open("./p2.output", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);

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

// Parent and child may share the file descriptor to the same file, appending their outputs to it.