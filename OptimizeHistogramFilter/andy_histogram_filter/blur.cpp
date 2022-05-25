#include "headers/blur.h"

using namespace std;

vector < vector <float> > blur(vector < vector < float> >& grid, float blurring) {

	// initialize variables
	vector < vector <float> > window;
	vector < vector <float> > newGrid;
	vector <float> row;
	vector <float> newRow;

	int height;
	int width;
	float center, corner, adjacent;

	height = grid.size();
	width = grid[0].size();

	// calculate blur factors
	center = 1.0 - blurring;
	corner = blurring / 12.0;
	adjacent = blurring / 6.0;

	int i, j;
	float val;

	// 2D vector reprenting the blur filter
  	window = {
      		  {corner, adjacent, corner},
              {adjacent, center, adjacent},
              {corner, adjacent, corner}
             };

	// variables for blur calculations
	vector <int> DX;
	vector <int> DY;

	DX.push_back(-1); DX.push_back(0); DX.push_back(1);
	DY.push_back(-1); DY.push_back(0); DY.push_back(1);

	int dx;
	int dy;
	int ii;
	int jj;
	int new_i;
	int new_j;
	float multiplier;
	float newVal;

	// initialize new grid to zeros
	for (i=0; i<height; i++) {
		newRow.clear();
		for (j=0; j<width; j++) {
			newRow.push_back(0.0);
		}
		newGrid.push_back(newRow);
	}

	// blur the grid and store in a new 2D vector
	for (i=0; i< height; i++ ) {
		for (j=0; j<width; j++ ) {
			val = grid[i][j];
			newVal = val;
			for (ii=0; ii<3; ii++) {
				dy = DY[ii];
				for (jj=0; jj<3; jj++) {
					dx = DX[jj];
					new_i = (i + dy + height) % height;
					new_j = (j + dx + width) % width;
					multiplier = window[ii][jj];
					newGrid[new_i][new_j] += newVal * multiplier;
				}
			}
		}
	}

	return newGrid;
}
