#include<iostream>
using namespace std;
#include<vector>

void printSolution(vector<vector<int>>& board,int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(board[i][j]){
                cout<<"Q ";
            }else{
                cout<<"- ";
            }
        }
        cout<<"\n";
    }
    cout<<"\n\n\n";
}

bool isSafe(vector<vector<int>>& board,int row,int col,int n){
     int i=row;
     int j=col;
     while(j>=0){
        if(board[i][j]){
            return false;
        }
        j--;
     }

     i=row;
     j=col;

     while(i>=0 && j>=0){
        if(board[i][j]){
            return false;
        }
        i--;
        j--;
     }

     i=row;
     j=col;

     while(i<n && j>=0){
        if(board[i][j]){
            return false;
        }
        i++;
        j--;
     }

     return true;
}

void solve(vector<vector<int>>& board,int n,int col){
    if(col>=n){
        printSolution(board,n);
        return ;
    }

    for(int row=0;row<n;row++){
        if(isSafe(board,row,col,n)){
            board[row][col]=1;
            solve(board,n,col+1);
            board[row][col]=0;
        }
    }
}
int main(){

    int n;
    cout<<"Enter number of queens : ";
    cin>>n;
    vector<vector<int>>board(n,vector<int>(n,0));
    solve(board,n,0);

    return 0;
}