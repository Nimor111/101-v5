#include <iostream>
#include <string.h>

using namespace std;

int solve_sector(const char * string, int & sectorIdx) {
	int liters = 0, countD = 0, countU = 0, numberOfUs = 0;
	bool isEnd = 0;
	for ( int i = sectorIdx; i < strlen(string); i++) {
		if ( string[i] == 'u' ) numberOfUs++;
	}

	while(countD < numberOfUs) {
		if ( string[sectorIdx] == 'd') {
		 	liters += 500 + 1000 * countD; sectorIdx++; countD++;
		 	while ( string[sectorIdx] == 'd' && countD < numberOfUs) {
		 		liters += 500 + 1000 * countD;
		 		countD++;
		 		sectorIdx++;
		 	}
		}
		if ( string[sectorIdx] == 'h') {
			liters += 1000 * countD; sectorIdx++;
			while ( string[sectorIdx] == 'h') {
				liters += 1000 * countD;
				sectorIdx++;
			}
		}
		if ( string[sectorIdx] == 'u' ) {
			countU = countD-1;
			liters += 500 + 1000 * countU; sectorIdx++; countU--; countD--;
			while (string[sectorIdx] == 'u') {
				if ( countD == 0 ) { isEnd = 1; break; }
				liters += 500 + 1000 * countU;
				sectorIdx++; countU--; countD--;
			}
			if ( countD == 0 ) { isEnd = 1; break; }
		}
	}

	if ( !isEnd ) liters = 0;

	return liters;
}

int lakes(const char * string) {
	int liters = 0, sectorIdx = 0;
	while ( sectorIdx != strlen(string) ) {
		for ( int i = sectorIdx; i < strlen(string); i++) {
			if ( string[i] == 'd') { sectorIdx = i; break; }
		}
		liters += solve_sector(string, sectorIdx);
	}
	return liters;
}

int main()
{
	std::cout << lakes("ddhhuu") << std::endl;
	std::cout << "\n\n";
	std::cout << lakes("ddhhddhuhhuuu") << std::endl;
	std::cout << "\n\n";
	std::cout << lakes("dddhhhuuhhuuuhdddduu") << std::endl;

	return 0;
}
