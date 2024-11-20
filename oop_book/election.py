class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0
    
    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        self.votes += other
        return self


class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        total_votes = 0
        most_votes = 0
        winner = None

        for candidate in candidates:
            total_votes += candidate.votes
            if candidate.votes > most_votes:
                most_votes = candidate.votes
                winner = candidate.name
        
        for candidate in candidates:
            name = candidate.name
            votes = candidate.votes

            print(f"{name}: {votes} votes")
        
        
        
        percentage = f"{(most_votes / total_votes) * 100:.1f}%"

        print(f"\n{winner} won: {percentage} of votes")
        

        
        
    

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1
    
    


election = Election(candidates)
election.results()