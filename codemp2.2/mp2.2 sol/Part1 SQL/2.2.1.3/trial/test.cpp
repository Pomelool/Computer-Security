#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "md5.h"
#include <iostream>
#include <boost/regex.hpp>
#include <string>

using namespace std;
int isAttack(string md5hash) {
	// find a single quote

	// after single quote, should be one or more spaces, and then "or" || "OR" || "oR" || "Or"

	// and then one or more spaces
	return 1;
}
string random_string(int len)
{
   srand(time(0));
   string str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
   int pos;
   while(str.size() != len) {
    pos = ((rand() % (str.size() - 1)));
    str.erase (pos, 1);
   }
   return str;
}
int main()
{
	//int i = 0;
	string s ("3143435");
    regex e ("3*5");
	if(regex_match(s,e)) {
		cout << "true" << endl;
	}
/*
	while(1) {
		// randomly generate a string
		string rdmStr = random_string(30);
		// calculate the md5hash
		string md5hash = md5(rdmStr);
		// validate it, if it's qualified, then break
		cout << rdmStr << endl;
		cout << md5hash << endl;
		if(isAttack(md5hash) > 0) {
			break;	
		}
		break;
	}
	printf("valid attack hash found\n");*/
	return 0;
}
