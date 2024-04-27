#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
    int pid;
    int a, b;
    if ((pid = fork()) == 0){   //child process returns 0.
        int pid1 = getpid();
        printf("child: pid = %d\n", pid);   //pid() child's return values => 0
        printf("child: pid1 = %d\n", pid1); //child's pid1 => 7192
    }
    else{                       //parent process returns non-zero
        int pid1 = getpid();
        printf("parent: pid = %d\n", pid);  //pid() parent's returnn values => 7192
        printf("parent: pid1 = %d\n", pid1);    //parent's pid1 => 7187
    }

    return 0;
}
