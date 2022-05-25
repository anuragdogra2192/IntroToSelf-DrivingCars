#include "headers/normalize.h"
using namespace std;

vector< vector<float> > normalize(vector< vector <float> >& grid) {

	float total = 0.0;
	int i;
	int j;
    vector<float> newRow;
  
  	for (i = 0; i < grid.size(); i++)
	{
		for (j=0; j< grid[0].size(); j++)
		{
			total += grid[i][j];
		}
	}

	vector< vector<float> > newGrid;

	for (i = 0; i < grid.size(); i++) {
		newRow.clear();
		for (j=0; j< grid[0].size(); j++) {
			newRow.push_back(grid[i][j] / total);
		}
		newGrid.push_back(newRow);
	}

	return newGrid;
}
