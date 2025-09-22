class Solution {
    //using strinbuilder
    public String simplifyPath(String path) {
        Stack<String> st=new Stack<>();
        StringBuilder sb=new StringBuilder("");
        String[] component=path.split("/");
        for(String i:component){
            if(i.equals(".") || i.equals("")){
                continue;
            }
            else if(i.equals("..")){
                if(!st.isEmpty()){
                    st.pop();
                }
            }
            else{
                st.push(i);
            }
        }
        
        while(!st.isEmpty()){
            sb.insert(0,"/"+st.pop());
        }
        return sb.length()==0?"/":sb.toString();
    }
}