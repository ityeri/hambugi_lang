HAMBUGI_LANG
===
제 친구는 요즘 `햄부기햄북 햄북어 햄북스딱스 함부르크햄부가우가 햄비기햄부거 햄부가티햄부기온앤 온을 차려오거라. 햄부기햄북 햄북어 햄북스딱스 함부르크햄부가우가 햄비기햄부거 햄부가티햄부기온앤 온을 차려오라고 하지않앗느냐.`
라는 밈에 푹 빠져있습니다.

이 언어는 코딩을 싫어하는 제 친구가
이 밈을 혐오할수 있도록 하기 위해서 만들어진 언어입니다.

확장자는 `.hbg` 입니다. ~~햄부기~~



기본 시스템
===

* 모든 변수는 부호가 있으며, 이상적으론 범위가 무한한 정수(int) 입니다.
  다루는 모든 데이터형 또한 기본적으로 부호있는 무한한 범위의 정수입니다.

* 기본적인 변수는 오직 3개이며, 기본값은 모두 0입니다.
  * `A`, `B`, `C`

---

* 정수형의 자료를 배열로 저장하는 무한한 크기의 메모리가 있으며,
  이 메모리로부터 정수 인덱스를 통해 값을 가져올수 있습니다.
  또한 아직 값이 지정되지 않은 메모리 위치의 기본값은 0입니다.

* 메모리의 주소는 0부터 시작합니다.



문법
===

* 모든 띄어쓰기, 줄바꿈은 무시됩니다.
  이 문서와 예제의 모든 띄어쓰기나 줄바꿈은 순수 가독성을 위함입니다.
  (인터프리터에 모든 줄바꿈과 띄어쓰기가 제거된 체로 코드가 입력됩니다.)

* 현재 초기 구현체에서 주석은 직접적으로 지원되지 않습니다.
  기본적으로 문법으로 인식되는 문자열 외에 모든 내용은 무시하지만,
  현재로썬 문법 외에 내용을 넣을경우 구현체가 **예상치 못한 행동을 할 가능성이 있습니다**



## 숫자 표현
모든 숫자는 기본적으로 정수로 표현됩니다.
`햄부가우가` 를 활용해서 숫자를 표현하며, 
`햄부` 뒤에 붙는 `가` 또는 `우` 의 갯수로 각 10진수의 자릿수를 지정합니다.

예로, 숫자 `328` 을 표현하고 싶다면,
`햄부 가가가 우우 가가가가가가가가` 형태로 씁니다.

* `햄부` 뒤에 오는 `가` 의 갯수가 총 3개 이기에,
  첫자리에는 3이 들어갑니다.
* 또한 이후에 오는 `우` 의 갯수는 2개 이기에 둘째자리는 2.
* 또 이후에 오는 `가` 의 갯수가 8개 이기에 셋째 자리는 8입니다.

결과적으로 이는 `328` 을 나타냅니다.

`우` 가 먼저 나와도 정상 작동합니다. 
즉, `햄부 우우우 가가 우우우우우우우우` 도 동일한 `328` 입니다.

0 을 나타내고 싶은 경우에는, `구` 를 사용할수 있습니다.
`201` 을 나타내고 싶은경우, `햄부 가가 구 가` 형태로 작성하면 됩니다.



## 변수 명칭

햄부기 언어에는 3가지의 변수가 있습니다. `A`, `B`, `C`.
~~조만간 2개로 줄일수도~~

이 3가지의 변수는 코드에서 각각 다른 방식으로 지칭합니다.

* `A` : `햄부`
* `B` : `햄북어`
* `C` : `햄북스딱스`



## 값 설정

상술한 명칭과 숫자 포현을 통해 
`햄부기` 명령어를 사용하여 특정 변수의 값을 설정할수 있습니다.
> `햄부기 <설정할 값> <설정될 변수>`

예로, `햄부기 햄부 가가가 햄북어` 는 `B` 의 값을 3 으로 설정하겠단 의미입니다.

설정할 값을 변수를 통해 지정할수도 있습니다.
> `햄부기 <설정할 값을 담은 변수> <설정될 변수>`

`A` 의 값을 `B` 로 설정하고 싶다면,
`햄부기 햄북어 햄부` 형태로 작성하면 됩니다.



## 값 연산

### 덧셈
덧셈은 `함부르크` 명령어를 이용하여 수행됩니다.
> `함부르크 <더해질 변수> <더할 수>`

`더해질 변수 += 더할 수` 의 형태로 수행됩니다.

예로, `A` 에 13 을 더하고 싶다면
`함부르크 햄부 햄부 가 우우우` 형태로 작성하면 됩니다.

변수끼리 더할수도 있습니다.
> `함부르크 <더해질 변수> <더할 변수>`

`더해질 변수 = 더해질 변수 + 더할 변수` 의 형태로 수행됩니다.

예로, `A` 에 3 이 있고, `C` 에 5 가 있다고 가정했을때,
`함부르크 햄부 햄북스딱스` 를 수행하면,
`A` 는 8 이 되고, `C` 는 원래 값인 5 가 그대로 있습니다.

---

### 뺄셈

뺄셈은 `햄부가티` 명령어를 이용하여 수행됩니다.
> `햄부가티 <빼질 변수> <뺄 수>`

`빼질 변수 -= 뺄 수` 의 형태로 수행됩니다.

예로, `A` 에 5 를 빼고 싶다면
`햄부가티 햄부 햄부 우우우우우` 형태로 작성하면 됩니다.

변수끼리 뺄수도 있습니다.
> `햄부가티 <빼질 변수> <뺄 변수>`

`빼질 변수 = 빼질 변수 - 뺄 변수` 의 형태로 수행됩니다,

