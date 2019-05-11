#pragma once

///////////////////////////////////////////////////////////////////////////
// wcircular_queue
///////////////////////////////////////////////////////////////////////////
template <typename T, size_t N >
class wcircular_queue
{
public:
	wcircular_queue< T, N >();

	bool enqueue(T data);
	T dequeue();

	T front() const;
	bool empty() const;
	bool full() const;

	void print() const;

private:
	std::array< T, N > m_queue;
	size_t m_count = 0;
	size_t m_front = 0;
	size_t m_rear = 0;
};

template<typename T, size_t N>
inline wcircular_queue<T, N>::wcircular_queue()
{
	m_queue.fill(T());
}

template<typename T, size_t N>
inline bool wcircular_queue<T, N>::enqueue(T data)
{
	if ( full() )
	{
		std::cout << "queue is full" << std::endl;
		return false;
	}

	m_queue[ m_rear++ ] = data;
	m_rear = m_rear % N;

	++m_count;

	return true;
}

template<typename T, size_t N>
inline T wcircular_queue<T, N>::dequeue()
{
	if ( empty() )
	{
		std::cout << "queue is empty" << std::endl;
		return T();
	}
		

	T value = front();

	++m_front;
	m_front = m_front % N;

	--m_count;
	
	return value;
}

template<typename T, size_t N>
inline T wcircular_queue<T, N>::front() const
{
	return empty() ? T() : m_queue[ m_front ];
}

template<typename T, size_t N>
inline bool wcircular_queue<T, N>::empty() const
{
	return 0 == m_count;
}

template<typename T, size_t N>
inline bool wcircular_queue<T, N>::full() const
{
	return N == m_count;
}

template<typename T, size_t N>
inline void wcircular_queue<T, N>::print() const
{
	if ( empty() )
	{
		std::cout << "queue is empty" << std::endl;
		return;
	}

	size_t count = 0;
	for ( size_t i = m_front; i < m_front + N; ++i, ++count )
	{
		if ( m_count == count ) break;
		std::cout << m_queue[ i % N ] << "  ";
	}
		
	std::cout << std::endl;
}

///////////////////////////////////////////////////////////////////////////
// wlist_queue
///////////////////////////////////////////////////////////////////////////
template <typename T>
class wlist_queue
{
public:
	wlist_queue< T >();

	void enqueue(T data);
	T dequeue();

	T front() const;
	bool empty() const;

	void print() const;

private:
	std::list< T > m_queue;
};

template<typename T>
inline wlist_queue<T>::wlist_queue()
{
	m_queue.clear();
}

template<typename T>
inline void wlist_queue<T>::enqueue(T data)
{
	m_queue.push_back(data);
}

template<typename T>
inline T wlist_queue<T>::dequeue()
{
	T value = front();
	m_queue.pop_front();
	return value;
}

template<typename T>
inline T wlist_queue<T>::front() const
{
	return m_queue.front();
}

template<typename T>
inline bool wlist_queue<T>::empty() const
{
	return m_queue.empty();
}

template<typename T>
inline void wlist_queue<T>::print() const
{
	for ( auto iter = std::begin(m_queue); iter != std::end(m_queue); ++iter )
		std::cout << *iter << "  ";
	std::cout << std::endl;
}
