#pragma once

#pragma region TREE_NODE
using CHILD_TYPE = char;
enum
{
	NONE = 0x00,
	LEFT = 0x01,
	RIGHT = 0x10,
	BOTH = 0x11,
};
template <typename T>
struct wtreenode
{
	wtreenode<T>* _left = nullptr;
	wtreenode<T>* _right = nullptr;
	CHILD_TYPE _type = NONE;
	T _data;

	wtreenode<T>();
	wtreenode<T>( T data );

	void deleteLeft();
	void deleteRight();

	bool nochild() const;
	CHILD_TYPE type() const;
};

template<typename T>
inline wtreenode<T>::wtreenode()
	: _data()
{
}

template<typename T>
inline wtreenode<T>::wtreenode( T data )
	: _data( data )
{
}

template<typename T>
inline void wtreenode<T>::deleteLeft()
{
	if( _left )
	{
		delete _left;
		_left = nullptr;
	}
}

template<typename T>
inline void wtreenode<T>::deleteRight()
{
	if( _right )
	{
		delete _right;
		_right = nullptr;
	}
}

template<typename T>
inline bool wtreenode<T>::nochild() const
{
	return ( nullptr == _left ) && ( nullptr == _right );
}

template<typename T>
inline CHILD_TYPE wtreenode<T>::type() const
{
	return _type;
}

#pragma endregion


#pragma region BINARY_TREE
enum class PRINT_ORDER_TYPE
{
	PRE,
	IN,
	POST
};
template <typename T>
class wbinary_tree
{
public:
	wbinary_tree<T>();
	~wbinary_tree<T>();

	void clear();
	void insert( T data );
	bool erase( T data );

	void print( PRINT_ORDER_TYPE type = PRINT_ORDER_TYPE::IN ) const;

	bool empty() const;
	size_t size() const;

private:
	void clearAll();
	void clearPostOrder( wtreenode<T>* node );

	void printPreOrder( wtreenode<T>* node ) const;
	void printInOrder( wtreenode<T>* node ) const;
	void printPostOrder( wtreenode<T>* node ) const;

	void erase( wtreenode<T>*& parent, wtreenode<T>*& child );

private:
	wtreenode<T>* m_root = nullptr;
	size_t m_count = 0;
};

template<typename T>
inline wbinary_tree<T>::wbinary_tree()
{
}

template<typename T>
inline wbinary_tree<T>::~wbinary_tree()
{
	clearAll();
}

template<typename T>
inline void wbinary_tree<T>::clear()
{
	clearAll();
	m_root = nullptr;
	m_count = 0;
}

template<typename T>
inline void wbinary_tree<T>::insert( T data )
{
	if( empty() )
	{
		wtreenode<T>* node = new wtreenode<T>( data );
		m_root = node;
		++m_count;
		return;
	}

	wtreenode<T>* traversal = m_root;
	while( true )
	{
		if( nullptr == traversal || traversal->_data == data )
		{
			break;
		}
		else if( traversal->_data > data && traversal->_left )
		{
			traversal = traversal->_left;
		}
		else if( traversal->_data > data )
		{
			wtreenode<T>* node = new wtreenode<T>( data );
			traversal->_left = node;
			traversal->_type |= LEFT;
			++m_count;
			break;
		}
		else if( traversal->_data < data && traversal->_right )
		{
			traversal = traversal->_right;
		}
		else if( traversal->_data < data )
		{
			wtreenode<T>* node = new wtreenode<T>( data );
			traversal->_right = node;
			traversal->_type |= RIGHT;
			++m_count;
			break;
		}
	}
}

