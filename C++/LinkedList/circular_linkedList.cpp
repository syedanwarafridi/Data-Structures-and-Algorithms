#include<iostream>

using namespace std;

class Node{
	
	public:
		int data;
		Node* next;
		
		Node(int val){
			data = val;
			next = NULL;
		}

};

class CircularLinkedList{

	private:
		Node* head;
		int size;
		
	public:
		CircularLinkedList(){
			head = NULL;
			size = 0;
		}
		
		//Push node in front
		void PushInFront(int val){
			Node* newNode = new Node(val);
			if(head == NULL){
			
				head = newNode;
				head->next = head;
			}
			else{
			
				Node* tail = head;
				while(tail->next != head){
					tail = tail->next;
				}
				
				tail->next = newNode;
				newNode->next = head;
				head = newNode;
			}
			size++;
		}
		
		//Push on Back
		void PushInBack(int val){
			Node* newNode = new Node(val);
			
			if(head == NULL){
				head = newNode;
				head->next = head;
			}
			else{
				Node* tail = head;
				while(tail->next != head){
				
					tail= tail->next;
				}
				
				tail->next = newNode;
				newNode->next = head;
				
			}
			size++;
		}
		
		
		//Pop from front
		void PopFromFront(){
		
			if(head == NULL){
				return;
			}
			
			Node* tail = head;
			while(tail->next != head){
				tail = tail->next;
			}
			
			Node* temp = head;
			head = head->next;
			tail->next = head;
			delete temp;
			size --;
			
		}
		
		//pop from back
		void PopFromBack(){
		
			if(head == NULL){
				return;
			}
			
			Node* tail = head;
			while(tail->next->next != head){
				tail = tail->next;
			}
			
			Node* temp = tail->next;
			tail->next = head;
			delete temp;
			size --;
			
		}
		
		   // Function to get the size of the linked list
		int getSize() {
		    return size;
		}

		// Function to print the contents of the linked list
		void printList() {
		    if (head == NULL) {
		        return;
		    }
		    Node* curr = head;
		    do {
		        cout << curr->data << " ";
		        curr = curr->next;
		    } while (curr != head);
		    cout << endl;
		}
};


int main() {
    CircularLinkedList cll;

    cll.PushInBack(10);
    cll.PushInBack(20);
    cll.PushInFront(5);
    cll.PushInFront(2);
    cll.PopFromFront();
    cll.PopFromBack();

    cll.printList(); // Output: 5 10

    return 0;
}

