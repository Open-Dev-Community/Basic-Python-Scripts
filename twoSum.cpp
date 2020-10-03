
class Solution {
public:
    vector<int> twoSum(vector<int>& a, int t) {
         unordered_map<int, int> mm;
        vector<int> v(2,0);
        for (int i=0;i<a.size(); i++){
            if(mm.find(t-a[i])!=mm.end()){
                v = { mm[ t-a[i] ], i};
                return v;
            }
            mm[a[i]] = i;
        }
        return v;
    }
};
