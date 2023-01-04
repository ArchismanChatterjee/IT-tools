#include<stdio.h>
int main(){
int r[10],num,i,Rs=0;
printf("Enter the number of Resistances:");
scanf("%d",&num);
printf("\nEnter the value of each Resistence:n");
for (i=0; i<num;i++){
printf("\nR%d:",i+1);
scanf("%d",&r[i]);
}
for(i=0;i<num;i++){
Rs= Rs+ r[i];
}
printf("\nEnter the value of each Resistence:%d Kohm", Rs);
return(0);
}