# Makefile for run CloudConf
#
#
.PHONY: run motif clean test

run:
	./cloudconf.py  -style cleanlooks
	
motif:
	./cloudconf.py  -style motif

test:
	./NPA_IAAScloudsim.jar 20110303_NPA_NPA_0.8.ini 
	
	@echo "********TEST FOR  20110303_DVFS__.ini START***********"
	./IAAScloudsim.jar 20110303_DVFS__.ini 
	@echo "********TEST FOR  20110303_DVFS__.ini  END ***********"
	
	@echo "********TEST FOR 20110303_IQR START***********"
	./IAAScloudsim.jar 20110303_IQR_MC_1.5.ini 
	./IAAScloudsim.jar 20110303_IQR_MMT_1.5.ini 
	./IAAScloudsim.jar 20110303_IQR_RS_1.5.ini 
	./IAAScloudsim.jar 20110303_IQR_MU_1.5.ini 
	@echo "********TEST FOR 20110303_IQR.ini END ***********"
	
	@echo "********TEST FOR 20110303_THR START***********"
	./IAAScloudsim.jar 20110303_THR_MC_0.8.ini 
	./IAAScloudsim.jar 20110303_THR_MMT_0.8.ini 
	./IAAScloudsim.jar 20110303_THR_RS_0.8.ini 
	./IAAScloudsim.jar 20110303_THR_MU_0.8.ini 
	@echo "********TEST FOR 20110303_THR.ini END ***********"
	
	@echo "********TEST FOR 20110303_MAD START***********"
	./IAAScloudsim.jar 20110303_MAD_MC_2.5.ini 
	./IAAScloudsim.jar 20110303_MAD_MMT_2.5.ini 
	./IAAScloudsim.jar 20110303_MAD_MU_2.5.ini 
	./IAAScloudsim.jar 20110303_MAD_RS_2.5.ini 
	@echo "********TEST FOR 20110303_MAD.ini END ***********"
	
	@echo "********TEST FOR 20110303_LR START***********"
	./IAAScloudsim.jar 20110303_LR_MC_1.2.ini 
	./IAAScloudsim.jar 20110303_LR_MMT_1.2.ini 
	./IAAScloudsim.jar 20110303_LR_MU_1.2.ini 
	./IAAScloudsim.jar 20110303_LR_RS_1.2.ini 
	@echo "********TEST FOR 20110303_LR.ini END ***********"
	
	@echo "********TEST FOR 20110303_LRR START***********"
	./IAAScloudsim.jar 20110303_LRR_MC_1.2.ini 
	./IAAScloudsim.jar 20110303_LRR_MMT_1.2.ini 
	./IAAScloudsim.jar 20110303_LRR_MU_1.2.ini 
	./IAAScloudsim.jar 20110303_LRR_RS_1.2.ini 
	@echo "********TEST FOR 20110303_LRR.ini END ***********"
