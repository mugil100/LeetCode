class Solution {
    public String longestCommonPrefix(String[] strs) {

        if(strs.length<1){
            return "";
        }
        else if(strs.length==1){
            return strs[0];
        }
        int curr =0;
        String temp = strs[0];
        int len = temp.length();
        int count = temp.length();
        for(int i=1; i< strs.length;i++){
            
            String word2 = strs[i];
            len = Math.min(word2.length(), temp.length());
            curr=0;
            for(int j=0; j< len; j++){
                if(word2.charAt(j) == temp.charAt(j) ){
                    curr = j+1;
                    System.out.println(count);
                }
                else{
                    break;
                }
            }
            count = Math.min(count,curr);
        }
    return temp.substring(0,count);
    }
}