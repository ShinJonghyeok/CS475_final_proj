# Marked Personas: Using Natural Language Prompts to Measure Stereotypes in Language Models

[논문 링크](https://aclanthology.org/2023.acl-long.84.pdf)

## 1.	Introduction

### 1.1 LLM과 stereotype

여러 사람들에게 정보를 제공하는 LLM에서 stereotype이나 social bias는 문제다.

### 1.2 기존 stereotype 측정 방법들의 한계

stereotypical 관계를 측정하는 인위적인 템플릿에서 수동적으로 만든 데이터셋 혹은 사람이 쓴 stereotype을 포함하는 문장에 의존한다.

특정 인구 집단에 대한 stereotype인지를 특정하는 것, 좀 더 넓은 범위의 집단으로 일반화하는 것 사이 trade-off가 있다.

타자화(othering)나 비유하는 것과 같은 은근한 패턴을 잡지 못한다.

특히, 다른 일반적인 문장에서 긍정적인 것으로 분류되지만 stereotype을 내포하고 있는 단어들을 못 잡아낸다.

### 1.3	Marked Personas

#### 1.3.1 Concept

비지도, lexicon-free 방법. natural language prompt로 어떤 집단이든 그에 관한 stereotype을 잡는다.

Persona랑 Markedwords로 구성. 처음에 LLM한테 특정 집단 소속 가상인물 설명(persona) 만들어달라고 한다.

같은 prompt를 사용해서 LLM vs 사람에서 stereotype 정도를 비교 가능하다. 이 비교는 Lexicon-based 방법의 한계를 보여줄 것.

Marked Words는 LLM이 지배 그룹과 특정 그룹을 어떻게 다르게 그리는가 보여주는 방법이다.

Markedness 개념에서 왔는데 marked랑 unmarked 사이 언어적, 사회적 차이를 보여주는 것임.

그 차이를 명확하게 보여주는 word가 Marked Words임.

#### 1.3.2 차별점

데이터셋, lexicon, 라벨링 필요 없다. “인구 집단(ex black woman)”, “unmarked default(ex white, man)” 두 개만 정해주면 된다. Corpus 정해지지 않고, 다양한 차원의 인구 모델 만들기 가능. 다른 연구에도 쉽게 적용될 것.

#### 1.3.3 특징

기존에 간과하던 긍정적이고 무해해 보이지만 특정 집단에게 차별적인 패턴도 잡아냄.

#### 1.4 논의 거리

Stereotype을 anti-stereotype으로 바꾸는 게 어떻게 기존 규범을 강화하는지, 그게 어떻게 활용되는지 볼 것. LLM 제작자에게 바치는 충고.

## 2.	Background and Related Work

논문의 모델은 Markedness에 기반함.

Markedness는 index – indices의 관계와 같이 단어 원형이 unmarked, 변형된 것이 marked라는 문법적 개념에서 출발함.

비문법적인 것으로 확장되면 white나 man 같이 주류가 unmarked, 비주류가 marked임. 백인 우월주의, 가부장제의 영향에 markedness 밀접하게 연관되어 있음.

Stereotype, 주류와 비주류 인식 차이는 이런 권력을 강하게 함. Stereotype을 “사회 계층을 구체화”하는 특성으로 정의했다.

LLM에서 Stereotype, bias 측정하는 방법은 많이 있는데, 그 중에서 Marked Personas(이하 MP)는 다른 모델 점수가 3/5가 최대인 것과 달리 4/5다.

Metric은 다음과 같다.

i)	Generalize to new demographic groups

ii)	Is grounded in social science theory

iii)	Is exhaustively characterized the full range of stereotypes

iv)	Use natural-language LLM inputs

v)	Capture specific stereotypes

iii) 빼고 다 만족함.

Exhaustiveness 면에서 보자면 Marked Personas는 exhaustive(철저하게) 모든 stereotype을 특성화하는 것보다 다른 인구 집단의 표상에서 특정 데이터셋 패턴을 특성화하려고 했다.

