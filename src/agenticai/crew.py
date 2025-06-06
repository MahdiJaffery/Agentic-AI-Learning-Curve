from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

import pandas as pd

@CrewBase
class Siriil():
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def lead_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['lead_agent'],
            verbose = True
        )
    
    @agent
    def accounting_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['accounting_agent'],
            verbose = True
        )
    
    @agent
    def analyst_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['analyst_agent'],
            verbose = True
        )
    
    @agent
    def tax_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['tax_agent'],
            verbose = True
        )
    
    @agent
    def reviewer_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['reviewer_agent'],
            verbose = True
        )

    #   Adding Tasks    
    @task
    def accounting_task(self) -> Task:
        return Task(
            config = self.tasks_config['accounting_task'],
            output_file = 'InitialReport.md'
        )
    
    @task
    def analyst_task(self) -> Task:
        return Task(
            config = self.tasks_config['analyst_task'],
            output_file = 'AnalysisFile.md'
        )
    
    @task
    def tax_task(self) -> Task:
        return Task(
            config = self.tasks_config['tax_task'],
            output_file = 'TaxReview.md'
        )
    
    @task 
    def review_task(self) -> Task:
        return Task(
            config = self.tasks_config['review_task'],
            output_file = 'ReviewFile.md'
        )

    @task
    def lead_task(self) -> Task:
        return Task(
            config = self.tasks_config['lead_task'],
            output_file = 'FinalReport.md'
        )

    #   Making the Crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
    

