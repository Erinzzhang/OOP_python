//
//  main.cpp
//  hw0
//
//  Created by erin on 2018/9/21.
//  Copyright © 2018年 Erin Zhang. All rights reserved.
//

#include <iostream>
#include <vector>


using namespace std;

int main()
{
    int M, N, factor,first,temp;
    vector <int> stack1, stack2;
  
    cout << "plz input first odd number: ";
    cin >> first;
    while (first % 2 == 0)
    {
        cout << "plz input first odd number: ";
        cin >> first;
    }
    
    cout << "plz input N for create numbers: ";
    cin >> N;

    temp = first;
    for(int i= 0; i< N; i++)
    {
        stack1.push_back(temp);
        temp = temp + 2;
    }
    
    cout << "require: M < N, plz input M for select elements: ";
    cin >> M;
    
    while(M > N)
    {
        cout << "require: M < N, N = " << N << endl;
        cout << "plz input M again: ";
        cin >> M;
    }
    
    cout << "plz input number as a factor for select elements: ";
    cin >> factor;
    
    for (int j = 0; j < M; j++)
    {
        int temp2 = 0;
        temp2 = stack1[j];
        if (temp2 % factor == 0)
        {
            stack2.push_back(stack1[j]);
        }
        
    }
    
    cout << "stack1: " << endl;
    for (int m  = 0; m < stack1.size(); m++)
    {
        cout << stack1[m] << " ";
    }
    cout << endl;
    
    cout << "stack2: " << endl;
    if (stack2.size()>0)
    {
        for (int n  = 0; n < stack2.size(); n++)
        {
            cout << stack2[n] << " ";
        }
    }

    cout << endl;
    
    
    return 0;
}
