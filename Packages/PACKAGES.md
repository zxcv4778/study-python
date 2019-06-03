PACKAGES
=================

- 간단한 프로그램이 아니라면 패키지 구조로 파이썬 프로그램을 만드는 것이 공동 작업이나 유지 보수 면에서 유리하다.
- 패키지 구조로 모듈을 만들면 모듈과 이름이 겹치더라도 더 안전하다.

패키지 생성
------------

패키지 기본 구성 요소 준비

- Directory 구성

<pre>
Game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
</pre>

<pre><code>
# echo.py

def echo_test():
    print("echo")
    
---------------------

# render.py

def render_test():
    print("render")
</code></pre>

<pre><code>
from Game.graphic.render import render_test

print(render_test())

# 출력 결과
render
None
</code></pre>

\__init\__.py 의 용도
---------------------

- 해당 파일이 없으면 해당 디렉토리가 패키지로 인식되지 않는다.
