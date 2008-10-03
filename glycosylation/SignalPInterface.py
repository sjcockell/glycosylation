import sys
import os
import re
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
		elif outtype == 'full':
			self.signalp_command = "signalp -t euk -f full "+seq_file
		elif outtype == 'short':
			self.signalp_command = "signalp -t euk -f short "+seq_file
		elif outtype == 'summary':
			self.signalp_command = "signalp -t euk -f summary "+seq_file

	def execute_signalp(self):
		fin, fout = os.popen4(self.signalp_command)
		result = fout.read()
		return result

	def parse_signalp_summary(self, output=None):
		yes_count = 0
		linelist = output.splitlines()
		nnlist = linelist[9:14]
		p = re.compile('YES$')
		p2 = re.compile('Prediction')
		p3 = re.compile('Signal peptide')
		for nn in nnlist:
			m = p.search(nn)
			if m:
				yes_count += 1
		for line in linelist:
			m2 = p2.match(line)
			if m2:
				m3 = p3.search(line)
				if m3:
					yes_count += 1
		return yes_count