따라서 Marked Personas는 문화적으로 종속되거나 꾸준히 진화하는 stereotype도 잡아낼 수 있다.

sexism, racism 등의 다면적 요소들이 bias나 harm을 합쳐서 나타내기도 하는데 Marked Personas는 그것도 잡아낸다. (다른 모델들은 angry black woman나 직업으로 잡아냄)

## 3.	Methods

### 3.1 Personas: Generating Intersectional Portrayals

#### 3.1.1 LLM Personas

논문은 제약 없는 생성에서 stereotype을 측정하려 한다. Zero-shot setting (아무 인자도 주지 않았음)에서 LLM에게 자연어 프롬프트를 준다.

Ex) “Imagine you are an Asian woman. Describe yourself.”

여기서 LLM이 출력하는 것이 특정 인구 집단에 속하는 개인의 자연어 묘사, 즉 persona다. 위의 예시에서는 Asian woman.

여기서 persona는 정체성보다 유연하고 즉석에서 만들어지는 언어학적인 의미에 가깝다. 특히 HCI나 NLP에서 persona는 가상의 인물 모델로 쓰인다.

매 생성마다 다면적인 사회적 정체성을 지니는 persona가 나오고, 그로부터 LLM이 여러 정체성 집단의 조합의 사람을 어떻게 표현하는지 알 수 있게 해준다.

![Prompt for generating persona](imgs/img1.png)
 
논문에서 Persona를 만들기 위해 사용한 프롬프트. (성별), (인종), (성별, 인종) 집단을 만들어 줌.

특징적으로 첫 번째 프롬프트에는 your goal~explicitly라는 문장이 있는데 이게 stereotype 만드는 것을 더 부추기기 때문에 처음에는 다른 프롬프트부터 사용함.

Stereotype을 좀 더 확실하게 측정하기 위해 워딩이나 길이를 다양하게 함. 분석 시 Top word에 따른 차이가 의미 있게 나지 않아 프롬프트에 따른 output을 전체적으로 봄.

#### 3.1.2 Human-written Personas

평균 나이 30살 미국 사람들로부터 추출. 각 참가자는 자신을 설명하는 output 하나, imaginary race라고 생각하고 자기 소개 하나 작성.

(실제 흑인, 실제 백인, 가상 흑인, 가상 백인)이 나옴. 이 방법을 생각해 낸 논문 저자에 따르면 가상 흑인이 stereotype이 가장 많음.

프롬프트는 다음과 같음. 이와 동일한 프롬프트를 써서 만들어진 persona와 사람이 쓴 응답을 비교할 것임.

![Prompt for getting human-written persona](imgs/img2.png)

### 3.2 Marked Words: Lexicon-Free Stereotype Measurement

Unmarked된 집단과 특정 집단을 구분 짓는 단어 세트 : Marked Words.

Set of marked groups S 정의하고 $s \in S$에 대한 persona set $P_s$를 다른 unmarked group과 구분하게 하는 단어들을 찾는다.

Fightin’ Words method를 사용해서 분석할 것임.

Informative Dirichlet prior를 사용함.

첫째로, $P_s$와 그에 해당하는 unmarked identity의 log-odds ratio를 구함.

데이터셋에서 자세히 보고자 하는 셋들을 제외한 다른 텍스트들이 prior distribution을 맡아줌.

이때 통계적으로 중요한 정도는 z-score로 측정함. z-score > 1.96이면 중요하다고 생각됨.

이때, unmarked identity와 $P_s$의 통계적으로 중요한 단어들이 나올텐데 여러 unmarked identity에 대한 측정 후 그들의 교집합에 있는 단어들을 꺼냄.

예시1) Singular group : 인종 $e \in E$, $P_e$와 $P_White$에 대한 log-odd ratio 구하고 z-score 높은 단어들 구함.

