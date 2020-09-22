#include <iostream>
#include <string>

using namespace std;

int main(){
    cout << "Type # to exit" << endl;
    string str;
    int st, end, temp;
    while(1){
        cout << "Enter a string: ";
        getline(cin, str);
        if(str == "#"){
            break;
        }
        st = 0;
        end = str.length() - 1;
        for (int i = 0; i < str.length()/2; i++){
            temp = str[st];
            str[st] = str[end];
            str[end] = temp;
            st += 1;
            end -= 1;
        }
        cout << str << "\n";
        
    }
    return 0;
    
}