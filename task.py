class Task: 
    def __init__(self, name, description, rank):
        self.name = name
        self.description = description
        self.rank = rank
    
    def __str__(self):
        return f"Name: {self.name} | Description: {self.description} | Rank: {self.rank}"
    