예로, `A` 에 10 이 있고, `C` 에 3 이 있다고 가정했을때,
`햄부가티 햄부 햄북스딱스` 를 수행하면,
`A` 는 7이 되고, `C` 는 원래 값인 3 이 그대로 있습니다.



## 메모리 조작

### 읽기

메모리로 부터 값을 불러오는 작업은 `햄비기` 명령어를 통해 수행됩니다.
> `햄비기 <가져올 위치> <저장할 변수>`

예로, 메모리의 3번째의 값을 가져와 `B` 변수에 저장할려면
`햄비기 햄부 가가가 햄북어` 형태로 작성하면 됩니다.

메모리로부터 가져올 위치를 변수로 지정할수도 있습니다.
> 햄비기 <가져올 위치를 의미하는 변수> <저장할 변수>

예로, 메모리의 `A` 번째 위치로부터 값을 가져와 `C` 에 저장하고 싶다면,
`햄비기 햄부 햄북스딱스` 형태로 작성하면 됩니다.

---

### 쓰기

메모리에 값을 쓰는 작업은 `햄부거` 명령어를 활용합니다.
> `햄부거 <쓸 위치> <저장할 값>`

예로, 메모리의 3번째 위치에 2를 쓰고 싶다면,
`햄부거 햄부 가가가 햄부 가가` 형태로 작성하면 됩니다.

메모리에 쓸 위치, 쓸 값을 변수를 통해 지정할수도 있습니다.
> `햄부거 <쓸 위치를 의미하는 변수> <쓸 변수>`

예로, 메모리의 `A` 위치에 `B` 의 내용을 저장하고 싶다면,
`햄부거 햄부 햄북어` 형태로 작성하면 됩니다.



## 라벨

아래 서술할 분기 명령어의 분기 기준점이 되는 라벨을 작성할때 사용됩니다.
> `함부가` `함부가우가` `함부가우가우가` `함부가우가우가우가` ...

라벨은 `함부가` 뒤에 붙은 `우가` 를 기준으로 구분합니다.

> ⚠ `함부가우` 또는 `함부가우가우` 처럼 `우` 로 끝나는 라벨 명령문은
> 틀린 명령문 입니다.


## 분기

특정 변수나 숫자의 값이 0일 경우, 분기하는 작업은 `햄부기온앤온` 으로 수행됩니다.
> `햄부기온앤온 <0인지 확인할 변수 or 값> <분기 라벨>`

예로, `A` 변수가 0일때 `함부가우가` 로 분기하고 싶다면,
`햄부기온앤온 햄부 함부가우가` 형태로 작성하면 됩니다.

---

특정 변수나 숫자의 값이 0이 아닌 양수일경우 분기할려면, `햄부기온앤` 을 사용합니다.
> `햄부기온앤 <0이 아니며, 양수인지 확인할 변수 or 값> <분기 라벨>`

예로, `B` 의 값이 0이 아닌 양수일경우 `함부가우가우가` 로 분기하고 싶다면,
`햄부기온앤 햄북어 함부가우가우가` 형태로 작성하면 됩니다.

---

특정 변수나 숫자의 값이 0이 아닌 음수일경우 분기할려면, `햄부기앤온` 을 사용합니다.
> `햄부기앤온 <0이 아니며, 음수인지 확인할 변수 or 값> <분기 라벨>`

예로, `B` 의 값이 0이 아닌 양수일경우 `함부가우가우가` 로 분기하고 싶다면,
`햄부기앤온 햄북어 함부가우가우가` 형태로 작성하면 됩니다.



## 출력

출력 명령은 `를 차려오거라` 를 통해 수행됩니다.
> `<출력할 값> 를 차려오거라`

숫자를 유니코드 기준 문자로 변환하여 출력합니다.

예로, 문자 `쬄` 을 출력하고 싶을경우, `쬄` 은 유니코드로 `U+CB04` 이며,
십진으론 `51972` 입니다.

때문에
```hbg
햄부 가가가가가 우 가가가가가가가가가 우우우우우우우 가가 를 차려오거라
```
라고 작성할시 문자 `쬄` 이 출력됩니다.

---

특정 변수의 내용을 출력하는것 또한 가능합니다.
> `<출력할 변수> 를 차려오거라`

`A` 변수의 내용을 출력하고 싶다면,
`햄부 를 차려오거라` 형태로 작성하면 됩니다.

> ⚠ 변수에 51972가 들어있을 경우 `51972` 가 그 숫자 그대로 출력되는게 아닌,
> 51972를 유니코드로 변환한 `쬄` 이 출력됩니다,



## 입력

입력은 `에 차려오라고 하지않앗느냐` 를 활용하여 수행 됩니다.
> `<저장할 변수> 에 차려오라고 하지 않았느냐`

`A` 변수에 사용자의 입력을 저장하고 싶다면,
`햄부 에 차려오라고 하지 않았느냐` 형태로 작성하면 됩니다.

> ⚠ 사용자의 입력은 유니코드 한 글자로 받으며,
> 사용자가 `쬄` 을 입력할 경우 
> 변수에는 이를 유니코드 기준 숫자로 변환한 `51972` 가 저장됩니다.



QnA
===

Q. 와 구현체다!

A. 있긴한데 아직 분기 구현 안함;;

---

Q. 이거 튜링 완전 맞죠?

A. 구현체 완성해서 테스트 해봐야 할듯요 
~~근대아마맛지안를가~~

---

Q. 오류 있는거 같은데 확실치가 않아요

A. 오탈자든, 문법 충돌이든, 맞춤법이든, 서식이든
그냥 이상하다 싶은거 있음 일단 이슈 써주세요 ~~뇌 빼고 작성한지라~~



TODO
===
음수 표현 추가
분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투분기고투