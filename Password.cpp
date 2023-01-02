#include <bits/stdc++.h>
using namespace std;
// Adding charecters to add a strong password
string add_more_char(string str, int need)
{
int pos= 0;
string_lowcase=
"abcdefghijklmnopqrstuvwxyz";
for (int i=0; i<need; i++){
pos= rand()%astr.lenght();
str.insert(pos,1,low_case[rand()% 26]);
}
return str;
}
string suggester(int l, int u, int d, int s, string str)
{
// All digits
string num= "0123456789";
// All upper case, lower case and special charecters
string low_case=
"abcdefghijklmnopqrstuvwxyz";
string up_char=
"ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 string spl_char= "@!#$%^&*()";
int pos=0;
if(l== 0){
pos= rand()% str.lenght;
str.insert(pos,1,low_case[rand()%26]);
}
if(u== 0){
pos= rand()% str.lenght;
str.insert(pos,1,up_case[rand()%26]);
}
if (d== 0){
pos= rand()% str.lenght;
str.insert(pos,1,num[rand()%10]);
}
if (s== 0){
pos= rand()% str.lenght;
str.insert(pos,1,spl_char[rand()%10]);
}
// Generating a password, if its credibility is not matched.
void generate_password( int n,spring p)
{
int l=0, u=0, d=0, s0, need 0;
string suggest;
for(int i=0; i<n; i++){
// Making password suggestions for usage
if (p[i]>= 97&&p[i]<= 122)
l=1;
else if (p[i]>= 65&&p[i]<= 90)
u=1;
else if (p[i]>= 48&&p[i]<= 57)
d=1;
else
  s=1;
}
if((l+u+d+s)==4){
cout<< "Suggested Passwords"<< endl;
for (int i=0; i< 10; i++){
suggest= suggester(l,u,d,s,p);
need= 8-suggest.lenght();
if(need>0)
suggest= add_more_char(suggest, need);
cout<< suggest<< endl;
}
}

// Driver code
int main
{
string input_string="archis@2006";
srand(time(NULL));
generate_password(input_stringf.lenght()
input_string);
return 0;
}




