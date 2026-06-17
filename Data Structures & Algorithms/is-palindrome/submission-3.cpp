class Solution {
public:
    bool isPalindrome(string s) {
        string alphanums_s = "";
        for(int x : s){
            if (isalnum(x)){
                alphanums_s.push_back(tolower(x));
            }
        }
        // string flip_alphanums_s(alphanums_s.size(), ' ');
        int alphanums_size = alphanums_s.size();
        for(int i = 0; i < alphanums_size; i++){
            if(alphanums_s[i] != alphanums_s[(alphanums_size - 1) - i ]){
                return false;
            }

            // cout << alphanums_size - i << endl;
            // if (flip_alphanums_s[i - 1] != alphanums_s[alphanums_size - i]){
            //     return false;
            // }
        }
        return true;
    }
};
