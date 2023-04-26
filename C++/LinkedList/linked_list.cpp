#include<iostream>

using namespace std;

class Node{
	public:
		int data;
		Node* next;
		
		Node(int d){
			data = d;
			next = NULL;
		}

};

// Linked list class declaration
class LinkedList{
	private:
		Node* head;
	
	public:
		LinkedList(){
			head = NULL;
		}
		
		void addNode(int d){
			Node* newNode = new Node(d);
			if(head == NULL){
				head = newNode;
			}
			else{
				Node* currNode = head;
				while(currNode->next != NULL){
					currNode = currNode->next;
				}
				currNode->next = newNode;
			}
		}
		
		void displayList() {
			Node* currNode = head;
			while (currNode != NULL) {
			    	cout << currNode->data << " ";
			   	 currNode = currNode->next;
			}
			cout << endl;
    }

};

int main() {
    LinkedList list;
    list.addNode(1);
    list.addNode(2);
    list.addNode(3);
    list.addNode(4);
    list.displayList();

    return 0;
}

