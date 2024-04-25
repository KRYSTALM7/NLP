#include<stdio.h>
#include<string.h>
int main(){
    char name;
print("Enter your name:");
scanf("%s",name);
if( strcmp(name,"jane") == 0)
       printf("Hello,jane!\n");
       return 0;
}