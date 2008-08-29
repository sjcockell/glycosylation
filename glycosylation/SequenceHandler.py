import sys
import os
from Bio import ExPASy
from Bio import SeqIO
class SequenceHandler:
	"methods for handling sequencing within project"
#	seq_record = SeqIO.seq_record 
	def __init__(self, sprot_code=None):
		"sets variables for instance"
		handle = ExPASy.get_sprot_raw(sprot_code)
		self.seq_record = SeqIO.read(handle, "swiss")
		handle.close()

	def get_sequence_id(self):
		return self.seq_record.id

	def get_sequence(self):
		return self.seq_record.seq

	def get_sequence_description(self):
		return self.seq_record.description

	def get_sequence_name(self):
		return self.seq_record.name

	
