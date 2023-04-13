// STACK DATA Structure with POINTERS //

#include<iostream>

using namespace std;

class Stack{

	private:
		// struct to hold the data and pointer to the next node in the stack
		struct Node{   
			int data;
			Node* next;
		};
		
		Node* top; // pointer to the top node in the stack
	
	public:
		Stack(){ //constructer
		top = nullptr; // assigning null value to the pointer
		}
		
		void Push(int val){
			Node* newNode = new Node;
			newNode->data = val;
			newNode->next = top;
			top = newNode;
		}
		
		int Pop(){
			if(top == nullptr){
				cout<<"Error: Stack is empty"<<endl;
				return -1;
			}

			int val = top->data;
			Node* temp = top;
			top = top->next;
			delete temp;
			return val;
		}
		
		int Peek(){
			if (top == nullptr) {
			    cout << "Error: Stack is empty" << endl;
			    return -1;
        		}
        		return top->data;
		}	
};


int main() {
    Stack s;
    s.Push(1);
    s.Push(2);
    s.Push(3);
    cout << s.Pop() << endl;
    cout << s.Peek() << endl;
    cout << s.Pop() << endl;
    cout << s.Pop() << endl;
    cout << s.Pop() << endl;
    return 0;
}
