#include "headers/sense.h"

using namespace std;

vector< vector <float> > sense(char color, vector< vector <char> >& grid, vector< vector <float> >& beliefs,  float p_hit, float p_miss) 
{
	vector< vector <float> > newGrid;
    newGrid.reserve(grid.size());
	
  	vector<float> newRow;
	newRow.reserve(grid[0].size());
  
	float p;
	int i, j;
	//height = grid.size();
	//width = grid.size();

	for (i=0; i<grid.size(); i++) 
    {
		newRow.clear();
		for (j=0; j<grid[0].size(); j++) 
        {
			if (grid[i][j] != color)
            {
				p = beliefs[i][j] * p_miss;
			}
          	else 
            {
				p = beliefs[i][j] * p_hit;
			}
			newRow.push_back(p);
		}
		newGrid.push_back(newRow);
	}
	return newGrid;
}
