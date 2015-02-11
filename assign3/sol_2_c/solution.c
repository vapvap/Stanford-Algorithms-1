#include <stdio.h>

typedef unsigned char edge[25];

int main() {

	


	return 0;
}

unsigned int ** get_input(const char * filename) {

	FILE * fp;
	unsigned char buf[4096];

	if(!filename) {
		return NULL;
	}

	if(!(fp = fopen(filename, "r"))) {
		return NULL;
	}

	while(1) {
		if(!fgets(
	}
}
