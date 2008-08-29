import Bio.Prosite
class ConsensusPredictor:
	def __init__(self, s=None, ps=None):
		self.sequence = s
		self.prosite = Bio.Prosite.Pattern(ps)

	def predict_consensus(self):
		match = self.prosite.PrositeMatch(self.sequence)
		print match
		
