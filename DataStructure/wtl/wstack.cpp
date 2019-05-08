#include "pch.h"
#include "wstack.h"

// 테스트 코드

/*
	{
	wfixed_stack< int, 5 > s;

	for( int i = 0; i < 6; ++i )
	{
		if( s.push( i ) )
			s.print();
		else
			std::cout << "stack is full" << std::endl;
	}
	std::cout << "peek() = " << s.peek() << std::endl;

	for( int i = 0; i < 6; ++i )
	{
		if( s.pop() )
			s.print();
		else
			std::cout << "stack is empty" << std::endl;
	}
		}

	{
		wdynamic_stack< int > s;

		for( int i = 0; i < 5; ++i )
		{
			s.push( i );
			s.print();
		}

		std::cout << "peek() = " << s.peek() << std::endl;

		for( int i = 0; i < 5; ++i )
		{
			s.pop();

			if( s.empty() )
				std::cout << "stack is empty" << std::endl;
			else
				s.print();
		}
	}

	{
		wlist_stack< int > s;
		for( int i = 0; i < 5; ++i )
		{
			s.push( i );
			s.print();
		}

		std::cout << "peek() = " << s.peek() << std::endl;

		for( int i = 0; i < 5; ++i )
		{
			s.pop();

			if( s.empty() )
				std::cout << "stack is empty" << std::endl;
			else
				s.print();
		}
	}
*/