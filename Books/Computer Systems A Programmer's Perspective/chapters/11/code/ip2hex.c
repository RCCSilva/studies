#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>

void main(int argc, char **argv) 
{
    unsigned char buf[sizeof(struct in_addr)];
    int ip_result = inet_pton(AF_INET, argv[1], buf);

    printf("0x");
    for(int i = 0; i < sizeof(struct in_addr); i++)
    {
        printf("%x", buf[i]);
    }
    printf("\n");
}