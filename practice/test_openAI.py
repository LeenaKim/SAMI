import openai
import json

class TestOpenAI():

    def __init__(self, openAI_api_key):
        openai.api_key = openAI_api_key
    """
    system : set the behavior of the assistant (optional)
    user : provide requests or comments for the assistant to respond to
    Because the models have no memory of past requests,
    all relevant information must be supplied as part of the conversation history in each request
    """
    def dummyTest1(self):
        dummy_intro = "Hi all, I’m Leena Kim from Seoul, South Korea. I studied Sociology for my Bachelors and I’m taking OMSCS course pursuing ML specialization. I work full time as a software developer at a bank in Korea and I’m in the mobile loan team. I’ve been to the countries in South America and South East Asia. My favorite country is Colombia where I did my exchange semester, and an unique country that I lived for a year is Timor-Leste, a tiny island between Indonesia and Australia. When I’m not working or studying, I love to go to travel. Last week I went to Chiang Mai, Thailand to spend my spring vacation. I’ve taken AI4R, ML4T, ML, Network Science, DL and AIES so far."

        dummy_entity_json = '''
        {
            "post_id": 3661734,
            "thread_id": 1622144,
            "platform": "ED",
            "process": "Introduction",
            "user": {
                "official_name": "Patrick Westervelt",
                "name": "Patrick Westervelt",
                "id": 121161,
                "email": "unknown"
            },
            "entities": [
                {
                    "labels": [
                        "GPE",
                        "City"
                    ],
                    "properties": {
                        "name": "Atlanta"
                    },
                    "relationship": {
                        "type": "LOCATED_IN",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "GPE",
                        "State"
                    ],
                    "properties": {
                        "name": "Georgia"
                    },
                    "relationship": {
                        "type": "LOCATED_IN",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "GPE",
                        "Country"
                    ],
                    "properties": {
                        "name": "United States"
                    },
                    "relationship": {
                        "type": "LOCATED_IN",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Timezone"
                    ],
                    "properties": {
                        "name": "-05:00"
                    },
                    "relationship": {
                        "type": "AT_TIME",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "GPE",
                        "City"
                    ],
                    "properties": {
                        "name": "New Jersey"
                    },
                    "relationship": {
                        "type": "MENTIONED_LOCATION",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Hobby"
                    ],
                    "properties": {
                        "name": "cooking"
                    },
                    "relationship": {
                        "type": "INTERESTED_IN",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Hobby"
                    ],
                    "properties": {
                        "name": "hiking"
                    },
                    "relationship": {
                        "type": "INTERESTED_IN",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Hobby"
                    ],
                    "properties": {
                        "name": "board/tabletop games"
                    },
                    "relationship": {
                        "type": "INTERESTED_IN",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Hobby"
                    ],
                    "properties": {
                        "name": "video gaming"
                    },
                    "relationship": {
                        "type": "INTERESTED_IN",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Course"
                    ],
                    "properties": {
                        "name": "CS 7637: Knowledge-Based Artificial Intelligence"
                    },
                    "relationship": {
                        "type": "MENTIONED_COURSE",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Course"
                    ],
                    "properties": {
                        "name": "CS 6750: Human-Computer Interaction"
                    },
                    "relationship": {
                        "type": "MENTIONED_COURSE",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Course"
                    ],
                    "properties": {
                        "name": "CS 6601: Artificial Intelligence"
                    },
                    "relationship": {
                        "type": "MENTIONED_COURSE",
                        "properties": {}
                    }
                },
                {
                    "labels": [
                        "Course"
                    ],
                    "properties": {
                        "name": "CS 6460: Educational Technology"
                    },
                    "relationship": {
                        "type": "MENTIONED_COURSE",
                        "properties": {}
                    }
                }
            ]
        }
        '''
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a salutation specialist employed by Georgia Institute of Technology. "
                            "Your job is to write attractive, informal, friendly salutation sentences "
                            "to bring readers' attention and make them continue using our friend-match service. "
                            "Readers are the students in the Online Master of Science in "
                            "Computer Science program who gave their introduction post with their information. "},
                {"role": "assistant",
                 "content": "The student may not reside in Georiga or even the United States. "
                            "We don't know the student is currently "
                            "taking the courses mentioned in the student or have completed."
                            "List of matched classmates will be appeared after this salutation."},
                {"role": "user",
                 "content": "Step 1: Read the student's properties json extracted from their introduction posts in triple backticks. "
                            "Use only the first name in \'name\' property and utilize \'entities\' property to make more "
                            "personalized salutation."
                            "```" + dummy_entity_json + "``` "
                            "Step 2: Write one short salutation sentences with provided students' information. "}

            ]
        )
        return response