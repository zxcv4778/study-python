TUPLE
====================

- 리스트와 튜플은 다른게 '별로' 없다.
- 가장 큰 차이라고 볼 수 있는 건 tuple은 값을 변경할 수 없다.

생성
----------

<pre><code>
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
</code></pre>

튜플을 변경하려고 할 때
--------------------

> 튜플 요소 삭제

<pre><code>
del t3[2]

# 출력 결과
TypeError: 'tuple' object doesn't support item deletion
</code></pre>

> 튜플 요소 변경

<pre><code>
t3[-1] = 9

# 출력 결과
TypeError: 'tuple' object does not support item assignment
</code></pre>