예시2) Intersectional group : 인종-성별 $eg \in E \times G$, $P_eg$와 $P_man$ / $P_eg$와 $P_White$에 대한 log-odd ratio를 각각 구하고 공통적으로 z-score가 높은 단어를 추출.

실제 사회적으로 강한 그룹은 다양할 수 있는데 인터넷 기반 데이터셋에서는 백인, 남자가 주류였음.

English LLM은 그런 데이터셋을 쓰므로 백인, 남자를 각각 unmarked default로 삼았음.

이 사회적 카테고리는 여러 문맥에 따라 달라질 수 있고, Marked Personas는 다른 문맥에서도 적용될 수 있을 것임.

#### 3.2.1 Robustness Checks: Other Measures

Marked Words 결과가 잘 되었는지 다른 측정법으로 교차 검증함.

**Classification**

1 vs all SVM classification으로 top words 구함.

이 방법은 1. 주어진 집단의 persona가 데이터셋의 다른 모든 persona들과 구분이 되는지, 2. 이 persona들을 구분하는 특징들을 보여준다.

이 방법을 쓰려면 데이터 익명화, 문장 부호 제거, 대문자 제거, 대명사 제거, 성별/인종을 명확하게 나타내는 단어들(Smith et al.(2022)에서 가져왔다 함) 제거 해야 함.

각 persona p를 bag of words로 보고 top words 뽑아내면 classified!

**Jensen-Shannon Divergence(JSD)**

각 marked group에 대해서 JSD의 Shifterator implementation을 사용함.

marked persona를 unmarked persona로부터 다르게 만들어주는 top 10 단어들을 계산해 줌.

## 4. Experiments

OpenAI's API를 사용하는 여러 모델에서 시도를 했음. 메인은 GPT4, GPT3.5(text-davinci-003)임.

세팅 : (maximum length = 256, top P = 1, frequency penalty = 0, presence penalty = 0, best of = 1) : default setting, temperature = 1. GPT4에 대해서는 max_tokens = 150. GPT-3.5는 2022년 12월에, 나머지는 2023년 5월에 2023-03-15-preview API 버전 사용해서 문장들 생성.

ChatGPT, 구형 GPT, non-OpenAI 모델들은 제한 사항들이 있었음. 몇몇은 일관성 있는 답을 내주지 못했었음.

Marked Personas는 인구 집단의 어떤 교집합에 대해서도 결과를 만들어낼 수 있지만, Ghavami and Peplau(2013)가 제시한 카테고리를 사용했음. nonbinary gender도 추가함.

그래서 인종은 5가지 (Asian, Black, Latine, Middle-Eastern, White), 성별은 3가지 (man, woman, nonbinary), 성별-인종은 15가지를 탐구하게 됨.

2개의 모델, 한 모델 당 15개의 카테고리, 카테고리 당 6가지 프롬프트, 프롬프트 당 15개 샘플 = 총 2700개 persona.

다음은 예시 persona임.

![Example persona generation](imgs/img3.png)

Marked Words 프레임으로 인종 축, 성별 축에 대해서 marked group이 어떻게 다른지 통계적으로 중요한 단어들만 뽑아냄.

교차 검증을 위해 JSD, 1 vs all SVM classification 사용.

SVM에 대해서는 training data 80%, test data 20%로 나눠서 적용.

서로 다른 인구 집단의 설명은 구분하기 쉬웠음. SVM 정확도가 GPT4에서는 0.96 $\pm$ 0.02, GPT3.5에서는 0.92 $\pm$ 0.04로 꽤 높게 나오는 것을 볼 수 있었음.

Marked Words, JSD, SVM에서 top words는 공통점이 의미 있게 많았음.

## 5. Persona Evaluation: Comparison to Human-written Personas

LLM 생성 output과 human-written output을 비교하기 위해서 백인, 흑인 stereotype 속성 리스트를 사용.

persona들에서 평균적으로 몇 퍼센트의 단어가 백인, 흑인 stereotype lexicon에 포함되어 있는지 셌음.

다음은 실제 그래프임.

![Percentage of words in lexicon](imgs/img4.png)

Lexicon에 따르면 LLM 생성 persona가 human-written보다 더 많은 stereotype을 가지고 있는 것을 보여줬음.

GPT4 persona에서 흑인 stereotype은 흑인 persona에서, 백인 stereotype은 백인 persona에서 더 잘 나타났음.

예시) GPT4 Black Persona : "As a Black man, I stand at a *tall* 6'2'' with a strong, *athletic* build"

이탤릭체 시켜놓은 게 흑인 stereotype lexicon에 포함된 단어들.

**Shortcomings of Lexicons**

분석해보니 human-written data가 더 넓은 분포의 stereotype 단어들을 포함함. LLM이 만든 persona는 감정 분석에서 긍정적으로 보이는 단어들만 포함함.

다음은 실제 그래프임.

![Gen vs Human](imgs/img5.png)

흑인 persona에서 Lexicon으로 잡아내지 못하는 패턴이 관측됨. 백인 persona에서 관측되지 않으나 흑인 persona에서만 관측되는 단어는 해로운 단어임. 이런 점에서 unsupervised manner의 Marked Personas가 필요.

GPT4와 달리 GPT3.5에서는 백인 persona에서도 흑인 stereotypes가 포함되어 있었음. 이를 통해 어떤 표상이나 stereotype이 lexicon들로 하여금 잡아내지 못하게 하는 걸까?를 도출함.

## 6. Analyzing Marked Words: Pernicious Positive Portrayals

Marked Words로 잡아낸 top words를 관측할 것. 대체로 이들은 긍정적인 감정을 표하나 문제 있는 표상이나 stereotype을 보임.
"essentialism"과 "othering"을 볼 수 있음. (본질, 타자화로 번역했는데 한국인이라면 마늘 냄새 남~~이라던지, 얘기할 때 우리는 피자 좋아하고 너네는 ~~과 같이 인종이나 성별 같은 카테고리로 다른 사람처럼 대하는 걸 의미하는 걸로 받아들였음)

다음은 Marked Words가 뽑아낸 단어 목록임.

![Top words of generated persona](imgs/img6.png)

특이한 점으로는 성별 / 인종에서 축 하나로만 나눈 데에서는 안 나오던 unique한 단어들이 성별-인종 그룹에서 나타났다는 것임.

ex) strong, resilient Black woman.

**Sentiment and Positive Stereotyping**

이 method는 감정에 구애받지 않고 top words를 뽑아내는데 top words를 보면 긍정적인 단어가 많음.

아마 OpenAI의 bias 약화 기능에 의한 것인 듯함.

감정 분석은 -1(부정) ~ +1(긍정)을 판단해주는 NLTK의 VADER sentiment analyzer를 사용함.

(mean, std) GPT4 : (0.83, 0.27) GPT3.5 : (0.93, 0.15). Top words : (0.05, 0.14)

긍정적임에도 불구하고 단어들이 끼치는 해악은 분명 존재함.

예를 들면 성별에서 소수자들(여성 포함)이 부적절한 칭찬을 통한 차별을 받는다던가 동등한 기회를 주는 프로그램에서 특정 인종이 간과된다던가.

다른 면에서, 특정 인종 종교에 대한 긍정적이고 동질적인 표현이 다문화주의나 anti인종차별주의를 기르는 것처럼 보이지만 기저에 체계적인 인종차별주의를 가능하게 하는 logic을 따르는 것을 볼 수 있다.

**Appearance**

외모와 관련된 단어를 보면, 백인 집단에 대해서는 객관적인 설명을 쓰나 그게 아닌 unmarked group에서는 petite나 colorful, curvy 같이 백인 표준에 따라 비교했을 때만 의미 있는 단어들이 보임.

심지어 백인 표준은 백인우월주의와 연관된 것임.

와중에 소수 그룹은 대상화되고 비인간화되어 표현되었다.

ex) Asian Women : almondshaped, petite, smooth 특히 이국적이고, 복종적이고, 지나치게 성적인 이미지를 그려냄.

ex) Latina Women : vibrant, curvaceous, rhythm, curves(in GPT4) / vibrant, passionate, brown, culture, spicy, colorful, dance, curves(in GPT3.5) 열대 이미지를 그리는 비유, 다 동질화 시키고 성적인 이미지를 그려냄.

**Markedness, Essentialism and Othering**

다음은 Top words for singular group이다.

![Top words for singular groups](imgs/img7.png)

백인 GPT-3.5 persona는 good 같은 중립적이고 일상적인 단어들이 보이는 반면에 다른 그룹은 그렇지 않다.

비슷하게 남성 persona는 friendly, casually 같은 단어가 있으나 다른 그룹은 그렇지 않다.

ex) Middle-Eastern identity는 종교의 경건함과 엮여있음. 잔인한 광신도처럼 그려냄. 비인간화, 악마화하는 부분임.

앞에서 언급한 바와 같이 백인 기준으로 문화, 전통, 자긍심, 유산을 포함하는 단어를 그려낸다.

성별도 마찬가지.

중동, 아시아 persona에 대한 단어들은 동양 문화에 대한 비판과도 연관되어 있는데 서구 문화에 반해 "궁극적 타자"로서 damaging 묘사다. 

동양과 달리 서구의 문화를 부정확하고, 낭만적으로 표현한 것은 제국주의를 정당화하는 수단으로 쓰이기도 했다.

특정 인구 그룹의 이야기를 관찰해보면, 그들의 다양성을 보여주기보다 획일화시키는 것을 볼 수 있다.

essentialism이라고 할 수 있는데 이 그룹의 개인들은 인류로 보여지기 보다 고정된 본질적 특징들로 구성되어 있다고 여기는 것이다.

이는 소수 그룹에 대한 부정적 믿음을 갖게 해서 권력 차이의 유지가 정당하다고 여기게 해서 Othering을 불러오고, default 그룹과 완전 다른 벽을 쌓게 만든다.

**The Myth of Resilience**

![Occurence of resilience](imgs/img8.png)

백인이 아닌 교집합 persona에서 strength나 resilient 같은 단어들이 보임. 특히 흑인 여성 persona에서 자주 보임.

가난, 불평등, 그 외 널리 퍼져있는 사회적 이슈들을 극복한다는 뜻을 내포한다.

이 긍정적인 것처럼 보이는 글은 심리적 고통, 나쁜 건강, 자살 행동과 연관되어 있다.

strength와 resilience를 갖게 하는 구조를 바꾸려기보다 개인이 그러한 환경 속에서 이러한 자질을 가지길 바람으로써 이러한 환경들을 정상인 것처럼 인식되게 한다.

**Limitations of Anti-stereotyping**

![Top words for intersectional groups](imgs/img9.png)

Nonbinary 성을 가진 사람들에게 embrace, authentic을 여성들에게 independent, 흑인에게 leader, powerful이라는 단어들이 들어갔다.

bias를 줄이는 매커니즘의 결과물로 보이는데 역사적으로 부족했던 요소들을 집어넣은 것 같다. 와중에 unmarked 개인들은 저런 단어가 없다.

이런 단어들이 들어가게 되면 essentializing 이야기들이 오히려 강화되어 나빠질 것.

## 7. Downstream Applications: Stories

LLM 사용 시 자주 사용되는 기능은 무언가를 만들거나 창의적인 작문으로 유저들을 도와주는 기능이다.

그렇다면 Persona 뿐만 아니라 Story에서는 어떨까를 생각해 볼 수 있고, 15 "성별 x 인종"에 대해서 각 30개의 스토리를 만들었음.

