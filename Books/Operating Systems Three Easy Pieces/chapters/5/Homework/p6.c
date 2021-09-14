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
        printf("CHILD (PID: %d)\n", (int) getpid());
        // int rc_wait = waitpid(NULL, NULL, NULL);
        // printf("CHILD - This is the response of the wait(): %d\n", rc_wait);
        return 4;
    } else 
    {
        printf("(PID: %d)\n", (int) getpid());
        int status = 0;
        waitpid(-1, &status, 0);
        printf("This is the response of the wait(): %d\n", WEXITSTATUS(status));
    }
   
    return 0;
}

// wait() suspends the current process until the child terminates. 
// With waitpid() we can specify the PID and also can return on different status changes