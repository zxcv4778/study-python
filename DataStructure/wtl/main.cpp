#include "pch.h"

int main( int argc, char* argv[] )
{
	wbinary_heap< int > heap( 11 );
	heap.insert( 3 );
	heap.insert( 2 );
	heap.insert( 1 );
	heap.insert( 15 );
	heap.insert( 5 );
	heap.insert( 4 );
	heap.insert( 45 );

	while( heap.size() )
		std::cout << heap.extract() << std::endl;
	
	
	return 0;
}