#include<iostream>

using namespace std;

class Node{
	public:
		int data;
		Node* next;
		Node* prev;
	
	Node(int d){
	
		data = d;
		next = NULL;
		prev = NULL;
		
	}
};

class Doubly_LinkedList{
	
	private:
		Node* head;
		Node* tail;
		int size;
	
	public:
		Doubly_LinkedList(){
			head = NULL;
			tail = NULL;
			size = 0;
		}
		
		void PushInFront(int d){
		
			Node* newNode = new Node(d);
			
			if(head==NULL){
				
				head = newNode;
				tail = newNode;
			}
			else{
			
				head->prev = newNode;
				newNode->next = head;
				head = newNode;
							
			}
			size++;
		
		}
		
		void PushInBack(int d){
			Node* newNode = new Node(d);
			if (tail == NULL) {
			    head = newNode;
			    tail = newNode;
			}
			else {
			    tail->next = newNode;
			    newNode->prev = tail;
			    tail = newNode;
			}
			size++;
    }
			
		
		
		void PopFromFront(){
			
			if(head==NULL){
				return;
			}
			Node* temp = head;
			head = head->next;
			if(head != NULL){
				head->prev = NULL;
			}
			delete temp;
			size--;
		
		}
		
		
		void PopFromBack(){
			
			if(tail==NULL){
				return;
			}
			Node* temp = tail;
			tail = tail->prev;
			if(tail != NULL){
				tail->next = NULL;
			}
			delete temp;
			size--;
		
		}
		
		int getSize(){
			return size;
		}
		
		void DisplayList(){
		
			Node* curr = head;
			while(curr != NULL){
				cout<< curr->data <<" ";
				curr = curr->next;
			}
			cout<<endl;
		}

};


int main(){

    Doubly_LinkedList dll;
    
    dll.PushInBack(10);
    dll.PushInBack(20);
    dll.PushInFront(5);
    dll.PushInFront(2);
    dll.PopFromFront();
    dll.PopFromBack();
    
    dll.DisplayList(); // Output: 5 10
    
    return 0;
}
