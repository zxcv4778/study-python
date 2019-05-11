#include "pch.h"

int main( int argc, char* argv[] )
{
	{
		wcircular_queue< int, 5 > q;
		for ( int i = 1; i < 6; ++i )
		{
			q.enqueue(i);
			q.print();
		}

		for ( int i = 0; i < 3; ++i )
		{
			q.dequeue();
			q.print();
		}

		for ( int i = 1; i < 4; ++i )
		{
			q.enqueue( i * 10);
			q.print();
		}
	}
	
	{
		std::cout << "wlist_queue" << std::endl;
		wlist_queue< int > q;
		for ( int i = 1; i < 6; ++i )
		{
			q.enqueue(i);
			q.print();
		}

		for ( int i = 0; i < 3; ++i )
		{
			q.dequeue();
			q.print();
		}

		for ( int i = 1; i < 4; ++i )
		{
			q.enqueue(i * 10);
			q.print();
		}
	}

	return 0;
}