template<typename T>
inline bool wbinary_tree<T>::erase( T data )
{
	if( empty() )
		return false;

	if( 1 == size() )
	{
		delete m_root;
		m_root = nullptr;
		m_count = 0;
		return true;
	}

	if( m_root->_data == data )
	{
		switch( m_root->type() )
		{
			case LEFT:
				m_root = m_root->_left;
				break;
			
			case RIGHT:
				m_root = m_root->_right;
				break;

			case BOTH:
			{
				wtreenode<T>* root_right_min = m_root->_right;
				wtreenode<T>* root_right_min_parent = nullptr;

				while( root_right_min->_left )
				{
					root_right_min_parent = root_right_min;
					root_right_min = root_right_min->_left;
				}

				root_right_min_parent->_left = root_right_min->_right;
				m_root->_data = root_right_min->_data;

				delete root_right_min;
				--m_count;
			}
				break;
		}
		return true;
	}

	wtreenode<T>* parent = nullptr;
	wtreenode<T>* traversal = m_root;
	bool is_delete = false;
	bool is_left = false;
	while( traversal )
	{
		if( traversal->_data > data )
		{
			parent = traversal;
			traversal = traversal->_left;
			is_left = true;
		}
		else if( traversal->_data < data )
		{
			parent = traversal;
			traversal = traversal->_right;
			is_left = false;
		}
		else
		{
			erase( parent, traversal );
			--m_count;
			break;
		}
	}

	return is_delete;
}

template<typename T>
inline void wbinary_tree<T>::print( PRINT_ORDER_TYPE type ) const
{
	switch( type )
	{
		case PRINT_ORDER_TYPE::PRE:		printPreOrder( m_root );	break;
		case PRINT_ORDER_TYPE::IN:		printInOrder( m_root );		break;
		case PRINT_ORDER_TYPE::POST:	printPostOrder( m_root );	break;
	}
	std::cout << std::endl;
}

template<typename T>
inline bool wbinary_tree<T>::empty() const
{
	return 0 == m_count;
}

template<typename T>
inline size_t wbinary_tree<T>::size() const
{
	return m_count;
}

template<typename T>
inline void wbinary_tree<T>::clearAll()
{
	clearPostOrder( m_root );
}

template<typename T>
inline void wbinary_tree<T>::clearPostOrder( wtreenode<T>* node )
{
	if( nullptr == node ) return;

	clearPostOrder( node->_left );
	clearPostOrder( node->_right );
	delete node;
}

template<typename T>
inline void wbinary_tree<T>::printPreOrder( wtreenode<T>* node ) const
{
	if( nullptr == node ) return;
	std::cout << node->_data << "  ";
	printPreOrder( node->_left );
	printPreOrder( node->_right );
}

template<typename T>
inline void wbinary_tree<T>::printInOrder( wtreenode<T>* node ) const
{
	if( nullptr == node ) return;
	printInOrder( node->_left );
	std::cout << node->_data << "  ";
	printInOrder( node->_right );
}

template<typename T>
inline void wbinary_tree<T>::printPostOrder( wtreenode<T>* node ) const
{
	if( nullptr == node ) return;
	printPostOrder( node->_left );
	printPostOrder( node->_right );
	std::cout << node->_data << "  ";
}

template<typename T>
inline void wbinary_tree<T>::erase( wtreenode<T>*& parent, wtreenode<T>*& child )
{
	bool is_left = parent->_left == child;

	switch( child->type() )
	{
		case NONE:
			if( is_left )
				parent->deleteLeft();
			else
				parent->deleteRight();
			break;

		case LEFT:
			if( is_left )
				parent->_left = child->_left;
			else
				parent->_right = child->_left;
			
			delete child;
			child = nullptr;
			break;

		case RIGHT:
			if( is_left )
				parent->_left = child->_right;
			else
				parent->_right = child->_right;

			delete child;
			child = nullptr;
			break;

		case BOTH:
			wtreenode<T>* child_right_min = child->_right;
			wtreenode<T>* child_right_min_parent = child;

			while( child_right_min->_left )
			{
				child_right_min_parent = child_right_min;
				child_right_min = child_right_min->_left;
			}

			child->_data = child_right_min->_data;

			bool is_same = child == child_right_min_parent;
			switch( child_right_min->type() )
			{
				case NONE:
					if( is_same )
						child_right_min_parent->deleteRight();
					else
						child_right_min_parent->deleteLeft();
					break;

				case RIGHT:
					if( is_same )
						child_right_min_parent->_right = child_right_min->_right;
					else
						child_right_min_parent->_left = child_right_min->_right;
					break;
			}

			delete child_right_min;
			--m_count;
			break;
	}
}

#pragma endregion
