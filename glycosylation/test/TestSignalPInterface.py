import glycosylation.SignalPInterface as spi

sigp = spi.SignalPInterface('P68133', 'summary')
res = sigp.execute_signalp()
sigp.parse_signalp_summary(res)
