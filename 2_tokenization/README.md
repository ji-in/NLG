## 한국어 파일 tokenization 하기

mecab을 corpus.shuf.train.ko, corpus.shuf.valid.ko, corpus.shuf.test.ko에 적용하면, corpus.shuf.train.tok.ko, corpus.shuf.valid.tok.ko, corpus.shuf.test.tok.ko 파일들을 얻는다.     

mecab을 적용한 후, post_tokenize 파일을 실행해서 corpus.shuf.train.tok.post.ko, corpus.shuf.valid.tok.post.ko, corpus.shuf.test.tok.post.ko 파일들을 얻는다.

```
>python post_tokenize.py corpus.shuf.valid.tok.ko < corpus.shuf.valid.tok.ko > corpus.shuf.valid.tok.post.ko
```

```
>python post_tokenize.py corpus.shuf.train.tok.ko < corpus.shuf.train.tok.ko > corpus.shuf.train.tok.post.ko
```

```
>python post_tokenize.py corpus.shuf.test.tok.ko < corpus.shuf.test.tok.ko > corpus.shuf.test.tok.post.ko
```

post_tokenize.py 파일은 후에 detokenize를 편하게 하기 위함이다.

------

## 영문 파일 tokenization 하기

한국어를 mecab으로 형태소 분석을 했다면, 영문은 MosesTokenizer로 형태소 분석을 한다. 

MosesTokenizer를 corpus.shuf.train.en, corpus.shuf.valid.en, corpus.shuf.test.en에 적용해서 corpus.shuf.train.tok.en, corpus.shuf.valid.tok.en, corpus.shuf.test.tok.en 파일들을 얻는다.

MosesTokenizer를 적용한 후, post_tokenize 파일을 실행해서 corpus.shuf.train.tok.post.en, corpus.shuf.valid.tok.post.en, corpus.shuf.test.tok.post.en 파일들을 얻는다.

```
>python post_tokenize.py corpus.shuf.valid.tok.en < corpus.shuf.valid.tok.en > corpus.shuf.valid.tok.post.en
```

```
>python post_tokenize.py corpus.shuf.test.tok.en < corpus.shuf.test.tok.en > corpus.shuf.test.tok.post.en
```

```
>python post_tokenize.py corpus.shuf.train.tok.en < corpus.shuf.train.tok.en > corpus.shuf.train.tok.post.en
```

------

## 참고 - 윈도우에 MeCab 설치하기

Mecab을 윈도우에 설치하는데 많은 어려움을 겪었다. 결국 한가지 방법을 알아냈고, mecab을 설치하는데 성공하였다.

여러번의 구글링 끝에 mecab 설치를 위한 오픈소스인 `은전한닢 프로젝트`에 대해서 알게 되었고 [여기](https://somjang.tistory.com/entry/Windows-%EC%97%90%EC%84%9C-Mecab-mecab-%EA%B8%B0%EB%B0%98-%ED%95%9C%EA%B5%AD%EC%96%B4-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EA%B8%B0-%EC%84%A4%EC%B9%98%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)를 참고하여 윈도우에 mecab을 설치했다.

사실 `은전한닢`을 윈도우에 그냥 깔았을 때, 에러만 뜨고 설치가 잘 안됐었다. 계속 삽질을 하던 중, **파이썬 버전**이 문제인가 싶었다. 그래서 아나콘다로 파이썬 버전이 3.6x인 가상환경을 만들었다. (원래 쓰던 버전은 3.8x) 아니나 다를까, mecab이 잘 깔렸고 성공적으로 토큰화를 할 수 있었다. 

jupyter notebook 환경에서 mecab을 사용하려면, jupyter notebook의 kernel에 내가 만든 가상환경을 추가해야한다. 그것은 내가 따로 [여기](https://github.com/ji-in/note/tree/main/jupyter-notebook)에 정리했다.

mecab을 사용한 코드들은 tok_with_mecab.ipynb 파일에 고이 적어놨다.

------

## 참고 - MosesTokenizer 사용하기

영어로 된 문장의 형태소를 분석하기 위해서는 MosesTokenizer를 사용해야 한다.

강사님이 만든 tokenize를 위한 파이썬 파일은 다음과 같이 생겼었다.

```python
import sys, fileinput
from mosestokenizer import *

if __name__ == "__main__":
    with MosesTokenizer('en') as tokenize:
        for line in fileinput.input():
            if line.strip() != "":
                tokens = tokenize(line.strip())

                sys.stdout.write(" ".join(tokens) + "\n")
            else:
                sys.stdout.write('\n')
```

이 파일을 실행시키자, 에러가 뜨는 것이었다. 윈도우에서 실행시켜서 안되는 줄 알고 리눅스에서 다시 동일한 파일을 실행시켰다. 그래도 에러가 뜨는 것이었다. 

그래서 구글링을 통해서 [이 페이지](https://github.com/alvations/sacremoses)를 알아냈고, sacremoses를 설치해서 mosestokenizer를 사용했다. 

mosestokenizer를 사용한 코드들은 tok_with_MosesTokenizer.ipynb 파일에 고이 적어놨다.