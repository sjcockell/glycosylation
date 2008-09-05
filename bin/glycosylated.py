import glycosylation.ConsensusPredictor as cp
import glycosylation.SequenceHandler as sh
import sys
import os

def find_domains():
	n_gly = 'PS00001'
	er_loc = 'PS00014'
	gly_site = 0
	er_sig = 0
	both = 0
	total = 0
	file = os.path.abspath(__file__)
	file = os.path.dirname(file)
	#file = os.path.join(file, "human_proteome.list")
	file = os.path.join(file, "test_data.list")
	f = open(file, 'r')
	lines = f.readlines()
	for line in lines:
		line = line.rstrip()
		seqhandler = sh.SequenceHandler(line)
		seq = seqhandler.get_sequence()
		glypred = cp.ConsensusPredictor(seq, n_gly)
		erpred = cp.ConsensusPredictor(seq, er_loc)
		gly_bool = glypred.predict_consensus
		er_bool = erpred.predict_consensus
		print gly_bool
		print er_bool
		if gly_bool == 1:
			gly_site += 1
		if er_bool == 1:
			er_sig += 1
			if gly_bool == 1:
				both += 1
		total += 1
	print total
	print gly_site
	print er_sig
	print both

if __name__ == "__main__":
	find_domains()
