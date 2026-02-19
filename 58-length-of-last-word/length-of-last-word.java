class Solution {
    public int lengthOfLastWord(String s) {

        String sub_str;
        int find=0,i;
        int lind = s.length()-1;
        
        for(i=0; i<s.length();i++){
            if(s.charAt(i) !=' '){
                lind = i;
                System.out.println("lind :"+lind);
                if(i>0 && s.charAt(i-1)== ' '){
                    find =i;
                    System.out.println("find :"+find);
                }
            }
        }
        sub_str = s.substring(find,lind+1);
        System.out.println(sub_str);
        return sub_str.length();

        
    }
}