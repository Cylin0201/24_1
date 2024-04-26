#include <unistd.h>
#include <stdio.h>

int main(){
    int pid;

    if ((pid = fork()) == 0){   //자식 프로세스
        printf("Child PROCESS of %d is %d\n", getppid(), getpid());
    }
    else{                       //부모 프로세스
        printf("I am %d. My child is %d\n", getpid(), pid);
    }
    return 0;
}
