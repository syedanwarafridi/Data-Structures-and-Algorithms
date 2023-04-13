// STACK DATA STRUCTURE //

#include<iostream>
#include<string>

using namespace std;

class Stack{
	private:
		int top;
		int array[5];
	
	public:
		// Default Constructor
		Stack()
		{
			top = -1;
			for(int i = 0; i < 5; i++){
				array[i] = 0;
			}
		}
		// We will check here wether the stack is empty or not
		bool isEmpty()
		{
			if(top == -1)
				return true;
			else
				return false;
		}
		
		bool isFull()
		{
			if (top==4)
				return true;
			else
				return false;
		}
		
		void Push(int val)
		{
			if(isFull())
			{
				cout<<"Stack Overflow"<<endl;
			}
			else
			{
				top++;
				array[top] = val;
			}		
		}
		
		int Pop()
		{
			if(isEmpty())
			{
				cout<<"Stack is Underflow"<<endl;
				return 0;
			}
			else
			{
				int popValue = array[top];
				array[top] = 0;
				top--;
				return popValue;
			}
		}
		
		int Count()
		{
			return(top + 1);
		}
		
		int Peak(int pos)
		{
			if(isEmpty())
			{
				cout<<"Stack is Underflow"<<endl;
				return 0;
			}
			else
			{
				return array[pos];
			}
		}
		
		void Change(int pos, int val)
		{
			array[pos] = val;
			cout<<"Value changed at location: "<<endl;
		}
		
		void Display()
		{
			cout<<"All values in stack are: "<<endl;
			for(int i = 4; i >0; i--)
			{
				cout<<array[i]<<endl;
			}
		}
};



int main()
{
	Stack obj;
	int option, pos, val;
	
	do{
		cout<<"Select Any operation to do with Stack: "<<endl;
		cout<<"1 Push()"<<endl;
		cout<<"2 Pop()"<<endl;
		cout<<"3 isEmpty()"<<endl;
		cout<<"4 isFull()"<<endl;
		cout<<"5 Change()"<<endl;
		cout<<"6 Count()"<<endl;
		cout<<"7 Peak()"<<endl;
		cout<<"8 Display()"<<endl;
		cout<<"9 Clear screen"<<endl;
	
	cin >> option;
	switch(option)
	{
		case 1: 
			cout<<"Enter an item to push in stack: "<<endl;
			cin >> val;
			obj.Push(val);
			break;
		case 2:
			cout<<"Poped Values is : "<<obj.Pop()<<endl;
			break;
		case 3:
			if(obj.isEmpty())
				cout<<"Stack is Empty"<<endl;
			else
				cout<<"Stack is not Empty"<<endl;
			break;
		case 4:
			if(obj.isFull())
				cout<<"Stack is Full"<<endl;
			else
				cout<<"Stack is not Full"<<endl;
			break;
		case 5:
			cout<<"Enter Position of item you want to change: "<<endl;
			cin >> pos;
			cout<<"Enter Value you want to put: "<<endl;
			cin >> val;
			obj.Change(pos, val);
			break;
		case 6:
			cout<<"Numbers of itmes in stack are: "<<obj.Count()<<endl;
		case 7:
			cout<<"Enter Position you want to peak: "<<endl;
			cin >> pos;
			cout<<"Peak Function Called- "<<endl<< obj.Peak(pos) <<endl;
			break;
		case 8:
			obj.Display();
			break;
		case 9:
			system("cls");
			break;
		default:
			cout<<"Enter proper option number."<<endl;
		}
	}while(option!=0);
		return 0;
		}


