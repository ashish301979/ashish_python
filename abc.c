#include<stdio.h>
#include<unistd.h>
int main()
    {
        pid_t x;
        int y, z;
        y = 10;
        z = 20;
        x = fork();
        y = y + z;
        if(x > 0){
            printf(" %d",y);
        } 
        return 0;
    }
