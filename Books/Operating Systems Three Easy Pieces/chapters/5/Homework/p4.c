#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    int rc = fork();

    if (rc < 0)
    {
        fprintf(stderr, "Failed to create child process with fork()");
        exit(1);
    } else if (rc == 0)
    {
        char *myargs[2];
        myargs[0] = strdup("/bin/ls");
        myargs[1] = NULL;
        execv(myargs[0], myargs);    
    } else 
    {
        wait(NULL);
    }
   
    return 0;
}

// Each exec performs a different way to load the parameters and the possibility to set the environment or not.