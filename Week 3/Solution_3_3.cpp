#include<iostream>
#include<fstream>
#include<bitset> 
#include<vector>
#include<set>
#include<map>
#include<stack> 
#include<queue>
#include<algorithm> 
#include<numeric>
#include<string> 
#include<cstdio> 
#include<cmath>
#include<sstream>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 1000000000

//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "VECTOR" objects 
template<typename T>
ostream& operator << (ostream& o, const vector<T>& v){
    o << "[ ";
    for(int i=0; i<v.size(); i++){
        o << v[i];
        if(i != v.size()-1)
            o << ", ";  
    }     
    o << " ]"; // To include new lines in 2d vectors put " o << " ]\n" " 
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "SET" elements 
template<typename T>
ostream& operator << (ostream& o, const set<T>& s){
    o << "[ ";
    for(auto it : s){
        o << it;
        if(it != *s.rbegin())
            o << ", ";
    }
    o << " ]";
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "MAP" elements 
template<typename T, typename S>
ostream& operator << (ostream& o, const map<T, S>& m){
    for(auto it : m)
        o << it.first << " : " << it.second << "\n";
    return o;    
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "PAIR" class
template<typename T, typename S>
ostream& operator << (ostream& o, const pair<T, S>& p){
    o << "( ";
    o << p.first << ", " << p.second << " )";
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "STACK" objects 
template<typename T>
ostream& operator << (ostream& o, const stack<T>& s){
    o << "[ ";
    stack<T> temp = s;
    while(!temp.empty()){
        o << temp.top();
        temp.pop(); 
        if(temp.size() >= 1)
            o << ", ";  
    }
    o << " ]";
    return o;
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "QUEUE" objects
template<typename T>
ostream& operator << (ostream& o, const queue<T>& q){
    o << "[ ";
    queue<T> temp = q;
    while(!temp.empty()){
        o << temp.front();
        temp.pop(); 
        if(temp.size() >= 1)
            o << ", ";  
    }
    o << " ]";
    return o;
}
//----------------------------------------------------------------------------------------------------------------------------------------------------
// Code to print "PRIORITY QUEUE" elements 
template<typename T>
ostream& operator << (ostream& o, const priority_queue<T>& q){
    o << "[ ";
    priority_queue<T> temp = q;
    while(!temp.empty()){
        o << temp.top();
        temp.pop(); 
        if(temp.size() >= 1)
            o << ", ";  
    }
    o << " ]";
    return o;
}
//----------------------------------------------------------------------------------------------------------------------------------------------------
//===================================================================================================================================================
// Your Code starts here

int N = 2*(1e6) + 1;
vi t = vi(2*N, 0);

void update(int p, int value) {
    p += 1e6;
    p += N;
    t[p] = value;
    for(; p>1; p = p/2) t[p/2] = t[p] + t[p^1];
}

int sumRange(int l, int r) { // sum on interval [l, r]
    l += 1e6;
    r += 1e6;
    l = l+N; r = r+N+1;
    int res = 0;
    for(; l<r; l=l/2, r=r/2){
        if(l&1) res += t[l++];
        if(r&1) res += t[--r];
    }
    return res;
}

int solve(vector<vi>& P){
    int n = P.size();
    vector<vi> A;
    for(int i=0; i<n; i++){
        int p1x, p1y, p2x, p2y;
        p1x = P[i][0]; p1y = P[i][1]; p2x = P[i][2]; p2y = P[i][3];
        if(p1x == p2x){
            A.push_back(vi({p1x, 0, p1y}));
            A.push_back(vi({p2x, 0, p2y}));
        }
        else{
            A.push_back(vi({p1x, -1, p1y}));
            A.push_back(vi({p2x, 1, p2y}));
        }
    }
    sort(A.begin(), A.end());
    //cout << A << endl;
    int i = 0;
    int res = 0;
    while(i < A.size()){
        if(A[i][1] == 0){
            int l = A[i][2], h = A[i+1][2];
            i += 2;
            res += sumRange(l, h);
        }
        else if(A[i][1] == -1){
            update(A[i][2], 1);
            i += 1;
        }
        else if(A[i][1] == 1){
            update(A[i][2], 0);
            i += 1;
        }
    }
    return res;
}


int main(){
    int n; cin >> n;
    vector<vi> P;
    for(int i=0; i<n; i++){
        int p1x, p1y, p2x, p2y;
        cin >> p1x >> p1y >> p2x >> p2y;
        P.push_back(vi({min(p1x, p2x), min(p1y, p2y), max(p1x, p2x), max(p1y, p2y)}));
    }
    cout << solve(P) << endl;

return 0;
}
//===================================================================================================================================================

