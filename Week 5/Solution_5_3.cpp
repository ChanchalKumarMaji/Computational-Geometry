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

void solve(vii& P, vii& Q){
    int n = P.size(), q = Q.size();
    int px, py, x, y, dist, h, v;
    for(int i=0; i<q; i++){
        px = Q[i].first; py = Q[i].second;
        dist = INF;
        for(int j=0; j<n; j++){
            x = P[j].first; y = P[j].second;
            h = abs(x-px); v = abs(y-py);
            dist = min(dist, max(h, v));
        }
        cout << dist << endl;
    }
}


int main(){
    int n; cin >> n;
    int x, y;
    vii P(n, ii());
    for(int i=0; i<n; i++){
        cin >> x >> y;
        P[i] = ii(x, y);
    }
    int q; cin >> q;
    vii Q(q, ii());
    for(int i=0; i<q; i++){
        cin >> x >> y;
        Q[i] = ii(x, y);
    }
    solve(P, Q);

return 0;
}
//===================================================================================================================================================

