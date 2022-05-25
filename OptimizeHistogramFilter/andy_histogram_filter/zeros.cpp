#include "headers/zeros.h"

using namespace std;

vector < vector <float> > zeros(int& height, int& width) {
	int i, j;
	vector < vector <float> > newGrid;
  	newGrid.reserve(height);
	vector <float> newRow;
  	newRow.reserve(width);
	
  	for(i=0; i<width; i++)
    {
    	newRow.push_back(0.0);
    }
  	for(j=0; j<height; j++)
    {
      newGrid.push_back(newRow);
    }
  
	return newGrid;
}