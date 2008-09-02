import glycosylation.SequenceHandler as sh

seqhandler = sh.SequenceHandler('P68133')
id = seqhandler.get_sequence_id()
print id
seq = seqhandler.get_sequence()
print seq
