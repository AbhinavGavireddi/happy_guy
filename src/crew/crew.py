"""
Core module implementing the CrewAI workflow for generating personalized messages.
This module defines the agents and tasks required for the message generation pipeline.
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crew import OutputFormat
from langchain_openai import ChatOpenAI

# Initialize search and scraping tools
search_tool = SerperDevTool(n_results=5)
scrape_tool = ScrapeWebsiteTool()
llm = ChatOpenAI(temperature=0.3, model = 'gpt-4o-mini-2024-07-18')

@CrewBase
class HappyCrew:
    """
    Main crew class that orchestrates the message generation workflow.
    Uses YAML configuration files for agent and task definitions.
    """
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def data_collector(self) -> Agent:
        """
        Creates an agent responsible for collecting user data and information.
        
        Returns:
            Agent: Configured data collection agent with search capabilities
        """
        return Agent(
            config=self.agents_config['data_collector'],
            tools=[search_tool],
            verbose=True,
            allow_delegation=False,
            memory=True,
            llm=llm
            
        )

    @agent
    def content_creator(self) -> Agent:
        """
        Creates an agent responsible for generating the initial message content.
        
        Returns:
            Agent: Configured content creation agent
        """
        return Agent(
            config=self.agents_config['content_creator'],
            verbose=True,
            allow_delegation=False,
            memory=True,
            llm=llm
        )
    
    @agent
    def tone_expert(self) -> Agent:
        """
        Creates an agent responsible for refining message tone and style.
        
        Returns:
            Agent: Configured tone adjustment agent
        """
        return Agent(
            config=self.agents_config['tone_expert'],
            verbose=True,
            allow_delegation=False,
            memory=True,
            llm=llm
        )

    @agent
    def manager_agent(self) -> Agent:
        """
        Creates an agent responsible for managing the workflow.
        
        Returns:
            Agent: Configured manager agent
        """
        return Agent(
            config=self.agents_config['manager_agent'],
            verbose=True,
            allow_delegation=True,
            memory=True,
            llm=llm
        )

    @task
    def data_collection_task(self) -> Task:
        """
        Defines the task for collecting user data and information.
        
        Returns:
            Task: Configured data collection task
        """
        return Task(
            config=self.tasks_config['data_collection_task'],
            agent=self.data_collector(),
            output_file='outputs/data_collection.md',
        )

    @task
    def content_generation_task(self) -> Task:
        """
        Defines the task for generating initial message content.
        
        Returns:
            Task: Configured content generation task
        """
        return Task(
            config=self.tasks_config['content_generation_task'],
            agent=self.content_creator(),
            output_file='outputs/content.md'
        )
    
    @task
    def tone_adjustment_task(self) -> Task:
        """
        Defines the task for refining message tone and style.
        
        Returns:
            Task: Configured tone adjustment task
        """
        return Task(
            config=self.tasks_config['tone_adjustment_task'],
            agent=self.tone_expert(),
            output_pydantic=OutputFormat,
            output_file='outputs/tone.md'
        )

    @crew
    def crew(self) -> Crew:
        """
        Creates and configures the CrewAI workflow.
        
        Returns:
            Crew: Configured crew with sequential task processing
        """
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # manager_llm=llm,
            manager_agent=self.manager_agent(),
            output_log_file='outputs/happy_guy.log'
        )