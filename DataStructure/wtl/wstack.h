#pragma once

///////////////////////////////////////////////////////////////////////////
// wfixed_stack
///////////////////////////////////////////////////////////////////////////
#pragma region WFIXED_STACK
template <typename T, size_t N>
class wfixed_stack
{
public:
	wfixed_stack< T, N >();
	
	bool push( T data );
	bool pop();

	bool empty() const;
	bool full() const;

	T peek() const;
	void print() const;

private:
	T m_data[ N ];
	size_t m_top;
};

template<typename T, size_t N>
inline wfixed_stack<T, N>::wfixed_stack()
{
	memset( m_data, 0, sizeof( T ) * N );
	m_top = 0;
}

template<typename T, size_t N>
inline bool wfixed_stack<T, N>::push( T data )
{
	if( full() )
		return false;

	m_data[ m_top++ ] = data;

	return true;
}

template<typename T, size_t N>
inline bool wfixed_stack<T, N>::pop()
{
	if( empty() )
		return false;

	--m_top;

	return true;
}

template<typename T, size_t N>
inline bool wfixed_stack<T, N>::empty() const
{
	return 0 == m_top;
}

template<typename T, size_t N>
inline bool wfixed_stack<T, N>::full() const
{
	return m_top >= N;
}

template<typename T, size_t N>
inline T wfixed_stack<T, N>::peek() const
{
	assert( !empty() );
	return m_data[ m_top - 1 ];
}

template<typename T, size_t N>
inline void wfixed_stack<T, N>::print() const
{
	for( size_t i = 0; i < m_top; ++i )
		std::cout << m_data[ i ] << "  ";
	std::cout << std::endl;
}

#pragma endregion

///////////////////////////////////////////////////////////////////////////
// wdynamic_stack
///////////////////////////////////////////////////////////////////////////
#pragma region WDYNAMIC_STACK
template <typename T>
class wdynamic_stack
{
public:
	wdynamic_stack<T>();

	void push( T data );
	void pop();

	bool empty() const;

	T peek() const;
	void print() const;

private:
	std::vector< T > m_data;
};

template<typename T>
inline wdynamic_stack<T>::wdynamic_stack()
{
	m_data.clear();
}

template<typename T>
inline void wdynamic_stack<T>::push( T data )
{
	m_data.push_back( data );
}

template<typename T>
inline void wdynamic_stack<T>::pop()
{
	if( empty() )
		return;

	m_data.pop_back();
}

template<typename T>
inline bool wdynamic_stack<T>::empty() const
{
	return 0 == m_data.size();
}

template<typename T>
inline T wdynamic_stack<T>::peek() const
{
	assert( m_data.size() > 0 );
	return m_data[ m_data.size() - 1 ];
}

template<typename T>
inline void wdynamic_stack<T>::print() const
{
	for( size_t i = 0; i < m_data.size(); ++i )
		std::cout << m_data[ i ] << "  ";
	std::cout << std::endl;
}
#pragma endregion


///////////////////////////////////////////////////////////////////////////
// wlist_stack
///////////////////////////////////////////////////////////////////////////
#pragma region WDYNAMIC_STACK
template <typename T>
class wlist_stack
{
public:
	wlist_stack<T>();

	void push( T data );
	void pop();

	bool empty() const;

	T peek() const;
	void print() const;

private:
	std::list< T > m_data;
};

template<typename T>
inline wlist_stack<T>::wlist_stack()
{
	m_data.clear();
}

template<typename T>
inline void wlist_stack<T>::push( T data )
{
	m_data.push_back( data );
}

template<typename T>
inline void wlist_stack<T>::pop()
{
	if( empty() )
		return;

	m_data.pop_back();
}

template<typename T>
inline bool wlist_stack<T>::empty() const
{
	return 0 == m_data.size();
}

template<typename T>
inline T wlist_stack<T>::peek() const
{
	assert( m_data.size() > 0 );

	return m_data.back();
}

template<typename T>
inline void wlist_stack<T>::print() const
{
	for( auto& data : m_data )
		std::cout << data << "  ";
	std::cout << std::endl;
}

#pragma endregion
