class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_map<int,int> cftwo; // count_frequency-of twice of element

        // counting the frequnecy of each number 
        //{
                // 7: 1, 1: 1, 5: 2, 4: 2, 3: 1,
                //  6: 1, 0: 1, 9: 1, 8: 1, 2: 1
            // }

        for(auto num:nums){
                cftwo[num]++;
        }

        vector<int> result; //for resultant vector that we have to return 

        for(auto pair:cftwo){     //after counting its frequnecy then if it appears twice the push into the resultant vector called result.

           //.second checks the frequency of the vector(values )
            if(pair.second==2){
                result.push_back(pair.first); // .first checks the keys in the vector
            }
        }
        return result;

    }
};