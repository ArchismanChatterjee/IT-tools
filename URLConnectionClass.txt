

import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class URLConnectionclass
{
public static void main (String args[])
{
try 
{
URL url = new URL("https://innovateindia.mygov.in/ppc-2022/");
URLConnection urlcon= url.openConnection();
Map<String, List<String>> header = urlcon.getHeaderFields();

for (Map.Entry<String, List<String>> mp: header.entrySet()){
System.out.println("\nComplete source code of the URL is---");
System.out.println("---");

BufferedReader br= new BufferedReader(new InputStreamReader(urlcon.getInputStream ()));

String i;
// print the source code line by line 

while(( i = br.readLine()) != null)
{
System.out.println(i);
}
}
}
catch (Exception e) 
{
System.out.println(e);
}
}
}