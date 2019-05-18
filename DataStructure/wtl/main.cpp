#include "pch.h"

int main( int argc, char* argv[] )
{
	wbinary_tree<int> tree;

	//// GeeksOfGeeks
	//tree.insert( 50 );
	//tree.insert( 40 );
	//tree.insert( 70 );
	//tree.insert( 60 );
	//tree.insert( 80 );

	tree.insert( 12 );
	tree.insert( 5 );
	tree.insert( 15 );
	tree.insert( 3 );
	tree.insert( 1 );
	tree.insert( 13 );
	tree.insert( 14 );
	tree.insert( 17 );
	tree.insert( 19 );
	tree.insert( 18 );

	// tree.print( PRINT_ORDER_TYPE::PRE );
	tree.print( PRINT_ORDER_TYPE::IN );
	// tree.print( PRINT_ORDER_TYPE::POST );

	tree.erase( 15 );
	tree.print( PRINT_ORDER_TYPE::IN );
	
	return 0;
}