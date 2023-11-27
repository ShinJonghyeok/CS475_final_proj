Replication Presentation Script

# Introduction

안녕하십니까 여러분. 저희는 Marked Personas에 대해 발표할 Team 2입니다.

본격적으로 replication을 이야기 하기 전에 introduction에서 몇 가지를 소개하고자 합니다.

저희 논문의 문제는 "여러 사람들에게 정보를 제공하고 점점 널리 쓰이는 LLM이 stereotype이나 social bias를 포함해서 사람들에게 해를 끼친다"는 점에서 출발합니다.

이 문제를 해결하기 위해서 stereotype을 측정하는 기술들이 필요합니다.

현재까지 알려진 방법들은 lexicon과 같이 stereotypical 관계를 측정하는 인위적인 템플릿이나 사람들에 의해 쓰여진 문장 데이터셋에 의존합니다. 그들은 일부 stereotypical하거나 bias를 내포하는 단어들을 솎아냅니다.

하지만 이런 방법들은 한계를 가집니다. stereotype인지 아닌지를 지도하기 위한 데이터가 필요하고 감정 긍정(sentiment-positive)적으로 표현된 stereotype이나 타자화(othering)와 같은 은근한 stereotype들을 잡아내지 못한다는 단점이 있습니다.

여기서 우리는 unsupervised, lexicon-free 방법인 Marked Personas라는 모델을 소개합니다.

Marked Personas는 feature words와 markedness를 사용합니다.

feature words는 corpus에서 두 집단이 사용한 단어들 중 한 쪽에서만 자주 사용되는 단어들을 의미합니다.

예를 들어 민주당, 공화당 집단이 있을 때 right라는 단어는 공화당에서, kill이라는 단어는 민주당에서 자주 사용되었는데 이렇게 특정 집단에서 자주 사용된 단어들이 모여 feature words를 구성합니다.

이어 markedness라는 개념을 설명하겠습니다. The concept which articulates the linguistic and social differences between the unmarked default group and marked groups that differ from the default. 예를 들어 백인이나 남성 같이 사회적 주류가 unmarked, 비주류가 marked라고 표현되는 것이 markedness입니다. Marked Personas에서는 전체 corpus에서 각 인구 집단의 feature map을 뽑아냅니다.

Markedness를 기반으로 해 Marked Personas 연구를 진행하기 위해서는 두 가지가 필요합니다.

첫째로, 다음과 같은 프롬프트를 이용해서 특정 demographic group의 persona를 GPT 등의 생성 AI로부터 얻어냅니다.

둘째로, Marked Words 프레임에서 특정 demographic group의 persona set과 그 group의 unmarked identity를 비교해 통계적으로 중요한 단어들을 뽑아냅니다.

통계적으로 중요한 단어들은 Fightin' Words의 Informative Dirichlet prior를 이용한 log odds ratio를 통해 얻어낸 값들 중 z-score가 1.96보다 큰 단어들이 될 것입니다.

우리가 사용하는 데이터셋은 GPT4, GPT3.5가 각 인종, 성별, (인종, 성별) prompt에 대해서 만들어 내는 persona들입니다.

# Replication Results

-	어떻게 replication 시도했는가?

-	세팅, replication 방법 소개

-	어떤 문제가 있었고 어떻게 해결했는가?

-	현재까지 나온 결과

결과는 논문에서 나왔던 결과와 동일하게 나왔습니다.

첫 번째로 human-written data와 GPT-3.5가 만들어 낸 persona의 stereotype 비교입니다.

다음은 평균적으로 몇 퍼센트의 단어가 백인, 흑인 stereotype lexicon에 포함되어 있는지 측정해 나타낸 그래프입니다.

아까 언급했듯이 실제로 측정하지 못한 GPT-4를 제외하면 논문과 같은 값이 나와 있습니다.

Lexicon based 측정에 따르면 GPT들이 생성해낸 persona가 human-written personas보다 더 많은 stereotype을 가지고 있는 것을 확인할 수 있었습니다.

그리고 특징적으로 GPT-3.5에서 백인 persona에서 black stereotypes가 오히려 더 많이 관찰되었습니다. 좀 이상합니다.

그래프의 값을 봤을 때 Black persona에서 stereotype은 white persona에서 white stereotype에 비해 지나치게 낮은 값을 가지고 있습니다.
이는 lexicon으로 잡아내지 못한 black stereotype이 더 있고 이 방법만으로는 찾아낼 수 없었다고 해석할 수 있습니다.

다음은 모델 별로 생성한 흑인 persona에서 몇 퍼센트의 persona가 특정 단어를 포함했는지를 나타내는 그래프입니다.

여러분이 관찰할 수 있듯이 사람이 쓴 persona가 좀 더 다양한 단어들을 포함하고 있음을 관찰할 수 있습니다.

이 두 figure에서 낼 수 있는 결론은 lexicon based만으로는 stereotype 측정이 부족할 수 있다는 것입니다.

다음은 아까 소개했던 feature words를 구하는 방법으로 추출해낸 persona별 significant words 중 top words를 나타낸 표입니다.

(적을지 말지 모르겠는데 : 논문에서와 동일한 단어 set이 나와서 논문의 표를 빌려왔습니다.)

Black에서 strength, Asian에서 heritage, MiddleEast에서 headscarf 등 stereotype을 나타내는 단어들을 관찰할 수 있습니다.

stereotype들이 잘 나타나있습니다. 그런데 이 단어들을 보다 보면 부정적인 단어는 잘 보이지 않습니다. headscarf나 heritage는 부정적이지 않으니까요. 실제로 NLTK의 패키지를 사용해 감정 분석을 해보면 이들은 긍정적인 단어에 주로 속합니다.

우리는 아마 이것을 OpenAI의 bias 약화 기능에 의한 것이라고 생각합니다.

하지만 "와 이 성별인데 이 정도까지 했다고? 잘 했어" 등의 부적절한 칭찬 등은 분명 해롭습니다. 이런 단어들 또한 표에서 보시다시피 잘 잡아낸 것을 관찰할 수 있습니다.

외모와 관련된 용어들을 보면 백인 집단 대해서는 객관적인 설명을 쓰는 데 반해 marked group에서는 colorful, curvy 같이 백인 기준에서 비교했을 때 의미 있는 단어들이 보임. 마찬가지로 추출해 내야할 단어인데 잘 추출된 것을 볼 수 있다.

그리고 headscarf, heritage 같은 단어는 백인에게는 없으나 marked group에서 나온 단어들인데 서구 문화권 밖의 사람들을 사람이 아닌 본질들의 집합체로 보는 효과를 가져옵니다. 예를 들어 ME identity를 자세히 살펴보면 종교적으로 연관된 단어들이 많이 보이는데 외모와 마찬가지로 백인 기준에서 다른 점들을 persona에 포함시키는 것을 볼 수 있습니다.

마지막으로 combination된 persona에서 combination 원형의 persona들에서 나오지 않던 단어들을 볼 수 있는데 resilience라는 단어를 관찰할 수 있었습니다. '흑인 여성이라면 자고로 고난과 역경을 이겨내고 회복해야지!'라는 위험한 생각을 바탕으로 한 단어이기 때문에 이것 또한 축출되어야 하는 단어입니다.



# Plan
-	어떻게 improve 할건가? (Replication 결과 바탕)
