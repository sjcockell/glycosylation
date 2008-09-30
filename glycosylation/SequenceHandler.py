import sys
import os
from Bio import ExPASy
from Bio import SeqIO
from Bio import Seq

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

	def get_sequence_string(self):
		return Seq.tostring(self.seq_record.seq)

	def get_sequence_description(self):
		return self.seq_record.description

	def get_sequence_name(self):
		return self.seq_record.name

	def write_sequence_file(self):
		"writes sequence file in out/$UNIPROT.seq, fasta format"
		self.records = []
		self.records.append(self.seq_record)
		self.filename = self.seq_record.id+".seq"
		output_handle = open('out/'+self.filename, "w")
		SeqIO.write(self.records, output_handle, "fasta")
		output_handle.close()

	
