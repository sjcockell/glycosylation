import glycosylation.ConsensusPredictor as cp
import glycosylation.SequenceHandler as sh
import sys
import os

def find_domains():
	n_gly = 'PS00001'
	er_loc = 'PS00014'
	gly_site = 0
	gly_pro = 0
	er_sig = 0
	er_pro = 0
	both_pro = 0
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
		gly_bool = glypred.predict_consensus()
		er_bool = erpred.predict_consensus()
		if gly_bool > 0:
			gly_site += gly_bool
			gly_pro += 1
		if er_bool > 0:
			er_sig += er_bool
			er_pro += 1
			if gly_bool >= 0:
				both_pro += 1
		total += 1
	print "Number of proteins:\t",
	print total
	print "Number of N-Gly Dom:\t",
	print gly_site,
	print " in ",
	print gly_pro,
	print " proteins"
	print "Number of ER Loc Sig:\t",
	print er_sig,
	print " in ",
	print er_pro,
	print " proteins"
	print "Number of Glycosylated:\t",
	print both_pro

if __name__ == "__main__":
	find_domains()
