import sys
import os
from Bio import ExPASy
from Bio import SeqIO
class SequenceHandler:
	"methods for handling sequencing within project"
	seq_record
	def __init__(self, sprot_code=None):
		"sets variables for instance"
		handle = ExPASy.get_sprot_raw(sprot_code)
		seq_record = SeqIO.read(handle, "swiss")
		print seq_record.id
		print repr(seq_record.seq)
		print len(seq_record.seq)
		handle.close()
