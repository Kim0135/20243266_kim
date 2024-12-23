# 야구 체크스윙 판독기

### 분반, 팀, 학번, 이름
- (가)반, 20243266, 김승민
<hr/>

## 1. 요약
>야구 체크스윙을 판단하는 프로그램을 만들려고 한다. 야구에는 다양한 룰들이 존재하고 중요한 부분에는 비디오 판독이나 AI를 사용하곤 한다. 아웃, 세이프 판정에는 비디오 판독을 사용하고, 볼, 스트라이크 판정에는 ABS라는 AI를 사용한다. 하지만 체크스윙을 판단하는 것은 오로지 심판의 몫이다. 체크스윙이란 타자가 공을 치려고 스윙을 하다가 중간에 멈추는 동작을 말한다. 이 스윙의 판정에 따라 볼인지 스트라이크인지 정해지기 때문에 비디오 판독이나 AI를 도입해야 한다고 생각한다. 이 프로그램이 실제로 사용된다면 억울한 판정이 없어질 것이라고 예상한다.


## 2. 서론
야구는 전 세계적으로 사랑받는 스포츠 중 하나로, 경기에서 스트라이크와 볼의 판정은 타자와 투수의 대결에 결정적인 영향을 미칩니다. 그중 체크스윙은 타자가 스윙을 하려다가 중간에 멈추는 동작으로, 그 여부를 판단하는 것은 스트라이크나 볼을 결정짓는 중요한 요소입니다. 그러나 체크스윙 판정은 심판의 주관적인 판단에 의존하기 때문에 정확성과 일관성에 대한 논란이 끊이지 않고 있습니다.

국내에서도 체크스윙 판정에 대한 논란은 종종 발생해 왔습니다. 특히 2022년 한국 프로야구(KBO) 리그에서 일어난 몇몇 중요한 경기에서는 체크스윙 여부를 둘러싼 판정이 경기 결과에 큰 영향을 미친 바 있습니다. 2022년 KBO 플레이오프 경기에서 체크스윙 논란이 발생해 판정의 공정성에 대한 비판이 제기되었으며, 이러한 논란은 판정의 일관성과 정확성에 대한 의문을 불러일으켰습니다.

현재 KBO 리그를 포함한 야구 경기에서 체크스윙 판정은 여전히 심판의 주관적인 시각에 의존하고 있습니다. 빠른 투구 속도와 타자의 즉각적인 반응을 정확하게 판단하기 어려운 상황에서 종종 판정 논란이 발생하며, 경기의 공정성과 신뢰성에 부정적인 영향을 미칠 수 있습니다. 이러한 상황에서 판정의 객관성을 강화할 수 있는 기술적 해결방안이 필요합니다.

체크스윙 판정의 신뢰성을 높이기 위해 비디오 판독 시스템과 인공지능 기술을 결합한 자동화 판정 시스템 도입이 유망한 해결책이 될 수 있을 것입니다. 고속 카메라와 영상 분석 기술을 사용하여 타자의 스윙 궤적을 실시간으로 분석하고, 인공지능이 타자의 스윙 범위를 파악함으로써 더 정확하고 일관된 판정이 가능합니다. 이러한 시스템은 심판의 주관적 판단을 보완하거나 대체하여, 경기의 판정 오류를 줄이고 공정성을 높이는 데 기여할 것입니다.

이번 프로젝트는 체크스윙 판독 프로그램을 개발하고, 인공지능과 영상 분석 기술을 통해 체크스윙 판정의 정확성을 향상시키는 것을 목표로 합니다. 이를 통해 국내 야구 경기에서 판정의 공정성을 높이고, 경기의 신뢰성을 강화할 수 있을 것으로 기대됩니다.

## 3. 본론
체크스윙 판독 프로그램을 개발하기 위해서는 다양한 기술적 요소가 필요합니다. 주요 기술은 크게 컴퓨터 비전, 머신러닝/딥러닝, 그리고 데이터 처리 및 분석 기술로 나눌 수 있습니다.

- **컴퓨터 비전**: 영상 데이터를 처리하고 분석하는 기술로, 체크스윙 판독에 중요한 역할을 합니다. 카메라로 촬영된 선수의 스윙 영상을 처리하여 배트의 궤적과 손목 및 팔의 움직임을 정확하게 추적할 수 있어야 합니다. 이 과정에서 객체 추적과 영상 분할 기술이 핵심입니다. 여러 각도에서 촬영된 영상을 분석하여 정확한 스윙 정보를 추출하는 것이 중요합니다.

