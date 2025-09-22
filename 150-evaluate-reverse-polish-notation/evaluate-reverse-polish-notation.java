class Solution {
    public int evalRPN(String[] tokens) {
        //postfix evaluation using stack
        Stack<Integer> stack=new Stack<>();
        for(String i:tokens){
            if(i.equals("+") || i.equals("*") || i.equals("-") || i.equals("/")){
                int x=(int)stack.pop();
                int y=(int)stack.pop();
                if(i.equals("+")){stack.push(x+y);}
                else if(i.equals("-")){stack.push(y-x);}
                else if(i.equals("*")){stack.push(x*y);}
                else if(i.equals("/")){
                    if(x!=0){stack.push(y/x);}
                    else{stack.push(0);}
                }
            }
            else{
                stack.push(Integer.parseInt(i));
            }
        }
        return stack.peek();
    }
}