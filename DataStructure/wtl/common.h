#pragma once

template <typename T>
void wswap( T& lhs, T& rhs )
{
	T temp = lhs;
	lhs = rhs;
	rhs = temp;
}