from Bio.Seq import Seq
from Bio import ExPASy
from Bio import Prosite
from Bio.Prosite import Pattern as pa
class ConsensusPredictor:
	def __init__(self, s=None, ps=None):
		self.sequence = Seq(s)
		self.prosite = ExPASy.get_prosite_raw(ps)
		self.record = Prosite.read(self.prosite)
		self.pat = pa.compile(self.record.pattern)

	def get_pattern(self):
		return self.pat

	def predict_consensus(self):
		self.match = self.pat.match(self.sequence)
		
