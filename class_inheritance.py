class Agent:
    def __init__(self, name, model="gpt-4"):
        self.name = name
        self.model = model
        self.history = []
    
    def run(self, prompt):
        self.history.append(prompt)
        return f"[{self.name}] Processing: {prompt}"
    
    def __repr__(self):
        return f"Agent(name={self.name}, model={self.model})"


agent = Agent("ResearchBot", model="claude")
result = agent.run("Find papers on RAG")
print(result)
print(agent.history)

class SpecializedAgent(Agent):
    
    def __init__(self, name, specialty, model="gpt-4"):
        super().__init__(name, model)
        self.specialty = specialty
        
    def run(self, prompt):
        enhanced = f"[{self.specialty}] {prompt}"
        return super().run(enhanced)