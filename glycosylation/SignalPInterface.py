import sys
import os

class SignalPInterface:
	"methods for handling SignalP within project"
	def __init__(self, sprot_code=None):
		"sets variables for instance"
		seq_file = "out/"+sprot_code+".seq"
		signalp_command = "signalp -t euk "+seq_file

	def execute_signalp(self):
		
