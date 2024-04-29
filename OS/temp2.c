#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/types.h>

  int value = 0;
  
void *runner(void *param){
    value = 5;
    pthread_exit(0);
}
int main()
{
    int        pid;
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
