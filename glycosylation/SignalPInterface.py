import sys
import os
import glycosylation.SequenceHandler as sh

class SignalPInterface:
	"methods for handling SignalP within project"
	def __init__(self, sprot_code=None, outtype=None):
		"sets variables for instance"
		if not os.path.exists('out/'):
			os.system('mkdir out/')
		seq_file = os.path.abspath('out/')
		seq_file = os.path.join(seq_file, sprot_code+".seq")			
		if not os.path.exists(seq_file):
			seqh = sh.SequenceHandler(sprot_code)
			seqh.write_sequence_file()
		if outtype is None:
			self.signalp_command = "signalp -t euk "+seq_file
		elif outtype == '':

	def execute_signalp(self):
		fin, fout = os.popen4(self.signalp_command)
		result = fout.read()
		return result

	def parse_signalp(self, output=None):
		
