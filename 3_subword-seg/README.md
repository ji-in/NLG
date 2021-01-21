------

For subword segmentation, you can clone the following repository:
https://github.com/kh-kim/subword-nmt

If you are using Microsoft Windows, you can download Cygwin to mimic linux command-line environment.

URL: https://www.cygwin.com/

Also, in order to use 'tokenizer.py', you need to install mosestokenizer using following command:
$ pip install mosestokenizer

After installation, you need to download package inside nltk.

------

한국어의 경우 띄어쓰기가 제각각이다. 지금 사용하는(ai hub에서 다운 받은) corpus는 정제가 잘 되어 있어서 바로 subword seg를 해도 굉장히 잘 될 것이다. 그러나 일반적으로 크롤링한 데이터의 경우 띄어쓰기가 잘 안되어 있을 것이다. 그 경우 바로 subword seg를 뜻하지 않은 대로 결과가 나올 것이다. 

강사님의 경우 tokenization을 한 후에 subword seg를 하는 것을 좋아하신다고 한다. 

영어 같은 경우 쉼표와 마침표만 띄어준다. 영어는 띄어쓰기와 함께 발전해온 언어기 때문에 띄어쓰기가 매우 잘되어 있다.

------

- `learn_bpe.py` 실행하기

```
>python ./subword-nmt/learn_bpe.py --input ./data/corpus.shuf.train.tok.post.en --output bpe.en.model --symbols 50000 --verbose
```

```
>python ./subword-nmt/learn_bpe.py --input ./data/corpus.shuf.train.tok.post.ko --output bpe.ko.model --symbols 30000 --verbose
```

- `apply_bpe.py` 실행하기

```
>python ./subword-nmt/apply_bpe.py -c ./data/bpe.en.model < ./data/corpus.shuf.train.tok.post.en > ./data/corpus.shuf.train.tok.post.bpe.en
```

```
>python ./subword-nmt/apply_bpe.py -c ./data/bpe.en.model < ./data/corpus.shuf.valid.tok.post.en > ./data/corpus.shuf.valid.tok.post.bpe.en
```

```
>python ./subword-nmt/apply_bpe.py -c ./data/bpe.en.model < ./data/corpus.shuf.test.tok.post.en > ./data/corpus.shuf.test.tok.post.bpe.en
```

- `corpus.shuf.*.tok.post.bpe.ko` 형태의 파일 앞에서부터 3줄만 확인하기