- **머신러닝/딥러닝**: 체크스윙 여부를 판단하는 알고리즘은 머신러닝 또는 딥러닝 기술을 활용해 개발할 수 있습니다. 특히, CNN 같은 딥러닝 모델은 배트와 손목 움직임을 학습하고 분석하는 데 매우 적합합니다. 이 과정에서 대량의 체크스윙 영상 데이터를 수집하여 모델을 학습시켜야 합니다. 또한, 체크스윙 판독을 위한 기준을 설정하기 위해 지도학습 기법을 사용할 것입니다.

- **실시간 처리**: 실시간 경기 중 체크스윙을 판독하기 위해서는 고속으로 영상을 처리할 수 있는 시스템이 필요합니다. 이를 위해 병렬 처리와 고속 프레임 분석 기술이 요구되며, GPU를 활용한 실시간 데이터 처리도 필수적입니다. 여러 카메라에서 수집된 데이터를 효과적으로 분석하고 불필요한 데이터를 제거하는 것도 중요합니다.

체크스윙 판독 프로그램의 구현은 다음과 같은 단계로 이루어집니다.
1. 다양한 야구 경기에서 체크스윙 데이터를 수집합니다. 경기 영상 및 연습 영상을 통해 스윙의 특징을 정의하고, 이를 학습 데이터로 사용할 수 있도록 전처리합니다.
2. 전처리 단계에서는 OpenCV와 같은 영상 처리 라이브러리를 이용해 배트와 손목의 움직임을 추적하고, 노이즈를 제거합니다.
3. 이렇게 전처리된 데이터를 기반으로 CNN모델을 설계하고 학습시킵니다. 이 모델은 배트의 궤적과 손목의 움직임을 분석하여 체크스윙 여부를 판단합니다.
4. 다양한 각도에서 촬영된 영상을 활용하여 모델의 성능을 향상시키고, 실시간 판독이 가능하도록 최적화해야 합니다.
5. 실시간 판독 시스템을 구축하고, 고속 카메라와 GPU 서버를 연결하여 영상을 실시간으로 처리하고 분석하는 시스템을 구현합니다. 또한, 결과를 심판과 방송 장비에 즉시 전달할 수 있도록 UI 시스템도 설계합니다.

체크스윙 판독 프로그램의 성공적인 개발을 위해서는 다음과 같은 방향을 고려해야 합니다.
- **데이터 확보**: 다양한 선수의 스윙 스타일, 경기 환경, 조명 조건 등을 고려하여 포괄적인 데이터를 수집해야 합니다.
- **시스템 성능 최적화**: 실시간 경기에서 지연 없이 판독 결과를 제공하기 위해 GPU 활용을 극대화하고, 알고리즘의 경량화를 통해 처리 속도를 높여야 합니다.
- **UI 설계**: 판독 결과는 심판이나 사용자로부터 피드백을 받아 지속적으로 개선하고, 사용자가 판독 결과를 쉽게 이해할 수 있도록 UI 설계에도 신경 써야 합니다.

## 4. 결론
본 보고서에서는 야구 체크스윙 판독 프로그램을 개발하기 위한 기술적 요소, 구현 방법, 그리고 향후 발전 가능성에 대해 논의했습니다. 체크스윙은 경기에서 심판의 주관적인 판단에 의존하는 경우가 많기 때문에, 객관적이고 공정한 판독 시스템이 필요합니다. 이를 해결하기 위해 컴퓨터 비전과 딥러닝 기술을 결합한 자동화된 판독 시스템은 매우 효과적인 해결책이 될 수 있습니다. 특히, 고속 카메라와 객체 추적 기술을 활용해 선수의 배트와 손목 움직임을 분석하고, CNN 기반의 머신러닝 모델을 통해 실시간으로 체크스윙 여부를 판단하는 것이 핵심입니다. 또한, 판독 시스템의 실시간 성능 최적화와 다양한 데이터를 활용한 모델 학습이 중요한 성공 요소로 작용할 것입니다.
<hr/>

## 5. 출처
1. 하무림, <끊이지 않는 체크 스윙 오심 논란…비디오 판독 도입 늦어지는 이유는?>, KBS 뉴스, 2024.06.24, <https://news.kbs.co.kr/news/pc/view/view.do?ncd=7994959> (2024.10.17)   
2. KBO 규정 <https://www.koreabaseball.com/kbo/league/gamemanage2024.aspx> (2024.10.15)   
3. 얇은생각, <인공지능 : CNN(Convolutional Neural Networks) 개념, 예제, 분석>, 티스토리, <https://jjeongil.tistory.com/544> (2024.10.14)   
