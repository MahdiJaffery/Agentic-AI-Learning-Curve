#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from siriil.crew import Siriil

import pandas as pd

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputType = 'N'

    while inputType not in ['1', '2']:
        inputType = str(input("Types:\n1.\tTopic\n2.\tFile\nEnter Choice: "))
        if inputType not in ['1', '2']:
            print("Invalid Selection!\n")

    topic, filename = '', ''

    if(inputType == '2'):
        filename = str(input("Enter File Name: "))
        filename += ".xlsx"
        df = pd.read_excel(filename, sheet_name="TDSheet")
    else:
        topic = str(input("Enter Topic: "))
        
    inputs = {
        'topic': f'{topic}' if topic is not None else f'{df}',
        'name': 'Lead Analyst',
        'company_name': 'SiRiiL',
        'current_year': str(datetime.now().year),
        # 'current_date': str(datetime.now())
    }
    
    try:
        Siriil().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Siriil().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Siriil().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Siriil().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
