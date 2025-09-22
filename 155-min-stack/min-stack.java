class MinStack {
    //using 2 stacks
    Stack<Integer> stack1;
    Stack<Integer> stack2;
    int min=Integer.MAX_VALUE;
    public MinStack() {
        stack1=new Stack<>();
        stack2=new Stack<>();
    }
    
    public void push(int val) {
        stack1.push(val);
        min=Math.min(val,min);
        stack2.push(min);
    }
    
    public void pop() {
        stack1.pop();
        if(!stack2.isEmpty()){
            stack2.pop();
        }
        if(!stack2.isEmpty()){
        min=stack2.peek();}
        else{min = Integer.MAX_VALUE;}
    }
    
    public int top() {
        return stack1.peek();
    }
    
    public int getMin() {
        return stack2.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */