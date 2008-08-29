import glycosylation.SequenceHandler as sh

seqhandler = sh.SequenceHandler('P68133')
id = seqhandler.get_seq_id()
print id
seq = seqhandler.get_sequence()
print seq
