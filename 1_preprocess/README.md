## 사용한 데이터셋

[Ai Hub](https://www.aihub.or.kr/)에서 한국어-영어 번역(병렬) 말뭉치 AI데이터를 다운 받았다.

다운받으려면 승인을 받아야 한다. 자신이 이 데이터를 받아야 하는 이유만 제대로 쓰면 하루 안에 승인을 받을 수 있다. (대충 쓰는 경우 반려될 수도 있다고...)

데이터 셋을 다운받으면 .xlsx 파일들로 되어있다. 이 파일들 모두를 텍스트 파일로 바꾸어 사용하기 편리하게 만들었다. 단순한 방식인 copy & paste와 sublime text를 사용해 txt 파일로 가공하였다.

## Bash shell을 사용하여 데이터셋 가공하기

본인은 window10을 사용한다. 그래서 이미 깔려있었던 git bash를 사용해서 bash shell을 사용하였다.

먼저 txt 파일을 txv 파일로 변경했다.

```
$ cat *.txt > corpus.tsv
```

corpus.tsv에서 행의 숫자를 세어보았다. (word count -line)

```
$ wc -l ./corpus.tsv
1602418 ./corpus.tsv
```

corpus.tsv의 5개 라인만 출력해보자.

```
$ head -n 5 ./corpus.tsv
'Bible Coloring'은 성경의 아름다운 이야기를 체험 할 수 있는 컬러링 앱입니다.    Bible Coloring' is a coloring application that allows you to experience beautiful stories in the Bible.
씨티은행에서 일하세요?  Do you work at a City bank?
푸리토의 베스트셀러는 해외에서 입소문만으로 4차 완판을 기록하였다.      PURITO's bestseller, which recorded 4th rough -cuts by words of mouth from abroad.
11장에서는 예수님이 이번엔 나사로를 무덤에서 불러내어 죽은 자 가운데서 살리셨습니다.    In Chapter 11 Jesus called Lazarus from the tomb and raised him from the dead.
6.5, 7, 8 사이즈가 몇 개나 더 재입고 될지 제게 알려주시면 감사하겠습니다.       I would feel grateful to know how many stocks will be secured of size 6.5, 7, and 8.
```

corpus.tsv 을 shuffling 했다.

```
$ shuf ./corpus.tsv > ./corpus.shuf.tsv
```

'corpus.'으로 시작하는 파일들에는 몇 개의 행이 있는지 확인해보자.

```
$ wc -l ./corpus.*
  1602418 ./corpus.shuf.tsv
  1602418 ./corpus.tsv
  3204836 total
```

corpus.shuf.tsv로 train dataset과 valid dataset을 만들었다.

```
$ head -n 1200000 ./corpus.shuf.tsv > corpus.shuf.train.tsv ; tail -n 402409 ./corpus.shuf.tsv | head -n 200000 > ./corpus.shuf.valid.tsv
```

그리고 test dataset을 만들었다.

```
$ tail -n 202409 ./corpus.shuf.tsv > ./corpus.shuf.test.tsv
```

'corpus.shuf.'으로 시작하는 파일들에는 몇 개의 행이 있는지 확인해보자.

```
$ wc -l ./corpus.shuf.*
   202409 ./corpus.shuf.test.tsv
  1200000 ./corpus.shuf.train.tsv
  1602418 ./corpus.shuf.tsv
   200000 ./corpus.shuf.valid.tsv
  3204827 total
```

지금까지의 파일들은 모두 `한국어 tab 영어`로 되어있다. 파일들을 `한국어`와 `영어`로 분리하자.

```
$ cut -f1 ./corpus.shuf.train.tsv > corpus.shuf.train.ko ; cut -f2 ./corpus.shuf.train.tsv > corpus.shuf.train.en
$ cut -f1 ./corpus.shuf.valid.tsv > ./corpus.shuf.valid.ko ; cut -f2 ./corpus.shuf.valid.tsv > ./corpus.shuf.valid.en
$ cut -f1 ./corpus.shuf.test.tsv > ./corpus.shuf.test.ko ; cut -f2 ./corpus.shuf.test.tsv > corpus.shuf.test.en
```

잘 분리되었는지 확인해보자.

```
$ head -n3 ./corpus.shuf.*.ko
==> ./corpus.shuf.test.ko <==
왜 이렇게 약속을 안 지켜요?
이곳은 1985년부터 여러 차례 발굴이 실시되었으며, 다양한 종류의 유적과 13,000여 점에 달하는 토기, 철기, 골각기 등의 유물이 출토되었다.
이어 “이런 구조는 미국 이익에 유리하게 설계됐는데 이런 체제가 무너진다면 장기적으로 가장 피해를 보는 것은 미국일 것”이라고 덧붙였다.

==> ./corpus.shuf.train.ko <==
아쉽네요, 그럼 검은색으로 변경할 수 있나요?
돈의문박물관마을 골목낙서 놀이마당 행사가 열린 26일 서울 종로구 돈의문박물관마을을 찾은 어린이들이 분필로 낙서를 하며 즐거운 시간을 보내고 있다.
이번 행사에는 다양한 4차산업 핵심 ICT 기술 산업군을 한눈에 볼 수 있도록 스마트시티 체험행사가 마련됐다.

==> ./corpus.shuf.valid.ko <==
그것은 가장 까다로운 사용자들의 요구사항조차 충족시키는 다양한 스포츠 및 이벤트를 제공합니다.
사건 직후 B씨는 112에 A씨를 신고했으며, 현장에 출동한 경찰에 의해 검거된 A씨는 사건 경위를 조사한 뒤 신병처리가 결정될 방침이다.
이날 간담회는 평택항 운영현황을 설명하고 이용률 제고 등 활성화에 대한 방안을 모색하고 상호 간의 협력 방안에 대한 토론이 진행됐다.

$ head -n3 ./corpus.shuf.*.en
==> ./corpus.shuf.test.en <==
Why do you not keep your word?
Since 1985, there have been several excavations that unearthed various archaeological remains and over 13,000 artifacts, such as earthenware, ironware, and bone tools.
He/she added "Such a structure was designed in favor of U.S. interests, and if such a system collapses, it would be the U.S. that would be the most damaging in the long run."

==> ./corpus.shuf.train.en <==
That's too bad, could I change it to black?
Children visiting Donimun Museum Village in Jongno-gu, Seoul, are doodling with chalks and have a good time on the 26th, when the event of alley graffiti recreation ground of Donimun Museum Village.
The smart city experience event was prepared so that various core ICT technology industries could be seen at a glance.

==> ./corpus.shuf.valid.en <==
It delivers a wide range of sports and events to cover the needs of even the most demanding users.
B reported A on 112 right after the incident, and A was arrested by the police on the scene. The police will decide how to handle A after the investigation.
The meeting explained the operation status of the Pyeongtaek Port, sought ways to revitalize it, including raising the utilization rate, and discussed ways to cooperate with each other.
```

이렇게 bash shell을 사용하면 편리하게 데이터셋을 가공할 수 있다.

가지고 있는 파일들

```
2021-01-19  오후 02:27        29,127,432 corpus.shuf.test.en
2021-01-19  오후 02:27        28,794,152 corpus.shuf.test.ko
2021-01-19  오후 02:21        57,921,584 corpus.shuf.test.tsv
2021-01-19  오후 02:25       172,538,977 corpus.shuf.train.en
2021-01-19  오후 02:25       170,648,937 corpus.shuf.train.ko
2021-01-19  오후 02:20       343,187,914 corpus.shuf.train.tsv
2021-01-19  오후 02:18       458,283,343 corpus.shuf.tsv
2021-01-19  오후 02:26        28,741,134 corpus.shuf.valid.en
2021-01-19  오후 02:26        28,429,977 corpus.shuf.valid.ko
2021-01-19  오후 02:20        57,171,111 corpus.shuf.valid.tsv
2021-01-19  오후 02:17       458,283,343 corpus.tsv
```