```
$ head -n 3 corpus.shuf.*.tok.post.bpe.ko
==> corpus.shuf.test.tok.post.bpe.ko <==
▁▁왜 ▁▁이 렇게 ▁▁약 속 ▁▁을 ▁▁안 ▁▁지 켜 ▁▁요 ▁▁?
▁▁이 곳 ▁▁은 ▁▁1 9 85 ▁▁년 ▁▁부터 ▁▁여 러 ▁▁차례 ▁▁발 굴 ▁▁이 ▁▁실 시 ▁▁되 ▁▁었 ▁▁으며 ▁▁, ▁▁다 양 ▁▁한 ▁▁종 류 ▁▁의 ▁▁유 적 ▁▁과 ▁▁13 ▁▁, ▁▁000 ▁▁여 ▁▁점 ▁▁에 ▁▁달 하 ▁▁는 ▁▁토 기 ▁▁, ▁▁철 기 ▁▁, ▁▁골 각 기 ▁▁등 ▁▁의 ▁▁유물 ▁▁이 ▁▁출 토 ▁▁되 ▁▁었 ▁▁다 ▁▁.
▁▁이어 ▁▁“ ▁▁이 런 ▁▁구조 ▁▁는 ▁▁미 국 ▁▁이익 ▁▁에 ▁▁유리 ▁▁하 ▁▁게 ▁▁설 계 ▁▁됐 ▁▁는데 ▁▁이 런 ▁▁체 제 ▁▁가 ▁▁무 너 ▁▁진다면 ▁▁장 기 ▁▁적 ▁▁으로 ▁▁가 장 ▁▁피 해 ▁▁를 ▁▁보 ▁▁는 ▁▁것 ▁▁은 ▁▁미 국 ▁▁일 ▁▁것 ▁▁” ▁▁이 ▁▁라고 ▁▁덧 붙 였 ▁▁다 ▁▁.

==> corpus.shuf.train.tok.post.bpe.ko <==
▁▁아 쉽 ▁▁네 요 ▁▁, ▁▁그 럼 ▁▁검 은색 ▁▁으로 ▁▁변 경 ▁▁할 ▁▁수 ▁▁있 ▁▁나 요 ▁▁?
▁▁돈 의 문 ▁▁박물관 ▁▁마을 ▁▁골목 ▁▁낙 서 ▁▁놀이 ▁▁마당 ▁▁행사 ▁▁가 ▁▁열 린 ▁▁26 ▁▁일 ▁▁서 울 ▁▁종 로구 ▁▁돈 의 문 ▁▁박물관 ▁▁마을 ▁▁을 ▁▁찾 ▁▁은 ▁▁어 린 이 ▁▁들 ▁▁이 ▁▁분 필 ▁▁로 ▁▁낙 서 ▁▁를 ▁▁하 ▁▁며 ▁▁즐 거운 ▁▁시간 ▁▁을 ▁▁보 내 ▁▁고 ▁▁있 ▁▁다 ▁▁.
▁▁이 번 ▁▁행사 ▁▁에 ▁▁는 ▁▁다 양 ▁▁한 ▁▁4 ▁▁차 ▁▁산업 ▁▁핵 심 ▁▁I CT ▁▁기 술 ▁▁산업 ▁▁군 ▁▁을 ▁▁한 눈 ▁▁에 ▁▁볼 ▁▁수 ▁▁있 ▁▁도록 ▁▁스 마트 ▁▁시티 ▁▁체 험 ▁▁행사 ▁▁가 ▁▁마 련 ▁▁됐 ▁▁다 ▁▁.

==> corpus.shuf.valid.tok.post.bpe.ko <==
▁▁그 것 ▁▁은 ▁▁가 장 ▁▁까 다 로운 ▁▁사 용 ▁▁자 ▁▁들 ▁▁의 ▁▁요 구 ▁▁사항 ▁▁조 차 ▁▁충 족 ▁▁시 키 ▁▁는 ▁▁다 양 ▁▁한 ▁▁스포츠 ▁▁및 ▁▁이 벤트 ▁▁를 ▁▁제 공 ▁▁합니다 ▁▁.
▁▁사 건 ▁▁직 후 ▁▁B ▁▁씨 ▁▁는 ▁▁1 12 ▁▁에 ▁▁A ▁▁씨 ▁▁를 ▁▁신고 ▁▁했으며 ▁▁, ▁▁현 장 ▁▁에 ▁▁출동 ▁▁한 ▁▁경찰 ▁▁에 ▁▁의 해 ▁▁검 거 ▁▁된 ▁▁A ▁▁씨 ▁▁는 ▁▁사 건 ▁▁경 위 ▁▁를 ▁▁조사 ▁▁한 ▁▁뒤 ▁▁신 병 ▁▁처리 ▁▁가 ▁▁결 정 ▁▁될 ▁▁방 침 ▁▁이 ▁▁다 ▁▁.
▁▁이날 ▁▁간 담회 ▁▁는 ▁▁평 택 항 ▁▁운 영 ▁▁현 황 ▁▁을 ▁▁설 명 ▁▁하 ▁▁고 ▁▁이 용 ▁▁률 ▁▁제 고 ▁▁등 ▁▁활 성 ▁▁화 ▁▁에 ▁▁대 한 ▁▁방 안 ▁▁을 ▁▁모 색 ▁▁하 ▁▁고 ▁▁상호 ▁▁간 ▁▁의 ▁▁협 력 ▁▁방 안 ▁▁에 ▁▁대 한 ▁▁토 론 ▁▁이 ▁▁진 행 ▁▁됐 ▁▁다 ▁▁.
```

- `corpus.shuf.*.tok.post.bpe.en` 형태의 파일 앞에서부터 3줄만 확인하기

