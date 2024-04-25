#include<stdio.h>
#include<ctype.h>
void modifyString(char *str,void (*modifyFunc)(char *)){
    while(*str){
        modifyFunc(str);
    
        str++;
    }
}
void toLowercase(char *c){
    *c=tolower(*c);
}

void toUppercase(char *c){
    *c=toupper(*c);
}
int main(){
    char inputString[100];

    printf("Enter a string:");
    scanf("%99s",inputString);

    printf("original: %s\n",inputString);

    modifyString(inputString,toLowercase);
    printf("lowercase: %s\n",inputString);

    modifyString(inputString,toUppercase);
    printf("uppercase:%s\n",inputString);
    return 0;
}