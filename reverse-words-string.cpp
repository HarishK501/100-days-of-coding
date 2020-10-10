#include <iostream>
#include <string>

using namespace std;

string reverse(string str)
{
    char temp;
    int st = 0;
    int end = str.length() - 1;
    for (int i = 0; i < str.length() / 2; i++)
    {
        temp = str[st];
        str[st] = str[end];
        str[end] = temp;
        st += 1;
        end -= 1;
    }
    return str;
}

int main()
{
    cout << "Type # to exit" << endl;
    string str, word, result;
    while (1)
    {
        word = "";
        result = "";
        cout << "Enter a string: \n";
        getline(cin, str);
        if (str == "#")
        {
            break;
        }
        str = reverse(str);
        cout << "\nOUTPUT:\n";
        for (int i = 0; i < str.length(); i++)
        {
            if (str[i] == ' ')
            {
                result = result + reverse(word) + " ";
                word = "";
            }
            else
            {
                word += str[i];
            }
        }
        result += reverse(word);

        cout << result << "\n\n";
    }
    return 0;
}