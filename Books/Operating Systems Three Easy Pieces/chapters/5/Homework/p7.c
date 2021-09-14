#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    printf("(PID: %d)\n", (int) getpid());
    int rc = fork();

    if (rc < 0)
    {
        fprintf(stderr, "Failed to create child process with fork()");
        exit(1);
    } else if (rc == 0)
    {
        printf("CHILD (PID: %d) - Before closing the STDOUT\n", (int) getpid());
        close(STDOUT_FILENO);
        printf("CHILD (PID: %d)\n", (int) getpid());
    } else 
    {
        printf("(PID: %d)\n", (int) getpid());
        int status = 0;
        waitpid(-1, &status, 0);
        printf("This is the response of the wait(): %d\n", WEXITSTATUS(status));
    }
   
    return 0;
}

// The process does not print the text in the terminal, even though the parent keeps doing it.