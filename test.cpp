#include <iostream>
using namespace std;
int a[100];
int b[100];
int c[100];
int d[100];
int rab;
int rad;
int rbc;
int rdc;

int begin()
{

    cout << "pls enter answer a + b (it`s value < or = 100)" << endl;
    cin >> rab;
    if (rab > 100) { system("cls"); cout << "pls enter value < or = 100" << endl; exit(0);}
    cout << "pls enter answer b + c (it`s value < or = 100)" << endl;
    cin >> rbc;
    if (rbc > 100) { system("cls"); cout << "pls enter value < or = 100" << endl; exit(0);}
    cout << "pls enter answer a + d (it`s value < or = 100)" << endl;
    cin >> rad;
    if (rad > 100) { system("cls"); cout << "pls enter value < or = 100" << endl; exit(0);}
    cout << "pls enter answer d + c (it`s value < or = 100)" << endl;
    cin >> rdc;
    if (rdc > 100) { system("cls"); cout << "pls enter value < or = 100" << endl; exit(0);}

    else {
        return rab, rbc, rad, rdc;
    }
}

void loop1() // it`s a + b = rab
{
    int a1 = -1; int b1; int j = 0; int res;

    while (a1 < rab)
    {
        a1 = a1 + 1; b1 = -1;
        while (b1 < rab)
        {
            b1 = b1 + 1;
            res = a1 + b1;

            if (res == rab)
            {
                j = j + 1;
                a[j] = a1;
                b[j] = b1;
            }
        }
    }

}

void loop2() // it`s b + c = rbc
{
    loop1();
    int c1 = -1; int j = 0; int res; //int b1 = -1;


    while (c1 < rbc)
    {
        c1 = c1 + 1;

        for (int i = 0; i < rbc; i++) { 
            res = b[i] + c1; 
            
            if (res == rbc) { cout << b[i] << " + " << c1 << " = " << res << endl; } 
        }
    }

}

void debug()
{
    int choise;
    int res;
    //**************** Debug *********************
    cout << "Hello it`s Debugger, which loop you want fix? (we have 4 loops)" << endl;
    cin >> choise;
    if (choise == 1) {
        cout << "pls enter answer a + b (it`s any value)" << endl;
        cin >> rab;
        loop1();
        for ( int i = 0; i < rab + 2; i++) { res = a[i] + b[i]; if (res == rab) { cout << a[i] << "+" << b[i] << "=" << res << endl; } }



    }
    if (choise == 2) {
        cout << "pls enter answer  b + c (it`s any value)" << endl;
        cin >> rbc;
        loop2();
        for (int i = 0; i < rbc + 2; i++) { res = b[i] + c[i]; if (res == rbc) { cout << b[i] << "+" << c[i] << "=" << res << endl; } }

    }

    //**************** Debug *********************
}

int main()
{
    int res;
    string choise;
    cout << "This program calculates all possible values of a, b, c, d." << endl;
    cout << "a + b" << endl;
    cout << "+   +" << endl;
    cout << "d + c" << endl;
    cout << endl;
    cout << "do you want use debug ? (y/n)" << endl;
    cin >> choise;
    if (choise == "y"){    debug();}
    else {
        begin();
        loop1();
        for (int i = 0; i < rab + 2; i++) { res = a[i] + b[i]; if (res == rab) { cout << "possible value a = " << a[i] << endl; } }
        cout << endl;
        for (int i = 0; i < rab + 2; i++) { res = a[i] + b[i]; if (res == rab) { cout << "possible value b = " << b[i] << endl; } }
    }
return 0;
}