프롬프트는 다음과 같음.

![Prompt for generating story](imgs/img10.png)

결과를 보면 unmarked group에 대해서는 그들을 명시적으로 표현하는 단어들 외에 중요한 단어들은 중립적이다. (town이나 shop)

그러나 marked group에 대해서는 아시아인에게 무술과 같은 단어들이 중요한 단어들에 속한다.

원숭이 등과 같이 명백한 부정적 단어는 아니지만 표현적 해악에 포함된다.

만들어진 예문을 보면 유색 인종 여성에 대해 전에 언급했던 "극복신화"의 형태를 볼 수 있다. 'dreams', 'determined', 'worked hard'.

따라서 스토리와 같은 downstream application에도 이런 유해한 패턴들이 존재함을 알 수 있다.

## 8. Recommendations

LLM에서 똑같은 라벨링을 했음에도 markedness랑 othering이 관측됨.

LLM이 점점 더 많이 사용되는 추세이기에 다음과 같은 지침을 따르는 것이 중요할 것.

**긍정적인 단어 stereotype 처리하기, 이야기 본질화하기**

긍정적인 단어 중에서도 stereotype을 포함해서 해를 끼치는 단어들이 있음.

따라서 부정적 단어를 긍정적으로 바꾸는 것은 stereotype 제거에 충분한 해답이 되지 못함.

현재는 Critical refusal로 stereotype을 포함한 스크립트 생성을 막고 있음.

연구한 LLM 중에서는 ChatGPT에서만 나타나고 있는 형태.

하지만 미래에는 현재의 Critical refusal을 대체할 수 있는 방법이 나올 수 있을 것임.

모델은 인구 집단의 persona를 만드는 것이 stereotype이나 이야기를 본질화하는 것에 의존하지 않을 수 없다는 것을 인식해야 함.

**교집합 렌즈**

Identity가 여러 조합으로 이루어져 있을 때, 그들을 나누는 축 뿐만 아니라 그 조합의 특성도 분석해야 한다.

Asian Women을 예시로 들자면 Asian으로 분석, Women으로 분석하는 것 외에도 Asian Women으로 분석하는 것이 필요하다.

**Bias 완화 방법의 투명성**

OpenAI의 bias 완화 방법은 알려져 있지 않지만 최근 stereotype들은 덜 부정적이고 자주 나오는 행태를 보여준다.

bias 평가 방법은 보호받는 집단에 대한 폄하가 일어났을 때를 가정하는데, 이 방법은 긍정적인 stereotype들을 간과한다.

어떻게 bias가 완화되는지, 어떻게 bias를 막는지 등의 방법에 대한 정보 공개가 방법론의 발전을 불러올 것이다.

## 9. Limitations

완전하고 체계적으로 각 인구 집단의 stereotype이나 bias를 조사하는 것보다도 자주 쓰이게 될 LLM이 퍼트릴 수 있는 stereotype 패턴 제공에 집중했음. 하지만 OpenAI API를 통한 모델들만 측정했다는 것에서 한계가 있음.

Stereotype은 문화마다 다름. Marked Personas 모델 자체는 다른 문맥에서도 적용될 수 있지만 논문에서의 lexicon이나 정성적 분석은 미국식 stereotype에만 집중했고, 영어에서만 이루어졌음. 아마 더 다양한 집단에서 진행해 봐야 함.

Unsupervised 학습을 생각해보면 어떤 정체성이 unmarked/default인지도 unsupervised 방법으로 찾아야 하는데 현재는 어떤 정체성이 marked 혹은 unmarked인지 다 정의해주고 있음.

논문의 잠재적 위협으로는 인구 집단들에 대한 여러 나쁜 영향들을 연구하면서 그런 사회적 카테고리들을 구체화해버린다는 것이 있다.
또, OpenAI 모델들에 집중해서 연구했기에 그 모델들이 더 지배적으로 사용되는 것에 기여했을지도 모른다.
