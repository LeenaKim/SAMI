SAMI project - personality match related



# Papers

1. Bottom-Up and Top-Down: Predicting Personality with Psycholinguistic and Language Model Features

- use online data on human behavior and preferences (i.e., digital footprints) to automatically predict individuals’ levels of personality traits
- big 5 : Openness to Experience, Conscientiousness, Agreeableness, Extraversion, and Neuroticism or positively keyed, emotional stability
- language model-based approaches far outperform the traditional closed vocab ones for personality prediction
- larger language model does not always result in higher performance.
- the results of our interpretable machine learning analysis partially align with past, associative findings from personality psychology and underline the expressiveness of language use for individual differences

2. Predicting Personality from Social Media Text - Jennifer Golbeck

- use LIWC and its tool Receptiviti
  - Receptitiviti API : estimates of Bif Five personality traits based on a text sample
- 4 social media posts datasets from facebook, twitter
- predict big 5 personality with Receptiviti, samples' ground truth big 5 personality was previously measured
- error had a fairly wide range across the five personality traits

3. Predicting Personality with Social Media

- In this paper, we have shown that a users’ Big Five person- ality traits can be predicted from the public information they share on Facebook.

- analysing correlation between personality inventory(ground truth) and big 5 personality features using facebook data
- predicting personality with dot-producting the feature vector, train two ML also (m5sup/rules and Gaussian Processes)
- considered two structural features - number of friends and network density
- 연구 활용 방안 : With the ability to in- fer a user’s personality, social media websites, e-commerce retailers, and even ad servers can be tailored to reflect the user’s personality traits and present information such that users will be most receptive to it. 

4. On friendship development and the big five personality traits

- Our review suggests that **agreeableness** has the most consistent effects on both roman- tic relationships and friendships, followed by **neuroticism**. Extraver- sion, conscientiousness, and openness to experience have all been shown to influence relationship development, but their effects are inconsistent. 
- actor : who is more likely to initiate and end friendships, partner : who is more likely to be the target of friendship initiation and termination
- 참고문헌중 읽어볼만한 것 : the role of personality traits for friendship development (e.g., Wilson, Harris, & Vazire, 2015)
- paper focuses on two stages of friendship devel- opment: formation and maintenance.
- Extraversion: willing to make more friends
  - Actor effects
    - Extraverts' positive experiences with others, coupled with the sociability that characterizes extraversion, could drive them to approach others more and to be more willing to engage with strangers than introverts.
  - Partner effects
    - In short, extraverts seem to be liked more at first, but they are not necessarily more prone to elicit liking after the first impression.
  - dyadic effects
    - Similarity in extraversion can impact friendship formation. People, particularly introverts, tend to like others who match their level of extraversion 
  - summary
    - it is easy to imagine how friendships could look very different depending on the combination of extraversion levels (i.e., high‐high vs. high‐low vs. low‐low).
    - Nelson, Thorne, and Shapiro (2011) began studying the dynamics of matched versus mismatched friendships, but there is still more work to be done on this topic.
- Agreeableness
  - Actor effects
    - Surprisingly, however, agreeableness seems to be less important than extraversion in selecting new friends.
    - will use their interpersonal skills to make the interactions they happen to be in go smoothly, but they may not actively seek out new friendships.
  - Partner effects
    - Agreeableness does not immediately attract others, but later becomes a valuable trait in potential friends.
    - However, after interacting with others, agreeable people are better liked than disagreeable people (Cuperman & Ickes, 2009; Wortman & Wood, 2011)
    - In short, agreeable people are popular. 
  - Dyadic effects
    - When at least one of the two interaction partners is high on agreeableness, both are more likely to feel comfortable in the interaction, and independent coders observe more smiles and laughter in those interactions
    - However, if two highly disagreeable people are put together, the interaction does not go as well
  - summary
    - However, compatibility on agreeableness is not necessary for a successful interaction—one agreeable person in an interaction is enough for things to go smoothly.
- Neuroticism/emotional stability
  - Actor effects
    - Emotional stability (i.e., low neuroticism) is not associated with liking strangers more at zero acquaintance 
  - Partner effects
    - Neuroticism also has little to do with how much people are liked by new acquaintances
    - People high on neuroticism do not expect to be liked at zero acquaintance, (Back et al.). Similarly, they feel less comfortable and more self‐conscious interacting with strangers than do people low on neuroticism. 
- matching시 trait들중 우선순위를 정하는건 어떨까? agreeableness 1위
- 매칭시 friendship maintanance 보단 formation에 중점을 두는게 어떨까?

4. 