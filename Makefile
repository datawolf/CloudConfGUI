# Makefile for run CloudConf
#
#
.PHONY: run motif clean test

run:
	./cloudconf.py  -style cleanlooks
	
motif:
	./cloudconf.py  -style motif

clean:
	$(RM)	*.ini
test:
	./NPA_IAAScloudsim.jar 20110303_NPA_NPA_0.8.ini 
	
	@echo "********TEST FOR  20110303_DVFS__.ini START*********** "
	./IAAScloudsim.jar 20110303_DVFS__.ini 
	@echo "********TEST FOR  20110303_DVFS__.ini  END *********** "
	
	@echo "********TEST FOR 20110303_IQR START*********** "
	./IAAScloudsim.jar 20110303_IQR_MC_1.5.ini 
	./IAAScloudsim.jar 20110303_IQR_MMT_1.5.ini 
	./IAAScloudsim.jar 20110303_IQR_RS_1.5.ini 
	./IAAScloudsim.jar 20110303_IQR_MU_1.5.ini 
	@echo "********TEST FOR 20110303_IQR.ini END *********** "
