#include <iostream>

using namespace std;

class Rabotnik
{

	private string name;
	private string sec_name;
	private int age;
	private int salary;

	Rabotnik(string name, string sec_name, int age, int salary){

		this.name = name;
		this.sec_name = sec_name;
		this.age = age;
		this.salary = salary;
	};
	~Rabotnik();

	void sayHi(){
		cout<<"Hello i`m a "<<name<<endl;
	}

	string getName(){
		return name;
	}

	string setName(string name){
		this.name = name;
	}

	public static int sum(int x, int y){
		return x+y;
	}

	public abstract int abstract();

};




int main(int argc, char const *argv[])
{
	int res;

	calc(res->{
		return 10/2;
	});

	return 0;
}