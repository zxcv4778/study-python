#pragma once


template <typename T>
class wbinary_heap
{
public:
	wbinary_heap<T>( size_t capacity = 32 );
	~wbinary_heap<T>();

	void insert( T value );
	void erase( int index );

	T extract();
	T min() const;
	size_t size() const;

private:
	void minHeapify( int index );
	void decrease( int index, T value );

	size_t parent( int index ) const;
	size_t left( int index ) const;
	size_t right( int index ) const;

private:
	T* m_data = nullptr;
	size_t m_capacity = 0;
	size_t m_count = 0;
};

template<typename T>
inline wbinary_heap<T>::wbinary_heap( size_t capacity )
	: m_capacity( capacity )
{
	m_data = new T[ m_capacity ];
}

template<typename T>
inline wbinary_heap<T>::~wbinary_heap()
{
	delete[] m_data;
}

template<typename T>
inline void wbinary_heap<T>::insert( T value )
{
	if( m_capacity == m_count )
	{
		// overflow or resize
		return;
	}

	++m_count;
	int index = m_count - 1;
	m_data[ index ] = value;

	while( 0 != index && m_data[ parent( index ) ] > m_data[ index ] )
	{
		wswap( m_data[ index ], m_data[ parent( index ) ] );
		index = parent( index );
	}
}

template<typename T>
inline void wbinary_heap<T>::erase( int index )
{
	decrease( index, )
}

template<typename T>
inline void wbinary_heap<T>::decrease( int index, T value )
{
	m_data[ index ] = value;

	while( 0 != index && m_data[ parent( index ) ] > m_data[ index ] )
	{
		wswap( m_data[ index ], m_data[ parent( index ) ] );
		index = parent( index );
	}
}

template<typename T>
inline void wbinary_heap<T>::minHeapify( int index )
{
	size_t l_value = left( index );
	size_t r_value = right( index );

	size_t smallest = index;

	if( l_value < m_count && m_data[ l_value ] < m_data[ index ] )
		smallest = l_value;

	if( r_value < m_count && m_data[ r_value ] < m_data[ smallest ] )
		smallest = r_value;

	if( smallest != index )
	{
		wswap( m_data[ index ], m_data[ smallest ] );
		minHeapify( smallest );
	}
}

template<typename T>
inline T wbinary_heap<T>::extract()
{
	// exception case
	if( m_count <= 0 )
		return T();

	if( 1 == m_count )
	{
		--m_count;
		return m_data[ 0 ];
	}

	int min_value = m_data[ 0 ];

	m_data[ 0 ] = m_data[ m_count - 1 ];
	--m_count;
	minHeapify( 0 );

	return min_value;
}

template<typename T>
inline T wbinary_heap<T>::min() const
{
	return m_data[ 0 ];
}

template<typename T>
inline size_t wbinary_heap<T>::size() const
{
	return m_count;
}

template<typename T>
inline size_t wbinary_heap<T>::parent( int index ) const
{
	return ( index - 1 ) / 2;
}

template<typename T>
inline size_t wbinary_heap<T>::left( int index ) const
{
	return ( 2 * index + 1 );
}

template<typename T>
inline size_t wbinary_heap<T>::right( int index ) const
{
	return ( 2 * index + 2 );
}
