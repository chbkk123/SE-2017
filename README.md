# SE-2017
2017 CSE4006 Software Engineering

# 오픈소스 노트 앱 설명
이 오픈소스 노트 앱은 Django와 Polymer를 활용해서 만들었습니다.

이 노트앱에서 메모를 작성하면, 메인 화면에 그 메모의 제목과 마지막으로 수정된 날짜가 나열되어있으며, 메모 제목을 클릭하면 그 메모로 이동해 메모의 상세 내용을 볼 수 있고, 메모를 읽던 중 그 메모를 수정하려하거나 메모를 삭제할 수 있습니다.

원래는, 메모 작성/수정 화면에서 화면 우측에 자세한 현재 시간은 아니지만, 지금 날짜를 알 수 있는 달력과 함께 메모에 `**볼드**, _이탤릭_`을 넣어서 메모를 작성할 수 있게 하려고 했으나, 폴리머에 존재하는 텍스트 에디터를 적용시켜 메모의 제목과 내용을 입력하고 그 내용을 저장하게 하는 방법을 찾지 못하여 Django를 사용하는 법을 알려주는 [튜토리얼](https://tutorial.djangogirls.org/ko/)에서 알려주는 블로그 제작과, 그 블로그에 포스트를 올리고, 수정하고, 삭제하는 기능을 그대로 메모장으로 활용하는 방법으로 만들었습니다.

>만약 메모를 작성할 수 없을 경우, Django 블로그의 슈퍼유저가 로그인 된 상태로, 그 유저가 포스트를 올리고 수정하고 지우는 형태로 구현한 모양만 메모장 앱이여서 그러는 것으로 추정됩니다. 주소 뒤에 `/admin`으로 들어가 슈퍼유저로 로그인해야 합니다. 앱을 만드는 도중에 사용하지 않고 추가로 만들어놓은 슈퍼유저의 id는 home. password는 homework 입니다.
***
## 메인 화면 설명

상단의 **메모장**과 ![](http://postfiles13.naver.net/MjAxNzA0MjdfNTYg/MDAxNDkzMjc4MjQ1NzY1.w2ZwOS8WSx9LeQDVFwOzs_EhL7-H25T1a-xAB5HW8Kgg.kE3Hdi4z1doYlJWaD4m0TcmhYUZSpo_SBDXAwafF01kg.PNG.chbkk123/%EB%A9%94%EB%AA%A8%EC%9E%91%EC%84%B1.PNG?type=w3)가 있는 구분선은 메모장 앱의 기본이 되는 틀이며, 어떤 화면으로 넘어가도 공유하는 틀입니다.

>**메모장**은 이 앱이 Django 블로그와 그 포스트를 외부에서 게시, 수정, 삭제하는 것으로 구현되어있지만 메모장으로 만들었다고 주장하기 위해 적었으며, 클릭하면 메모장 앱의 메인 화면으로 무조건 이동하는 기능을 지니고 있습니다.

>![](http://postfiles13.naver.net/MjAxNzA0MjdfNTYg/MDAxNDkzMjc4MjQ1NzY1.w2ZwOS8WSx9LeQDVFwOzs_EhL7-H25T1a-xAB5HW8Kgg.kE3Hdi4z1doYlJWaD4m0TcmhYUZSpo_SBDXAwafF01kg.PNG.chbkk123/%EB%A9%94%EB%AA%A8%EC%9E%91%EC%84%B1.PNG?type=w3)는 새 메모를 입력하는 화면으로 이동하는 기능을 지니고 있으며, 어느 화면에서도 이 두 버튼은 작동하기 때문에 메모를 수정하거나 작성하고 있을때 클릭하지 않도록 주의하는 편이 좋습니다.

기본적으로 아무런 메모도 작성되어있지 않다면, 메인 화면에서는 상단의 틀 이외에는 아무것도 표시되지 않습니다.

![](http://postfiles3.naver.net/MjAxNzA0MjdfMzcg/MDAxNDkzMjc4MjQ2ODUx.xdpEbEI80nyS8ye8ohGszQ6PwRaAUA-AGLKrDyV-cRUg._Hy19KLev4dx4qDA23ZTNR0SNB_cCDloKWuybZ0oE90g.PNG.chbkk123/%EB%A9%94%EC%9D%B8%ED%99%94%EB%A9%B4.PNG?type=w3)


메모가 작성되어있다면, 아래와 같이 그 메모의 제목과 마지막으로 수정된 시간이 표시됩니다. 만약 작성 후 수정한 적이 없는 메모라면 그 시간은 메모가 작성된 시간을 나타내는 것입니다.

![](http://postfiles3.naver.net/MjAxNzA0MjdfMTc4/MDAxNDkzMjc4MjQ2Njc2.wpPVjnO9cHNbmwXQKMIc0M64JZr_jxIOiOb2B8KGwoAg.hIdKPjWBsTVJfdEC1iZ6CNwAliXAUZRqrfPh2-VLc54g.PNG.chbkk123/%EB%A9%94%EC%9D%B82.PNG?type=w3)

메모를 읽고 싶다면, 원하는 메모의 제목을 클릭하면 그 메모로 이동합니다.


## 메모 읽기 화면 설명

메모를 읽기 위해 제목을 클릭하면 다음과 같은 화면으로 이동합니다.

![](http://postfiles4.naver.net/MjAxNzA0MjdfNzAg/MDAxNDkzMjc4NTI1MDU4.hg-S9uk33QXcePT73_jgLHj70x6HVPB5ghYWBkmmz-Mg.mhi3Sqr65oLyQtvBw3l_rdF-amSLaLDLDN-aXTlUXo0g.PNG.chbkk123/%EB%A9%94%EB%AA%A8%EC%9D%BD%EA%B8%B0.PNG?type=w3)


메모 제목과 내용은 그 크기와 글씨 색으로, 그리고 공백으로 구분되어 한 눈에 알 수 있으며, 메모 내용이 끝나면 이 메모의 마지막 수정 시간이 기록되어 언제 작성/수정된 것인지 알 수 있습니다.

메모 제목 위에 존재하는 버튼은 메모 수정 버튼이며, 수정 시간 아래의 버튼은 메모 삭제 버튼입니다.

> ![](http://blogfiles.naver.net/MjAxNzA0MjdfMjkx/MDAxNDkzMjc4MjQ1MjY1.XxKiGYIa-w6N0v6s8bDPy4lYWKxLql7kzGpeQQnUrsUg.tgptnB5x7kIeTIkGpdmwtw7TS7168qffhbFlQ-wOQYUg.PNG.chbkk123/%EB%A9%94%EB%AA%A8_%EC%88%98%EC%A0%95.PNG)는 클릭하면 메모 작성화면으로 이동하지만, 그 제목과 내용은 이미 그 메모의 제목과 내용이 입력되어있기 때문에 그 제목과 내용을 고칠 수 있습니다.

> ![](http://postfiles7.naver.net/MjAxNzA0MjdfMTI3/MDAxNDkzMjc4MjQ1NDg1.e2Ei2auyEycAGOzE0ZlOad-TfWJ3m16714a7vtpQWNgg.xirgzLCR0P9ZZieSdQvb4rOSWrtud4J_oQU2GCvW2p4g.PNG.chbkk123/%EB%A9%94%EB%AA%A8%EC%82%AD%EC%A0%9C.PNG?type=w3)는 클릭하면 즉시 현재 읽고있는 메모를 삭제합니다. 안전을 위한 확인 질문을 하지 않고 즉시 삭제하기 때문에, 삭제할때 주의해서 삭제해야 합니다.


## 메모 작성 화면 설명

메모를 작성하고자 ![](http://postfiles13.naver.net/MjAxNzA0MjdfNTYg/MDAxNDkzMjc4MjQ1NzY1.w2ZwOS8WSx9LeQDVFwOzs_EhL7-H25T1a-xAB5HW8Kgg.kE3Hdi4z1doYlJWaD4m0TcmhYUZSpo_SBDXAwafF01kg.PNG.chbkk123/%EB%A9%94%EB%AA%A8%EC%9E%91%EC%84%B1.PNG?type=w3)버튼을 누르거나, 메모 읽기 화면에서 메모를 수정하고자 ![](http://blogfiles.naver.net/MjAxNzA0MjdfMjkx/MDAxNDkzMjc4MjQ1MjY1.XxKiGYIa-w6N0v6s8bDPy4lYWKxLql7kzGpeQQnUrsUg.tgptnB5x7kIeTIkGpdmwtw7TS7168qffhbFlQ-wOQYUg.PNG.chbkk123/%EB%A9%94%EB%AA%A8_%EC%88%98%EC%A0%95.PNG)버튼을 누르면 다음과 같은 화면으로 이동합니다.

![](http://postfiles4.naver.net/MjAxNzA0MjdfMTE3/MDAxNDkzMjc4MjQ2MTE3.ri-6IcsO6vk5FWdd4bKtT3Hl4iEeXHFnpKT1olq6SV0g.LEW_wwXZyQhRXIcdAwGYXIaS1T3f14rOz1boaHTuVwYg.PNG.chbkk123/%EB%A9%94%EB%AA%A8%EC%9E%91%EC%84%B1.PNG?type=w3)


현재 메모를 작성중이라고 알려주는 문자와 그 아래에는 달력 컴포넌트로 지금 날짜를 표시하고 있습니다. 다만 그 시간은 알 수 없습니다. 또한 달력의 날짜를 변경할 수는 있지만, 단순히 달력의 기능일뿐 메모 수정 시간에 영향을 주지는 않습니다.

이 후에 메모의 제목과 내용을 작성하고, 저장 버튼을 누르면 현재 메모가 저장되고, 지금 작성을 완료한 메모를 읽는 메모 읽기 화면으로 이동합니다. 만약 메모의 제목이나 내용 중 하나라도 입력하지 않고 저장 버튼을 누른다면, 아래와 같은 문구가 뜨며 메모를 저장하지도, 화면이 이동하지도 않습니다.

![](http://postfiles5.naver.net/MjAxNzA0MjdfMTY5/MDAxNDkzMjc4MjQ2MzQ5.OjSrEluhg3y2sHqPXJ-1km7pocE53afY9qTKUJVYSXMg.T5Pg0Q-AQH6tseKs0mumIwOy6Pxjuz6Ep-P2PFlEMeIg.PNG.chbkk123/%EB%A9%94%EB%AA%A8%EC%9E%91%EC%84%B1%EC%98%A4%EB%A5%98.png?type=w3)