```
$ head -n 3 corpus.shuf.*.tok.post.bpe.en
==> corpus.shuf.test.tok.post.bpe.en <==
▁▁W hy ▁▁do ▁▁you ▁▁n ot ▁▁k eep ▁▁y our ▁▁word ▁▁?
▁▁S ince ▁▁19 85 ▁▁, ▁▁th ere ▁▁h ave ▁▁b een ▁▁se ver al ▁▁ex c av ations ▁▁th at ▁▁un ear thed ▁▁v arious ▁▁arch ae ological ▁▁r em ains ▁▁and ▁▁over ▁▁1 3,000 ▁▁ar tif acts ▁▁, ▁▁s uch ▁▁as ▁▁ear th enware ▁▁, ▁▁ir on ware ▁▁, ▁▁and ▁▁bone ▁▁t ools ▁▁.
▁▁H e ▁▁/ ▁▁sh e ▁▁added ▁▁& quot ; ▁▁S uch ▁▁a ▁▁s truc ture ▁▁w as ▁▁d es igned ▁▁in ▁▁f avor ▁▁of ▁▁U .S. ▁▁inter ests ▁▁, ▁▁and ▁▁if ▁▁s uch ▁▁a ▁▁s ystem ▁▁c oll ap ses ▁▁, ▁▁it ▁▁w ould ▁▁be ▁▁the ▁▁U .S. ▁▁th at ▁▁w ould ▁▁be ▁▁the ▁▁most ▁▁dam aging ▁▁in ▁▁the ▁▁long ▁▁r un ▁▁. ▁▁& quot ;

==> corpus.shuf.train.tok.post.bpe.en <==
▁▁T hat ▁▁&apos ; s ▁▁t oo ▁▁b ad ▁▁, ▁▁c ould ▁▁I ▁▁change ▁▁it ▁▁to ▁▁bl ack ▁▁?
▁▁Ch ildren ▁▁vis iting ▁▁D on imun ▁▁M us eum ▁▁V illage ▁▁in ▁▁J ong n o-gu ▁▁, ▁▁S e oul ▁▁, ▁▁are ▁▁d ood ling ▁▁w ith ▁▁ch alks ▁▁and ▁▁h ave ▁▁a ▁▁g ood ▁▁time ▁▁on ▁▁the ▁▁2 6th ▁▁, ▁▁wh en ▁▁the ▁▁ev ent ▁▁of ▁▁alley ▁▁gr affiti ▁▁rec reation ▁▁ground ▁▁of ▁▁D on imun ▁▁M us eum ▁▁V illage ▁▁.
▁▁The ▁▁s mart ▁▁city ▁▁ex perience ▁▁ev ent ▁▁w as ▁▁pr epared ▁▁so ▁▁th at ▁▁v arious ▁▁c ore ▁▁IC T ▁▁t echnology ▁▁ind us tries ▁▁c ould ▁▁be ▁▁s een ▁▁at ▁▁a ▁▁gl ance ▁▁.

==> corpus.shuf.valid.tok.post.bpe.en <==
▁▁I t ▁▁d el ivers ▁▁a ▁▁wide ▁▁r ange ▁▁of ▁▁s ports ▁▁and ▁▁ev ents ▁▁to ▁▁c over ▁▁the ▁▁n eeds ▁▁of ▁▁even ▁▁the ▁▁most ▁▁d em anding ▁▁users ▁▁.
▁▁B ▁▁rep orted ▁▁A ▁▁on ▁▁1 12 ▁▁right ▁▁after ▁▁the ▁▁inc ident ▁▁, ▁▁and ▁▁A ▁▁w as ▁▁ar res ted ▁▁by ▁▁the ▁▁p ol ice ▁▁on ▁▁the ▁▁sc ene ▁▁. ▁▁The ▁▁p ol ice ▁▁will ▁▁d ec ide ▁▁how ▁▁to ▁▁h and le ▁▁A ▁▁after ▁▁the ▁▁inv estigation ▁▁.
▁▁The ▁▁me eting ▁▁ex pl ained ▁▁the ▁▁operation ▁▁st atus ▁▁of ▁▁the ▁▁P yeong taek ▁▁P ort ▁▁, ▁▁s ought ▁▁ways ▁▁to ▁▁r ev ital ize ▁▁it ▁▁, ▁▁inc luding ▁▁ra ising ▁▁the ▁▁uti lization ▁▁r ate ▁▁, ▁▁and ▁▁d isc us sed ▁▁ways ▁▁to ▁▁c oo per ate ▁▁w ith ▁▁each ▁▁other ▁▁.
```

- `corpus.shuf.*.tok.post.bpe.*` 형태의 파일 몇개의 line으로 되어있는지 확인하기

```
$ wc -l corpus.shuf.*.tok.post.bpe.*
    202409 corpus.shuf.test.tok.post.bpe.en
    202409 corpus.shuf.test.tok.post.bpe.ko
   1200000 corpus.shuf.train.tok.post.bpe.en
   1200000 corpus.shuf.train.tok.post.bpe.ko
    200000 corpus.shuf.valid.tok.post.bpe.en
    200000 corpus.shuf.valid.tok.post.bpe.ko
   3204818 total
```

