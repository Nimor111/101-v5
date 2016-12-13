#include <iostream>
#include <string.h>

int find_max_times(const char * string, char ch) {
	int times = 0, max_times = 0;
	for ( int i = 0 ; i < strlen(string); i++) {
		if ( string[i] == ch ) {
			times++;
			while(string[i] == ch) {
				times++;
				i++;
			}
			if ( times > max_times ) max_times = times;
		}
		times = 0;
	}

	return max_times;
}

void heads_and_tails(const char * string) {
	int newLength = 0;
	for ( int i = 0; i < strlen(string); i++) {
		if ( string[i] == 'H' || string[i] == 'T') {
			newLength++;
		}
	}

	char newstr[newLength];
	int newidx = 0;
	for ( int i = 0; i < strlen(string); i++) {
		if ( string[i] == 'H' || string[i] == 'T') {
			newstr[newidx++] = string[i];
		}
	}
	newstr[newidx] = '\0';

	int sizeH = find_max_times(newstr, 'H');
	int sizeT = find_max_times(newstr, 'T');

	if ( sizeH > sizeT ) std::cout << "H wins!" << std::endl;
	else if ( sizeT > sizeH ) std::cout << "T wins!" << std::endl;
	else std::cout << "Draw!" << std::endl;
}

int main()
{
	//examples from github
	heads_and_tails("H, H, H, H, H, T, T, T, T");
	heads_and_tails("H, H, H, H, T, T, T, T");
	heads_and_tails("H, T, H, T, T, H, T");
	heads_and_tails("T, T, T, H, T, T, T, H, T, T, T, H, H, H, H");

	return 0;
}
