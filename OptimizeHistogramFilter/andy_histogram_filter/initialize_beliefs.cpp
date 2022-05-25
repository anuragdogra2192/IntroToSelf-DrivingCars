#include "headers/initialize_beliefs.h"

using namespace std;

vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {

	// initialize variables for new grid
	vector< vector <float> > newGrid;
  	newGrid.reserve(grid.size());
	
  	vector<float> newRow;
	newRow.reserve(grid[0].size());
  	
  	float prob_per_cell;
	//height = grid.size();
	//width = grid[0].size();
  
	// calculate initial grid values
	prob_per_cell = 1.0 / ( (float) grid.size()*grid[0].size());

	// store initial values in a new 2D grid with same size as grid
	for (int i=0; i<grid[0].size(); i++) 
    {
		newRow.push_back(prob_per_cell);
	}
  	
  	for (int j=0; j<grid.size(); j++)
    {
		newGrid.push_back(newRow);
	}
  
	return newGrid;
}