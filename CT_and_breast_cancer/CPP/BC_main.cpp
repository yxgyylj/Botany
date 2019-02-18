/*-----------------------------------------------------------------------------------------
* A simple implementation of the BC_model Model to predict whether tumor is malignant (-1) or benign(1)
* 
* written by: Xige Yang
* Feb. 10, 2018
-----------------------------------------------------------------------------------------*/

#include <iostream>
#include <vector>
#include <cstdio>
#include <time.h>
#include <algorithm>
#include <math.h>
#include "BC_model.h"

using namespace std;

/*--------------------- Utility functions -- processing data ----------------------------*/
void loadIris(vector< vector<float> > &X, vector<int> &y)
{
	srand(time(NULL));
	freopen("iris.train", "rt", stdin);
	X = vector< vector<float> >(100, vector<float>(4));
	y = vector<int>(100);
	vector< vector<float> > temp(100, vector<float>(5));
	for(int i = 0; i < 100; i++)for(int j = 0; j < 5; j++)cin >> temp[i][j];	
	random_shuffle(temp.begin(), temp.end());
	for(int i = 0; i < 100; i++)
	{
		for(int j = 0; j < 4; j++)X[i][j] = temp[i][j];
		y[i] = temp[i][4];
	}
}

void loadBC(vector< vector<float> > &X, vector<int> &y,vector< vector<float> > &test_X, vector<int> &test_y)
{
	srand(time(NULL));
	freopen("BC.train", "rt", stdin);
	X = vector< vector<float> >(200, vector<float>(9));
	y = vector<int>(200);
	vector< vector<float> > temp;

	for(int i = 0; i < T_TOTAL; i++)
	{
		temp.push_back(vector<float>());
		for(int j = 0; j < 11; j++)
		{
			int a;
			cin >> a;
			temp.back().push_back(a);
		}
		if(temp.back().back()==4)temp.back().back() = 1;
		if(temp.back().back()==2)temp.back().back() = -1;
	}

	for(int i = 0; i < T_TOTAL; i++)temp[i].erase(temp[i].begin());

	for(int i = 0; i < 200; i++)
	{
		for(int j = 0; j < 9; j++)
		{
			X[i][j] = temp[i][j];
		}
		y[i] = temp[i][9];
	}

	test_X = vector< vector<float> >(T_TRING, vector<float>(9));
	test_y = vector<int>(T_TRING);

	for(int i = 0; i < T_TRING; i++)
	{
		for(int j = 0; j < 9; j++)
		{
			test_X[i][j] = temp[i+200][j];
			//cout << X[i][j] << " ";
		}
		test_y[i] = temp[i+200][9];
		//cout << y[i] << endl;
	}
}



int main()
{
	BC_model model(0.01, 100);
	vector< vector<float> > X;
	vector<int> y;
	vector< vector<float> > test_X;
	vector<int> test_y;
	loadBC(X,y,test_X,test_y);
	model.train(X,y);
	model.test(test_X,test_y);
	return 0;
}
