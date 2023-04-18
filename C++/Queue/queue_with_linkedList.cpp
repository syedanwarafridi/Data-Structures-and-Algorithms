#include<iostream>

using namespace std;

class Node{

	public:
		int data;
		Node* next;
		
		//constructor
		Node(int d){
			data = d;
			next = NULL;
		}
};

class Queue{
	
	private:
		Node* front;
		Node* rear;
	
	public:
		//constructor
		Queue(){
			front = NULL;
			rear = NULL;
		}
		
		bool isEmpty(){
			return front == NULL;
		}
		
		void EnQueue(int data){
			Node* newNode = new Node(data);
			
			if(rear == NULL){
				front = newNode;
				rear = newNode;
			}
			else{
				rear->next = newNode;
				rear = newNode;
			}
		}
		
		int DeQueue(){
			if(isEmpty()){
				cout<<"Queue is empty"<<endl;
				return -1;
			}
			
			Node* temp = front;
			int data = front->data;
			
			if(front == rear){
				front = NULL;
				rear = NULL;
			}
			else{
				front = front->next;
			}
			
			delete temp;
			return data;
		}	
		
		void Display(){
			Node* current = front;
			if (isEmpty()) {
				cout << "Queue is empty." << endl;
				return;
			}
			
			cout<<"Queue: ";
			while(current != NULL){
				cout<<current->data<<" ";
				current = current->next;
			}
			cout<<endl;
		}	
			
};


int main() {
    Queue q;

    q.EnQueue(10);
    q.EnQueue(20);
    q.EnQueue(30);
    q.Display();

    cout << "Dequeued: " << q.DeQueue() << endl;
    q.Display();

    q.EnQueue(40);
    q.Display();

    cout << "Dequeued: " << q.DeQueue() << endl;
    q.Display();

    cout << "Dequeued: " << q.DeQueue() << endl;
    q.Display();

    cout << "Dequeued: " << q.DeQueue() << endl;
    q.Display();

    return 0;
}
