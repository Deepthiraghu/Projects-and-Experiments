#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define CONCOUNT 20
int main(int argc,char *argv[])
{
    char string[1000], word[20][20], unit[20], c;
    int i = 0, j = 0, count = 0;
 FILE *fp;
fp=fopen(argv[1],"r");
// printf("Enter string: ");
char ch;int k=0;
strcpy(word[0],"and");
strcpy(word[1],"or");
strcpy(word[2],"but");
strcpy(word[3],"yet");
strcpy(word[4],"so");
strcpy(word[5],"for");
strcpy(word[6],"although");
strcpy(word[7],"as");
strcpy(word[8],"because");
strcpy(word[9],"if");
strcpy(word[10],"once");
strcpy(word[11],"since");
strcpy(word[12],"that");
strcpy(word[13],"which");
strcpy(word[14],"though");
strcpy(word[15],"when");
strcpy(word[16],"where");
strcpy(word[17],"while");
strcpy(word[18],"until");
strcpy(word[19],"unless");

float rate = 0,dcount=0,tot=0;float avg;
while(1)
{

//      printf("im here");
        int prate=0;
        char t[30];
        ch=fgetc(fp);
        if((int)ch==EOF){ break;}
        while(ch!='.')
        {
                string[k++]=ch;
                ch=fgetc(fp);
        }
    i = 0;
    string[k] = '\0';
    int flag=0;
        printf("%s\n", string);
        int unr=0;
    for (i = 0; i < strlen(string); i++)
    {
        if(i==0)
                flag=1;
        while (i < strlen(string) && !isspace(string[i]) && isalnum(string[i]))
        {
            unit[j++] = string[i++];
        }
        if (j != 0)
        {
            unit[j] = '\0';
            int z=0;

            for(z=0;z<CONCOUNT;z++){
                if (strcmp(unit, word[z]) == 0)
                {
                        count++;
                }
             }

                FILE *fr=fopen("r0.txt","r");

                 fscanf(fr,"%s",t);
                 while(!feof(fr)){
//                      printf("ref : %s\n",t);
                        if(strcmp(unit,t)==0)
                                prate++;
                        fscanf(fr,"%s",t);
                 }
//              printf("word:%s flag:%d prate:%f\n",unit,flag,prate);
                if(prate == 0){
                        if(flag==1){
                                printf("Defect identified: Unrelated definition\n");
                                rate--;
                                flag=0;
                        }
                }
                else if(flag==1)
                {
                        prate=0;
                        flag=0;
                }
           }
                j = 0;
        }


        k=0;
//      printf("No of connectives found:%d\n",count);
        if(prate!=0){
                printf("Positive policy identified : No shifting the topic\n");
                rate++;
        }
        else{
                rate--;
                printf("Defect identified : Doubtful definition\n");

        }

        if(count<2){
                printf("Defect identified : Saying too little\n");
                rate--;
        }
        else if(count>3){
                printf("Defect identified : Saying too much\n");
                rate--;
        }
        else{
                printf("Positive policy identified : One time argument\n");
                rate++;
        }


        printf("Definition Rating: %0.2f\n",rate);
        tot+=rate;
        dcount+=1;
        count=0;
        rate=0;
        char c=fgetc(fp);
}
avg=tot/dcount;
printf("Paper rating: %f",avg);
}
