#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int pipefd[2];
    int rc[2] = {-99, -99};

    pipe(pipefd);


    rc[0] = fork();
    if (rc[0] > 0)
    {
        rc[1] = fork();
        wait(NULL);
    }

    printf("(PID: %d)\n", (int) getpid());


    if (rc[0] == 0)
    {
        close(pipefd[0]);
        printf("I'm the first child\n");
        char str[] = "Hello, a message from your sister!";
        write(pipefd[1], str, strlen(str));
        return 0;
    }
    
    if (rc[1] == 0)
    {
        close(pipefd[1]); // I don't understand why wee need this haha
        char buf;
        printf("I'm the second child and I'll listen to my sister's message!\n");
        while(read(pipefd[0], &buf, 1))
        {
            write(STDOUT_FILENO, &buf, 1);
        }
        write(STDOUT_FILENO, "\n", 1);

        char message[] = "And that's what she said\n";

        write(STDOUT_FILENO, &message, strlen(message));

        return 0;
    }


    return 0;
}

