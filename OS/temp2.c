#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <pthread.h>
#include <wait.h>

int value = 0;
void *runner(void *param){    /* the thread */
    value = 5;
    pthread_exit(0);
}

int main(){
    pid_t        pid;
    pthread_t    tid;
    if ((pid = fork()) == 0)  {
        pthread_create(&tid, NULL, runner, NULL);
        pthread_join(tid, NULL);
        printf("CHILD: value = %d\n", value);    /* LINE C */
    }
    else  {
        wait(NULL);
        printf("PARENT: value = %d\n", value);    /* LINE P */
    }
}            
