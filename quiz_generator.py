import random

def generate_quiz(topic, num):
    sample_questions = {
        "Python": [
            {
                "question": "What is the keyword used to define a function in Python?",
                "options": ["func", "define", "def", "function"],
                "answer": "def"
            },
            {
                "question": "Which data type stores True or False values?",
                "options": ["int", "bool", "float", "str"],
                "answer": "bool"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "#", "/*", "--"],
                "answer": "#"
            }
        ],
        "Java": [
            {
                "question": "Who developed Java?",
                "options": ["Microsoft", "Sun Microsystems", "Google", "Apple"],
                "answer": "Sun Microsystems"
            },
            {
                "question": "Which keyword creates an object?",
                "options": ["create", "new", "object", "class"],
                "answer": "new"
            }
        ],
        "AI": [
            {
                "question": "AI stands for?",
                "options": ["Artificial Intelligence", "Automatic Internet", "Advanced Interface", "Applied Information"],
                "answer": "Artificial Intelligence"
            },
            {
                "question": "Which language is popular for AI?",
                "options": ["Python", "HTML", "CSS", "PHP"],
                "answer": "Python"
            }
        ]
    }

    if topic in sample_questions:
        questions = sample_questions[topic]
    else:
        questions = [
            {
                "question": f"What do you know about {topic}?",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "Option A"
            }
        ]

    return random.sample(questions, min(num, len(questions)))