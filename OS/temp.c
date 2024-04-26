#include <unistd.h>
#include <stdio.h>

int main(){
    int pid = fork();

    if (pid == 0){
        printf("Child PROCESS of %d is %d\n", getppid(), getpid());
    }
    else{
        printf("I am %d. My child is %d\n", getpid(), pid);
    }
    return 0;
}
