SAMI project - personality match related

[toc]



# Papers

1. **Bottom-Up and Top-Down: Predicting Personality with Psycholinguistic and Language Model Features**

- use online data on human behavior and preferences (i.e., digital footprints) to automatically predict individuals’ levels of personality traits
- big 5 : Openness to Experience, Conscientiousness, Agreeableness, Extraversion, and Neuroticism or positively keyed, emotional stability
- language model-based approaches far outperform the traditional closed vocab ones for personality prediction
- larger language model does not always result in higher performance.
- the results of our interpretable machine learning analysis partially align with past, associative findings from personality psychology and underline the expressiveness of language use for individual differences



2. **Predicting Personality from Social Media Text - Jennifer Golbeck**

- use LIWC and its tool Receptiviti
  - Receptitiviti API : estimates of Bif Five personality traits based on a text sample
- 4 social media posts datasets from facebook, twitter
- predict big 5 personality with Receptiviti, samples' ground truth big 5 personality was previously measured
- error had a fairly wide range across the five personality traits



3. **Predicting Personality with Social Media**

- In this paper, we have shown that a users’ Big Five person- ality traits can be predicted from the public information they share on Facebook.

- analysing correlation between personality inventory(ground truth) and big 5 personality features using facebook data
- predicting personality with dot-producting the feature vector, train two ML also (m5sup/rules and Gaussian Processes)
- considered two structural features - number of friends and network density
- 연구 활용 방안 : With the ability to in- fer a user’s personality, social media websites, e-commerce retailers, and even ad servers can be tailored to reflect the user’s personality traits and present information such that users will be most receptive to it. 



4. :star: **On friendship development and the big five personality traits**

- Our review suggests that **agreeableness** has the most consistent effects on both roman- tic relationships and friendships, followed by **neuroticism**. Extraver- sion, conscientiousness, and openness to experience have all been shown to influence relationship development, but their effects are inconsistent. 
- actor : who is more likely to initiate and end friendships, partner : who is more likely to be the target of friendship initiation and termination
- worth to read from reference : the role of personality traits for friendship development (e.g., Wilson, Harris, & Vazire, 2015)
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
- Agreeableness(상냥함)
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
  - Dyadic effects
    - there is some evidence that couples that share similar levels of neuroticism and negative emotionality are happier together than mismatched couples 
  - Summary
    - The research conducted so far suggests that neuroticism has little effect on friendship formation, but is problematic for friendships once they have been formed. People high on neuroticism seem to preemptively worry about their ability to have successful relationships, and often wind up behaving in ways that make relationships more fraught.
- Conscientiousness(양심)
  - Although conscientiousness has clear interpersonal implications (e.g., following through on commitments to others), it is less directly related to social behavior than extraversion and agreeableness
  - Based on these findings, the effects of conscientiousness should be more pronounced in the later stages of friendship development than in friendship formation. 
- Openness
  - That said, individuals tend to be friends with people who are similarly open (Lönnqvist & Itkonen, 2016; Selfhout et al., 2010). Given that openness is associated with values and interests (Dollinger, Leong, & Ulicni, 1996), similarity in openness could be indicative of other commonalities.
  - Compared to the other Big Five traits, openness is likely to be less related to actors' and partners' friendship satisfaction, but it may be related to other outcomes, such as one's position in social networks, or the variety of one's friends. 



5. **Promises and perils of inferring personality on github**

- how to infer personality:
  1. questionnaire
  2. Psycholinguistic test (from text to a model to generate personality scores)
- research question: Do psycholinguistic tests (trained on different text source(s)) reli- ably infer developer personality from SE communications data?
- We studied the Per- sonality Insights tool developed by IBM Watson2 and two models from academia: Golbeck et al. [23] designed for small text sizes such as Twitter posts and Yarkoni et al



6. **Linguistic Styles: Language Use as an Individual Difference**



7.  **the role of personality traits for friendship development**

- characteristics that lead to attraction
  - hypothesis 1 : people select friends who are similar to themselves
    - 1 way : consensual validation of one's attitudes and beliefs, which is provided by others who hold similar views
    - 2 way : participating in enjoyable activities with others who have similar interests
    - adults' choices of friends are based on similarity in several demographic characteristics or social attributes
    - level of attraction is directly related to the proportion of similar attitudes shared by two individuals (Byrne & Grifftt, 1973)
    - Similarities in sex, age, and race appear consistently in children's and adolescents' friendship (Hartup, 1983, 1993)
    - Degree to which friends agree with, and adopt, each other's social perceptions may determine whether the friendship is maintained
  - hypothesis 2 : people select friends who have desirable attributes
    - they discovered that liking a fictitious stranger is unrelated to similarity on several personality dimensions. rather, the important criterion isn the similarity between the stranger's personality and the subject's profile of an ideal personality.(Wetzel and Insko)
    - Ideal personality characteristics may be important when selecting friends because individuals strive to learn from, or emulate, a friend rather simply have their own personalities validated.



# General

- There are a few different scoring systems

  - Big 5 inventory questionnaire : 

    - *Instruction 5*: To work out if you are high, average, or low in each factor, compare the score of each factor (column X) to your average score (row B). For example, if your factor I extraversion score was 28 and your average score was 32, then you are average in extraversion.

      *Instruction 6*: Write in the column labeled “Y. Your Big Five Scale” if your score for each of the factors was H (high), A (average), or L (low).



# Thoughts

- What if we make priorities among traits when matching? Extraversion-agreeableness-neuroticism order. The rest two don't have big relationship with friendship.
- put importance on friendship formation rather than friendship maintanance or other phases of friendship.
- make a checklist of big 5 traits that students can choose binary traints. ex) introvert vs extrovert / agreeable / disagreeable etc. Seems more reasonable to classify students rather than receive the text explanation.
- Does personality really matter when they form friendship with online students? Aren't they more interested in someone who has potential to benefit them in career-wise? Or people with common situation as theirs?