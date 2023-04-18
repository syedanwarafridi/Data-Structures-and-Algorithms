#include<iostream>

using namespace std;

#define size 20

class Queue{
	
	private:
		int* array;
		int front;
		int back;
		
	public:
		Queue(){
			array = new int[size];
			front = -1;
			back = -1;
		}
		
		void EnQueue(int val){
			if(back==size-1){
				cout<<"Queue overflow"<<endl;
				return;
			}
			back++;
			array[back] =  val;
			
			if(front == -1){
				front++;
			}
		}
		
		void DeQueue(){
			if(front==-1 || front>back){
				cout<<"ERROR: No elements in queue"<<endl;
				return;
			}
			
			front = (front + 1) % size;
			
		}
		
		int Peek(){
			if(front==-1 || front>back){
				cout<<"ERROR: No elements in queue"<<endl;
				return -1;
			}
			return array[front];
		}
		
		bool isEmpty(){
			if(front==-1 || front>back){
				return true;
			}
			return false;
		}
};


int main() {
    Queue q;
    q.EnQueue(5);
    q.EnQueue(10);
    q.EnQueue(15);
    q.DeQueue();
    cout << q.Peek() << endl;
    return 0;
}
