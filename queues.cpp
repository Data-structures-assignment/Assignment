class MyStack {
private:
    queue<int> q1;
    queue<int> q2;

public:
    MyStack() {
        // Constructor - no initialization needed
    }
    
    void push(int x) {
        // Push the new element to q2
        q2.push(x);
        
        // Move all elements from q1 to q2
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }
        
        // Swap q1 and q2
        swap(q1, q2);
    }
    
    int pop() {
        if (empty()) {
            return -1; // or throw an exception
        }
        int top_element = q1.front();
        q1.pop();
        return top_element;
    }
    
    int top() {
        if (empty()) {
            return -1; // or throw an exception
        }
        return q1.front();
    }
    
    bool empty() {
        return q1.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
