#include <unistd.h>
#include <stdio.h>

int main(){
    while(1){
        char* cmd = read_command();
        int pid;
        if ((pid = fork()) == 0){
            exec(cmd);
            panic("exec failed!");
        }
        else wait(pid);
    }

}