# 23.06.01



- Be careful about IP right
- 10:30 am 으로 미팅 이동 -> 11:30
- Last semester SAMI was used to make team among students. We should utilize the data 



# 23.06.06

- SAMI history

처음 시작은 2.5 hours 개발만에 끝났었다. 



passenger condition?

NLP take token from text and compare with csv file 

Cdv file for location, hobbies... we have

Moved a lot -> rewrote the code



Changed to chatGPT



- 주의

stay informed, never surprise him

work : 1:1 meeting a week, 15min update, 더 많이 걸릴테면 30분정도



- 할일 : 

1. monday 30min calendar 9:00 am ET calendar 보내기





Reh 한테 나 알려주라고 할것. 



that's 

project for semester. 

there's no log file. 

we need to create log file. python logger

script that attracts all SAMI 



SAMI : 3.5 parts

NLP(chatGPT)

knowledge based (neo4j)

interacting with API...



response generation & knowledge based - how Agent attract 

each module has primary owner and backup



지금은 response generation & knowledge based 시작 

그 후 머신러닝으로 옮기기 



Rea & mustafa 



going slow is good thing



github issues 써야함 아무도 말을 안들음





# 23.06.07

- theory of mind
- TMK model
- metacognition group



# 23.06.12 Sandeep

personality challenging

1. reason why chatgpt works. it's black box. only fine tunning score. we don't know what's behind etc...
2. we don't know the basis of confidence. 

-> we cannot validate the result. 

Chelsea 66 students 

I need to understand the work what we have done. 

Chris surprised him. get familiar with his workm read about personality trait, Chelsea's data for common understanding. This week is to catch up his work. Ada etc.



another problem : what do we do with personality trait. How do I match students with personalities? From literature. We need to get to a point where it's promising. 희망이 없어보이면 멈춰야 함. getting conceptual work. 

A-learn where we are now B-how to match personalities 

Chris mentors me and next week I'm equal. 

Chris is smart but he's awful communicator. 

Has habit of surprise Sandeep. 

With me, I act as a anchor to communicate with Sandeep. 



Is there market? Can we clear market? => at some point he wants me to get to this point.



# 23.06.14 

- Pppp 
- meta cognition part?



# 23.06.18 Chris Personality

*my questions*

1. ppt p7, what are the numbers? what do they mean?
2. why did you choose big 5 instead of MBTI? because it's most widely used?
3. we may need to do self-report questionnaires to get the big 5 score => Chelsea's data(?)



*Previous slide*

- jill watson tool - big 5 personality insight - what Ashok initially thought. but it's not available anymore

- Ashok didn't like that we need to train ourselves (fine tunning) - top down paper code
- Santino API - didn't work well
- did well - chat GPT with same data(essay) - with good correlation
- so now started with Chelsea's dataset. instead of high, low value, it has 1 to 5 scales of scores. Chelsea's data is very representative. but it's too small. Only 69 samples.
- orange bar : Chelsea's dataset. 7p : Distribution - predicted and acutal are similar.
- then if we see each trait, chatGPT is plausible, not always 4 except Neuroticism. it's almost always 2. same with extraversion. it's wrong a lot. 
- P13: mse for different methods. ChatGPT does much better than all different kinds of random. 
- P14: started to add confidence of low/high. bc it's language model. it's not calculating anything. 
- confidence is black box. it's whatever chatGPT is deciding. chatGPT say explanation with points in the paragraph where he referred. 
- high conf is on the line, low conf is further out. it's separating.. low conf says there's more sparse. how we're gonna get this trait. 
- extraversion is important to get engaged - very bad with chatGPT. only 7 high conf
- p10 also not indicative
- 그래서 fine tunning을 해서 extraversion trait 높이려는 것
- high conf만 쓴다면 괜찮. 



- original idea: clustering. Helen is working on sth similar. 



*last presentation*

- Helen's work inline with clustering with RQ2. Derive preference, who they prefer to engaged? look at what they've posted -> predict how interested would be
- she's looking at preference from student A on student B based on posts. look at their interactions on forum, calculating preference
- P6: preference between traits. how we're gonna match students. figure what literature says and how we're gonna implement that to the code. 
- Ashok : literature은 이러니까 이렇게 match 하자! 빨리빨리! 
- fall sem 까지 result가 있기를 바람. 
- 해야할 것 : what this rule should be!
- p5: from one of the papers with multiple charts but didnt' dig in much. 
- P6: from one of the papers.
- p4~6 : his initial thoughts. we can build on it. 



