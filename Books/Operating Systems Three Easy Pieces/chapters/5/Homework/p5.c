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
        printf("(PID: %d)\n", (int) getpid());
        int rc_wait = wait(NULL);
        printf("CHILD - This is the response of the wait(): %d\n", rc_wait);
        return 1;   
    } else 
    {
        printf("(PID: %d)\n", (int) getpid());
        int rc_wait = wait(NULL);
        printf("This is the response of the wait(): %d\n", rc_wait);
    }
   
    return 0;
}

// The wait() returns the PID of the child process.
// wait() in the child process returns -1.