/*-----------------------------------------------------------------------------------------
* A simple implementation of the BC_model Model to predict whether tumor is malignant (-1) or benign(1)
* 
* written by: Xige Yang
* Feb. 10, 2018
-----------------------------------------------------------------------------------------*/

#ifndef _BC_MODEL
#define _BC_MODEL
#include <iostream>
#include <vector>
#include <cstdio>
#include <time.h>
#include <algorithm>
#include <math.h>

#define T_TOTAL		699
#define T_TRING		499

using namespace std;

class BC_model
{
public:
	BC_model(float h, int e);
	void train(vector< vector<float> > const &X, vector<int> const &y);
	int predict(vector<float> const &X);
	void test(vector< vector<float> > const &X, vector<int> const &y);
private:
	float netInput(vector<float> const &X);
	float bias = 1;
	vector<float> m_w;
	float eta;
	float epochs;
};

BC_model::BC_model(float h, int e)
{
	eta = (float)h;
	epochs = (int)e;
}

void BC_model::train(vector< vector<float> > const &X, vector<int> const &y)
{
	m_w = vector<float>(X[0].size());
	vector<int> m_err;
	cout << "Started Training" << endl;
	for(int i = 0; i < epochs; i++)
	{
		int errors = 0;
		for(int j = 0; j < X.size(); j++)
		{
			float update = eta * (y[j] - predict(X[j]));
			//m_w += X[j] * update;
			for(int q = 0; q < m_w.size(); q++)m_w[q]+=X[j][q]*update;
			bias += update;
			errors += update!=0 ? 1 : 0;
		}
		printf("Errors at Epoch %d: %d", i+1, errors);
		printf("\t Accuracy: %0.2f\n", (float)(100-errors)/100);
		//Adaptive Learning Rate
		if(errors==0)break;
		m_err.push_back(errors);
	}
}

void BC_model::test(vector< vector<float> > const &X, vector<int> const &y)
{
	int error = 0;
	for(int i = 0; i < X.size(); i++)
	{
		int ans = predict(X[i]);
		if(ans!=y[i])error++;
	}
	cout << "Accuracy on Test: " << (float)(199-error)/199 << endl;
}

float BC_model::netInput(vector<float> const &X)
{
	float sum = bias;
	for(int i = 0; i < X.size(); i++){
		sum += m_w[i]*X[i];
	}
	return tanh(sum);
}

int BC_model::predict(vector<float> const &X)
{
	return netInput(X)>=0 ? 1 : -1;
}

#endif