# 23.06.26 with Sandeep

- personality is second order impact

- personalizing SAMI was important 

- To do in Wednesday

1. talk about past week work, summarize one paper that is useful and why, summarize my thoughts. build a case around. 

   he wants me to be Intellectual horsepower

- talk with Psychology student about personalities. 

- keep them informed that it's not a easy job

- In the Wed meeting:

1. signaling to Ashok that I'm ready. I'm arrived.
2. updating Ashok what i've done
3. giving him check that it's not easy. we're in a very soft ground. we don't know what we're doing



# 23.06.28 

- we always need research hypothesis, then there is data as the mean to validate it

- feedback record : https://gtvault-my.sharepoint.com/:v:/g/personal/lkim93_gatech_edu/Earh_GCWMxdMofWsc37nKgEBhmZYZtc-dMANyBpA6aLkzg

- Ppt feedback
  - 4 entity, a lot of sensitive, 500 hobbies. uniqueness of. Are they very unique? if they are not unique, how do we find matches?
  - what is matching base? literaturized theme? 
  - revisit full features
  - high/low 를 찾지 못했다 
  - all conclusions were that similar on traits were good matches. We'll be able to see 
  - trait 3개부터 시작해서 그 안에서 조금씩 넓혀가자
  - Research question: how do we personalize SAMI? could personality be factor there? 
  - research hypo: 
- what would it take how much effort 
- request:
- personality can be useful for personalization. We can adjust SAMI's responses according to students' personality.
- here, research question could be, based on perceived personality of students, data we collected, sami가 personalization이 되지 않아서 학생들이 덜 참여한걸수도 있다.
- Is personality right 





**:star: Ashok's request**

- If personality is not the basis of match making, what is? It has to be in the literature.
  - review of matchmaking and just go explore and see what you find.
  - Figure out what is important when it comes to relationship formation. Obviously friendship is our focus but I would imagine that resources focused on romantic relationship formation may be useful as well. Look at what companies like [Match.com](http://match.com/) are considering when they make their matches. Like you had suggested, are demographic attributes cited as being important? Age, occupation, education level, common goals, and so on. 
- if personality is basis of personalization?
  - So before you were looking at personality as a basis for matchmaking, he wants you to instead broaden that to see what is important for matchmaking and then your focus on personality would shift from how does it affect friendship formation to "Does it have any effect on how you interact with someone?" So we aren't totally off the personality hook but I think this gives you more room to explore and go where your research takes you.
  - Ashok wants SAMI to respond in a way that takes into consideration SAMI's understanding of the person's personality (if the literature confirms his hypothesis that perceived personality does have an effect on how we communicate with a person). For example SAMI perceives a student as highly extraverted and it comes back and is like "Hi! It's great to meet you!" and if SAMI thinks you are an introvert it might just say "Hey..." haha or something like that.



# 23.07.5

chris will change prompt to ask chatGPT 

consider shared identity based on ~~~ to comp with introduction 



We're not using personality for personalization, not for the match

chatGPT makes the match but issue is if chatGPT is scalable to do 500 introduction? 



- Chris & Sandeep

not sure we're considering personality in match

we can't use whole intro post

pass json to chatGPT

chatGPT extracts json -> personality substraction -> personalized SAMI's answer

match making은 chatGPT가 하지 않음. 

simple project. work or not work. 

Personalization 있는 버전과 없는 버전 compare 해보기. 어떤 response가 more engaging 인지 파악. let's deploy this version in fall semester.



- RHEA's idea : chatGPT makes good post -> 'click' 을 클릭했을 때 추천된 상대에게 건네는 인삿말을 자동으로 생성하여 reply 하도록



# 23.07.6 Sandeep

- Byte size project 

- Chris - with personality

- SAMI has already structed entity

- you'll pass those entity in some form to student and ask chatGPT from student what does SAMI know about student and let them know how can connect. chatGPT 가 student 에 대해서 배우고 그에 맞는 response를 generate 하도록. 

- send any context and ask chatGPT a question. -> to learn openAI call. 

- take 1 intro post(hard-code) -> send that to chatGPT, question summarize entity or give some questions to chatGPT, play with prompt

- Once done that, we can do this first and then play with the feedback modification. 

- exaple task: summarize this post and introduce this person in autiance. 

- ask public questions in slack, not via DM

- change the SAMI's feedback: goal for this semester - for the reflection report 

- make chatGPT's feedback more spontaneous and natural 

