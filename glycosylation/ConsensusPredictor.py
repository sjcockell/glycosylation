from Bio.Seq import Seq
from Bio import ExPASy
from Bio import Prosite
from Bio.Prosite import Pattern as pa
import re

class ConsensusPredictor:
	def __init__(self, s=None, ps=None):
		if isinstance(s, basestring):
			self.sequence = Seq(s)
		else:
			self.sequence = s
		self.prosite = ExPASy.get_prosite_raw(ps)
		self.record = Prosite.read(self.prosite)
		self.pat = pa.compile(self.record.pattern)
		self.regexp = re.compile(pa.prosite_to_re(self.record.pattern))


	def get_pattern(self):
		return self.pat

	def predict_consensus(self):
		self.number_matches = 0
#		self.matches = self.pat.findall(self.sequence)
		self.matches = self.regexp.findall(Seq.tostring(self.sequence))
		for self.match in self.matches:
			self.number_matches += 1
		return self.number_matches
#		iif self.match is None:
#			return 0
#		else:
#			self.consensus = self.sequence[self.match.start():self.match.end()]
#			return 1
