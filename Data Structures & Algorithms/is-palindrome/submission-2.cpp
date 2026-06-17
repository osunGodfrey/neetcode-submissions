class Solution {
public:
    bool isPalindrome(string s) {
        string alphanums_s = "";
        for(int x : s){
            if (isalnum(x)){
                alphanums_s.push_back(tolower(x));
            }
        }
        string flip_alphanums_s(alphanums_s.size(), ' ');
        int alphanums_size = alphanums_s.size();
        for(int i = alphanums_size; i > 0; i--){
            // cout << alphanums_size - i << endl;
            flip_alphanums_s[i - 1] = alphanums_s[alphanums_size - i];
        }
        // cout << alphanums_s << endl;
        // cout << flip_alphanums_s << endl;
        if (flip_alphanums_s == alphanums_s){
            return true;
        }else{
            return false;
        }
        
        
    }
};
