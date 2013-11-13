#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

class DatacenterPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(DatacenterPage, self).__init__(parent)

## The First Group
        dcSettingGroup = QtGui.QGroupBox("Datacenter Setting")

#### Architecture
        archLabel = QtGui.QLabel("Architecture:")
        self.archCombo = QtGui.QComboBox()
        self.archCombo.addItem("X86")
        self.archCombo.addItem("Power")

        archLayout = QtGui.QHBoxLayout()
        archLayout.addWidget(archLabel)
        archLayout.addWidget(self.archCombo)

#### Upper Threshold
        upperThrLabel = QtGui.QLabel("Upper Threshold:")
        self.upperThrSpinBox = QtGui.QDoubleSpinBox()
        self.upperThrSpinBox.setRange(0.0, 1.0)
        self.upperThrSpinBox.setSingleStep(0.01)
        self.upperThrSpinBox.setValue(0.8)

        upperThrLayout = QtGui.QHBoxLayout()
        upperThrLayout.addWidget(upperThrLabel)
        upperThrLayout.addWidget(self.upperThrSpinBox)

#### Operating System

        osLabel = QtGui.QLabel("Operating System:")
        self.osCombo = QtGui.QComboBox()
        self.osCombo.addItem("Linux")
        self.osCombo.addItem("Windows")
        
        osLayout = QtGui.QHBoxLayout()
        osLayout.addWidget(osLabel)
        osLayout.addWidget(self.osCombo)

#### Lower Threshold
        lowerThrLabel = QtGui.QLabel("Lower Threshold:")
        self.lowerThrSpinBox = QtGui.QDoubleSpinBox()
        self.lowerThrSpinBox.setRange(0.0, 1.0)
        self.lowerThrSpinBox.setSingleStep(0.01)
        self.lowerThrSpinBox.setValue(0.2)

        lowerThrLayout = QtGui.QHBoxLayout()
        lowerThrLayout.addWidget(lowerThrLabel)
        lowerThrLayout.addWidget(self.lowerThrSpinBox)

#### Hypervisor
        hyperLabel = QtGui.QLabel("Hypervisor:")
        self.hyperCombo = QtGui.QComboBox()
        self.hyperCombo.addItem("Xen")
        self.hyperCombo.addItem("Kvm")

        hyperLayout = QtGui.QHBoxLayout()
        hyperLayout.addWidget(hyperLabel)
        hyperLayout.addWidget(self.hyperCombo)

#### VM Migrations
        vmMigLabel = QtGui.QLabel("VM Migrations:")
        self.vmMigCombo = QtGui.QComboBox()
        self.vmMigCombo.addItem("Enabled")
        self.vmMigCombo.addItem("Disabled")

        vmMigLayout = QtGui.QHBoxLayout()
        vmMigLayout.addWidget(vmMigLabel)
        vmMigLayout.addWidget(self.vmMigCombo)

#### Sheduling Interval
        shedulingIntervalLabel = QtGui.QLabel("Sheduling Interval")
        self.shedulingIntervalSpinBox = QtGui.QSpinBox()
        self.shedulingIntervalSpinBox.setRange(300,600)
        self.shedulingIntervalSpinBox.setSingleStep(300300300)
        self.shedulingIntervalSpinBox.setValue(300)

        shedulingIntervalLayout = QtGui.QHBoxLayout()
        shedulingIntervalLayout.addWidget(shedulingIntervalLabel)
        shedulingIntervalLayout.addWidget(self.shedulingIntervalSpinBox)

#### workload
        workloadLabel = QtGui.QLabel("WorkLoad:")
        self.workloadCombo = QtGui.QComboBox()
        self.workloadCombo.addItem("20110303")
        self.workloadCombo.addItem("20110306")
        self.workloadCombo.addItem("20110309")
        self.workloadCombo.addItem("20110322")
        self.workloadCombo.addItem("20110325")
        self.workloadCombo.addItem("20110403")
        self.workloadCombo.addItem("20110409")
        self.workloadCombo.addItem("20110411")
        self.workloadCombo.addItem("20110412")
        self.workloadCombo.addItem("20110420")

        workloadLayout = QtGui.QHBoxLayout()
        workloadLayout.addWidget(workloadLabel)
        workloadLayout.addWidget(self.workloadCombo)

#### processing cost

        processCostLabel = QtGui.QLabel("Processing Cost(per sec):")
        self.processCostSpinBox = QtGui.QDoubleSpinBox()
        #self.processCostSpinBox.setMinimum(0.0)
        self.processCostSpinBox.setRange(0.0, 100.0)
        self.processCostSpinBox.setSingleStep(0.1)
        self.processCostSpinBox.setValue(0.1)

        processCostLayout = QtGui.QHBoxLayout()
        processCostLayout.addWidget(processCostLabel)
        processCostLayout.addWidget(self.processCostSpinBox)
#### memory cost
        memoryCostLabel = QtGui.QLabel("Memory Cost(per MB):")
        self.memoryCostSpinBox = QtGui.QDoubleSpinBox()
        #self.memoryCostSpinBox.setMinimum(0.0)
        self.memoryCostSpinBox.setRange(0.0, 100.0)
        self.memoryCostSpinBox.setSingleStep(0.01)
        self.memoryCostSpinBox.setValue(0.05)

        memoryCostLayout = QtGui.QHBoxLayout()
        memoryCostLayout.addWidget( memoryCostLabel)
        memoryCostLayout.addWidget(self. memoryCostSpinBox)
#### storage cost
        storageCostLabel = QtGui.QLabel("Storage Cost(per MB):")
        self.storageCostSpinBox = QtGui.QDoubleSpinBox()
        #self.storageCostSpinBox.setMinimum(0.0)
        self.storageCostSpinBox.setRange(0.0, 100.0)
        self.storageCostSpinBox.setSingleStep(0.01)
        self.storageCostSpinBox.setValue(0.01)

        storageCostLayout = QtGui.QHBoxLayout()
        storageCostLayout.addWidget(storageCostLabel)
        storageCostLayout.addWidget(self.storageCostSpinBox)
#### bandwidth cost
        bandwidthCostLabel = QtGui.QLabel("Bandwidth Cost(per MB):")
        self.bandwidthCostSpinBox = QtGui.QDoubleSpinBox()
        #self.bandwidthCostSpinBox.setMinimum(0.0)
        self.bandwidthCostSpinBox.setRange(0.0, 100.0)
        self.bandwidthCostSpinBox.setSingleStep(0.1)
        self.bandwidthCostSpinBox.setValue(0.1)

        bandwidthCostLayout = QtGui.QHBoxLayout()
        bandwidthCostLayout.addWidget(bandwidthCostLabel)
        bandwidthCostLayout.addWidget(self.bandwidthCostSpinBox)
### The dcSetting GridLayout
        dcSettingLayout = QtGui.QGridLayout()
        dcSettingLayout.addLayout(archLayout, 0, 0)
        dcSettingLayout.addLayout(upperThrLayout, 0, 1)
        dcSettingLayout.addLayout(osLayout, 1, 0)
        dcSettingLayout.addLayout(lowerThrLayout, 1, 1)
        dcSettingLayout.addLayout(hyperLayout, 2, 0)
        dcSettingLayout.addLayout(vmMigLayout, 2, 1)
        dcSettingLayout.addLayout(shedulingIntervalLayout, 3, 0)
        dcSettingLayout.addLayout(workloadLayout, 3, 1)
        dcSettingLayout.addLayout(processCostLayout, 4, 0)
        dcSettingLayout.addLayout(memoryCostLayout, 4, 1)
        dcSettingLayout.addLayout(storageCostLayout, 5, 0)
        dcSettingLayout.addLayout(bandwidthCostLayout, 5, 1)


        dcSettingGroup.setLayout(dcSettingLayout)



## The Second Group
        dcInfoGroup = QtGui.QGroupBox("General Information")
        hostLabel = QtGui.QLabel("<i>Number of hosts:</i>")
        vmLabel = QtGui.QLabel("<i>Number of virtual machines:<i>")
        self.numHostLabel = QtGui.QLabel("")
        self.numVmLabel = QtGui.QLabel("")

        infoLayout= QtGui.QGridLayout()
        infoLayout.addWidget(hostLabel, 0, 0)
        infoLayout.addWidget(self.numHostLabel, 0, 1)
        infoLayout.addWidget(vmLabel, 1, 0)
        infoLayout.addWidget(self.numVmLabel, 1, 1)

        dcInfoGroup.setLayout(infoLayout)

## The main layout
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(dcSettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addStretch(1)
        mainLayout.addWidget(dcInfoGroup)

        self.setLayout(mainLayout)

    def save(self):
        print self.archCombo.currentText()

class HostPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HostPage, self).__init__(parent)
## First Group
        hostSettingGroup = QtGui.QGroupBox("Host Setting")

        numOfHostLabel = QtGui.QLabel("Number of Hosts:")
        self.numOfHostSpinBox = QtGui.QSpinBox()
        self.numOfHostSpinBox.setRange(1, 1500)
        self.numOfHostSpinBox.setSingleStep(1)
        self.numOfHostSpinBox.setValue(800)
        self.numOfHostSpinBox.valueChanged.connect(self.updateHostInfoGroup)
        
        vmSchedulingLabel = QtGui.QLabel("Virtual Machine Scheduling:")
        self.vmSchedulingCombo = QtGui.QComboBox()
        self.vmSchedulingCombo.addItem("Time Shared")
        self.vmSchedulingCombo.addItem("Space Shared")

        powerModelLabel = QtGui.QLabel("Power Model:")
        self.powerModelCombo = QtGui.QComboBox()
        self.powerModelCombo.addItem("Linear")
        self.powerModelCombo.addItem("Square root")
        self.powerModelCombo.addItem("Square")
        self.powerModelCombo.addItem("Clubic")
        self.powerModelCombo.addItem("Spec Power")


        ramProvisionerLabel = QtGui.QLabel("RAM Provisioner:")
        self.ramProvisionerCombo = QtGui.QComboBox()
        self.ramProvisionerCombo.addItem("Simple")
        self.ramProvisionerCombo.addItem("Dynamic")

        bandwidthProvisionerLabel = QtGui.QLabel("Bandwidth Provisioner:")
        self.bandwidthProvisionerCombo = QtGui.QComboBox()
        self.bandwidthProvisionerCombo.addItem("Simple")
        self.bandwidthProvisionerCombo.addItem("Dynamic")

        peProvisionerLabel = QtGui.QLabel("PE Provisioner:")
        self.peProvisionerCombo = QtGui.QComboBox()
        self.peProvisionerCombo.addItem("Simple")
        self.peProvisionerCombo.addItem("Dynamic")

        hostSettingLayout = QtGui.QGridLayout()
        hostSettingLayout.addWidget(numOfHostLabel, 0, 0)
        hostSettingLayout.addWidget(self.numOfHostSpinBox, 0, 1)
        hostSettingLayout.addWidget(vmSchedulingLabel, 1, 0)
        hostSettingLayout.addWidget(self.vmSchedulingCombo, 1, 1)
        hostSettingLayout.addWidget(powerModelLabel, 2, 0)
        hostSettingLayout.addWidget(self.powerModelCombo, 2, 1)
        hostSettingLayout.addWidget(ramProvisionerLabel, 3, 0)
        hostSettingLayout.addWidget(self.ramProvisionerCombo, 3, 1)
        hostSettingLayout.addWidget(bandwidthProvisionerLabel, 4, 0)
        hostSettingLayout.addWidget(self.bandwidthProvisionerCombo, 4, 1)
        hostSettingLayout.addWidget(peProvisionerLabel, 5, 0)
        hostSettingLayout.addWidget(self.peProvisionerCombo, 5, 1)

        hostSettingGroup.setLayout(hostSettingLayout)

# Second Group

        hostInfoGroup = QtGui.QGroupBox("Information")

        num = self.numOfHostSpinBox.value()/2
        numberLabel = QtGui.QLabel("<b>The Numbers of Hosts</b>")
        describeLabel = QtGui.QLabel("<b>Description</b>")
        type1Label = QtGui.QLabel("HP ProLiant ML110 G4 (1 x [Xeon 3040 1860 MHz, 2 cores], 4GB)")
        type2Label = QtGui.QLabel("HP ProLiant ML110 G5 (1 x [Xeon 3075 2660 MHz, 2 cores], 4GB)")

        self.num1Label = QtGui.QLabel(QString.number(num))
        self.num2Label = QtGui.QLabel(QString.number(num))

        hostInfoLayout= QtGui.QGridLayout()
        hostInfoLayout.addWidget(numberLabel, 0, 0)
        hostInfoLayout.addWidget(describeLabel, 0, 1)
        hostInfoLayout.addWidget(self.num1Label, 1, 0)
        hostInfoLayout.addWidget(type1Label, 1, 1)
        hostInfoLayout.addWidget(self.num2Label, 2, 0)
        hostInfoLayout.addWidget(type2Label, 2, 1)

        hostInfoGroup.setLayout(hostInfoLayout)


        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(hostSettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addStretch(1)
        mainLayout.addWidget(hostInfoGroup)

        self.setLayout(mainLayout)

    def updateHostInfoGroup(self):
        num = self.numOfHostSpinBox.value()/2
        extra = self.numOfHostSpinBox.value()%2
        num1 = num2 =  num

        if extra == 1:
            num1 = num+1

        self.num1Label.setText(QString.number(num1))
        self.num2Label.setText(QString.number(num2))

class VMPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(VMPage, self).__init__(parent)

## The First Group
        vmSettingGroup = QtGui.QGroupBox("Virtual Machine Setting")

        numOfVMLabel = QtGui.QLabel("Number of Virtual Machines:")
        self.numOfVMSpinBox = QtGui.QSpinBox()
#        self.numOfVMSpinBox.setMinimum(1)
        self.numOfVMSpinBox.setRange(1, 2000)
        self.numOfVMSpinBox.setSingleStep(1)
        self.numOfVMSpinBox.setValue(1500)
        self.numOfVMSpinBox.valueChanged.connect(self.updateVmInfoGroup)

        numOfVMLayout = QtGui.QHBoxLayout()
        numOfVMLayout.addWidget(numOfVMLabel)
        numOfVMLayout.addWidget(self.numOfVMSpinBox)

        vmSettingLayout = QtGui.QVBoxLayout()
        vmSettingLayout.addLayout(numOfVMLayout)

        vmSettingGroup.setLayout(vmSettingLayout)

## The Second Group
        vmInfoGroup = QtGui.QGroupBox("Information")

        num = self.numOfVMSpinBox.value()/4
        num1 = num2 = num3 = num4 = num
        numberLabel = QtGui.QLabel("<b>The Numbers of VMs</b>")
        describeLabel = QtGui.QLabel("<b>Description</b>")
        type1Label = QtGui.QLabel("High-CPU Medium Instance: 2.5 EC2 Compute Units, 0.85 GB")
        type2Label = QtGui.QLabel("Large Instance: 2 EC2 Compute Units, 3.75 GB")
        type3Label = QtGui.QLabel("Small Instance: 1 EC2 Compute Unit, 1.7 GB")
        type4Label = QtGui.QLabel("Micro Instance: 0.5 EC2 Compute Unit, 0.633 GB")


        self.num1Label = QtGui.QLabel(QString.number(num1))
        self.num2Label = QtGui.QLabel(QString.number(num2))
        self.num3Label = QtGui.QLabel(QString.number(num3))
        self.num4Label = QtGui.QLabel(QString.number(num4))

        vmInfoLayout= QtGui.QGridLayout()
        vmInfoLayout.addWidget(numberLabel, 0, 0)
        vmInfoLayout.addWidget(describeLabel, 0, 1)
        vmInfoLayout.addWidget(self.num1Label, 1, 0)
        vmInfoLayout.addWidget(type1Label, 1, 1)
        vmInfoLayout.addWidget(self.num2Label, 2, 0)
        vmInfoLayout.addWidget(type2Label, 2, 1)
        vmInfoLayout.addWidget(self.num3Label, 3, 0)
        vmInfoLayout.addWidget(type3Label, 3, 1)
        vmInfoLayout.addWidget(self.num4Label, 4, 0)
        vmInfoLayout.addWidget(type4Label, 4, 1)

        vmInfoGroup.setLayout(vmInfoLayout)


        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(vmSettingGroup)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(30)
        mainLayout.addWidget(vmInfoGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def updateVmInfoGroup(self):

        num = self.numOfVMSpinBox.value()/4
        extra = self.numOfVMSpinBox.value()%4
        num1 = num2 = num3 = num4 = num

        if extra == 3:
            num1 = num+1
            num2 = num+1
            num3 = num+1
        elif extra == 2:
            num1 = num+1
            num2 = num+1
        elif extra == 1:
            num1 = num+1

        self.num1Label.setText(QString.number(num1))
        self.num2Label.setText(QString.number(num2))
        self.num3Label.setText(QString.number(num3))
        self.num4Label.setText(QString.number(num4))


class PolicyPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(PolicyPage, self).__init__(parent)

## First Group
        keySettingGroup = QtGui.QGroupBox("Key Policy Setting")

        vmAllocationLabel = QtGui.QLabel("Virtual Machine Allocation Policy:")
        self.vmAllocationComboBox = QtGui.QComboBox()
        self.vmAllocationComboBox.addItem("IQR")
        self.vmAllocationComboBox.addItem("MAD")
        self.vmAllocationComboBox.addItem("LR")
        self.vmAllocationComboBox.addItem("LRR")
        self.vmAllocationComboBox.addItem("THR")
        self.vmAllocationComboBox.addItem("DVFS")
        self.vmAllocationComboBox.addItem("NPA")
        
        vmAllocationInfoButton = QtGui.QPushButton() 
        vmAllocationInfoButton.setIcon(QtGui.QIcon("./images/info.png"))
        vmAllocationInfoButton.setFlat(True)
        vmAllocationInfoButton.clicked.connect(self.vmAllocationMsgBox)

        vmSelectionLabel = QtGui.QLabel("Virtual Machine Selection Policy:")
        self.vmSelectionComboBox = QtGui.QComboBox()
        self.vmSelectionComboBox.addItem("MC")
        self.vmSelectionComboBox.addItem("MMT")
        self.vmSelectionComboBox.addItem("MU")
        self.vmSelectionComboBox.addItem("RS")
        self.vmSelectionComboBox.addItem("NPA")

        vmSelectionInfoButton = QtGui.QPushButton() 
        vmSelectionInfoButton.setIcon(QtGui.QIcon("./images/info.png"))
        vmSelectionInfoButton.setFlat(True)
        vmSelectionInfoButton.clicked.connect(self.vmSelectionMsgBox)


        parameterLabel = QtGui.QLabel("Parameter:")
        self.parameterEdit = QtGui.QLineEdit()

        keySettingLayout = QtGui.QGridLayout()
        keySettingLayout.addWidget(vmAllocationLabel, 0, 0)
        keySettingLayout.addWidget(self.vmAllocationComboBox, 0, 1)
        keySettingLayout.addWidget(vmAllocationInfoButton, 0, 2)
        keySettingLayout.addWidget(vmSelectionLabel, 1, 0)
        keySettingLayout.addWidget(self.vmSelectionComboBox, 1, 1)
        keySettingLayout.addWidget(vmSelectionInfoButton, 1, 2)
        keySettingLayout.addWidget(parameterLabel, 2, 0)
        keySettingLayout.addWidget(self.parameterEdit, 2, 1)

        keySettingGroup.setLayout(keySettingLayout)

## Second Group
        generalSettingGroup = QtGui.QGroupBox("General Setting")

        outputFolderLabel = QtGui.QLabel("Output Folder:")
        self.outputFolderEdit = QtGui.QLineEdit()
        self.outputFolderEdit.setText("output_test")

        self.outputToFile = QtGui.QCheckBox("Output to Files")

        generalLayout = QtGui.QGridLayout()
        generalLayout.addWidget(outputFolderLabel, 0, 0)
        generalLayout.addWidget(self.outputFolderEdit, 0, 1)
        generalLayout.addWidget(self.outputToFile, 1, 0, 1, 2)

        generalSettingGroup.setLayout(generalLayout)

## Third Information
        
        policyInfoGroup = QtGui.QGroupBox("Information")
        
        policyInfo1Label = QtGui.QLabel("<i>Output Folder</i> : Where the result are placed")
        policyInfo2Label = QtGui.QLabel("<i>Output To Files</i> : Indicate whether"
                    "the result are output to some csv files")
        policyInfo3Label = QtGui.QLabel("<i>Parameter</i> : The value of the Parameter" 
                    "depends the details of the policy ")

        policyInfoLayout = QtGui.QGridLayout()

        policyInfoLayout.addWidget(policyInfo1Label)
        policyInfoLayout.addWidget(policyInfo2Label)
        policyInfoLayout.addWidget(policyInfo3Label)

        policyInfoGroup.setLayout(policyInfoLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(keySettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(generalSettingGroup)
        mainLayout.addSpacing(20)
        mainLayout.addWidget(policyInfoGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def vmAllocationMsgBox(self):

        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Virtual Machine Allocation Policy")
        msgBox.setText("<b>The document has been modified.</b><br>"
                    "<hr>the second para<br>"
                    "<hr>the second para")
        msgBox.setIcon(1)
        msgBox.exec_()

    def vmSelectionMsgBox(self):

        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Virtual Machine Selection Policy")
        msgBox.setText("<b>The document has been modified.</b><br>"
                    "<hr>the second para<br>"
                    "<hr>the second para")
        msgBox.setIcon(1)
        msgBox.exec_()


class ConfigDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__()

        self.parent = parent
        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(80, 66))
        self.contentsWidget.setMovement(QtGui.QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QtGui.QStackedWidget()
        self.pagesWidget.addWidget(DatacenterPage())
        self.pagesWidget.addWidget(HostPage())
        self.pagesWidget.addWidget(VMPage())
        self.pagesWidget.addWidget(PolicyPage())

        self.pagesWidget.widget(1).numOfHostSpinBox.valueChanged.connect(self.updateInfoGroup)
        self.pagesWidget.widget(2).numOfVMSpinBox.valueChanged.connect(self.updateInfoGroup)

        closeButton = QtGui.QPushButton("Close")

        saveAsButton = QtGui.QPushButton("Save As")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.clicked.connect(self.parent.close)
        saveAsButton.clicked.connect(self.saveAs)

        horizontalLayout = QtGui.QHBoxLayout()
    #    horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(saveAsButton)
        buttonsLayout.addWidget(closeButton)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)
        
        self.updateInfoGroup()
        self.setLayout(mainLayout)

    def updateInfoGroup(self):

        numHost = self.pagesWidget.widget(1).numOfHostSpinBox.value()
        numVm = self.pagesWidget.widget(2).numOfVMSpinBox.value()
        self.pagesWidget.widget(0).numHostLabel.setText(QString.number(numHost))
        self.pagesWidget.widget(0).numVmLabel.setText(QString.number(numVm))

    def getConfFilename(self):
       
        workload = self.pagesWidget.widget(0).workloadCombo.currentText()
        vmAllocation = self.pagesWidget.widget(3).vmAllocationComboBox.currentText()
        vmSelection = self.pagesWidget.widget(3).vmSelectionComboBox.currentText()
        param = self.pagesWidget.widget(3).parameterEdit.text()

        return workload+'_'+vmAllocation+'_'+vmSelection+'_'+param+'.ini' 

    def writeDatacenter(self, f):
        
        dc = self.pagesWidget.widget(0)
        f.write("\nArchitecture="+dc.archCombo.currentText())
        f.write("\nUpperThreshold="+QString.number(dc.upperThrSpinBox.value()))
        f.write("\nOperateSystem="+dc.osCombo.currentText())
        f.write("\nLowerThreshold="+QString.number(dc.lowerThrSpinBox.value()))
        f.write("\nHypervisor="+dc.hyperCombo.currentText())
        f.write("\nVMMigrations="+dc.vmMigCombo.currentText())
        f.write("\nShedulingInterval="+QString.number(dc.shedulingIntervalSpinBox.value()))
        f.write("\nWorkload="+dc.workloadCombo.currentText())
        f.write("\nProcessCost="+QString.number(dc.processCostSpinBox.value()))
        f.write("\nMemoryCost="+QString.number(dc.memoryCostSpinBox.value()))
        f.write("\nStorageCost="+QString.number(dc.storageCostSpinBox.value()))
        f.write("\nBandwidthCost="+QString.number(dc.bandwidthCostSpinBox.value()))
        
    def writeHost(self, f):

        host = self.pagesWidget.widget(1)
        f.write("\nNumOfHosts="+QString.number(host.numOfHostSpinBox.value()))
        f.write("\nVMScheduling="+host.vmSchedulingCombo.currentText())
        f.write("\nPowerModel="+host.powerModelCombo.currentText())
        f.write("\nRAMProvisioner="+host.ramProvisionerCombo.currentText())
        f.write("\nBandwidthProvisioner="+host.bandwidthProvisionerCombo.currentText())
        f.write("\nPeProvisioner="+host.peProvisionerCombo.currentText())

    def writeVM(self, f):

        vm = self.pagesWidget.widget(2)
        f.write("\nNumOfVMs="+QString.number(vm.numOfVMSpinBox.value()))

    def writePolicy(self, f):

        policy = self.pagesWidget.widget(3)

        f.write("\nVmAllocationPolicy="+policy.vmAllocationComboBox.currentText())
        f.write("\nVmSelectionPolicy="+policy.vmSelectionComboBox.currentText())
        f.write("\nParameter="+policy.parameterEdit.text())
        f.write("\nOutputFolder="+policy.outputFolderEdit.text())
        if policy.outputToFile.isChecked():
            f.write("\nOutputToFile=True")
        else:
            f.write("\nOutputToFile=False")

    def saveAs(self):

        date = QDateTime.currentDateTime().toString()
        self.getConfFilename()

        fname = QtGui.QFileDialog.getSaveFileName(self, "Save IAAS CloudSim Configure File",
                    self.getConfFilename())

        if fname.isNull():
            return 

        f = open(fname, "w+")
        f.write("# Configure File For IAAS CloudSim")
        f.write("\n#      Date: "+date)
        f.write("\n#      Author: wanglong(wanglong@l-cloud.org)")
        f.write("\n\n# Datacenter Setting")
        self.writeDatacenter(f)
        f.write("\n\n# Host Setting")
        self.writeHost(f)
        f.write("\n\n# Virtual Machine Setting")
        self.writeVM(f)
        f.write("\n\n# Policy Setting")
        self.writePolicy(f)
        f.write("\n")
        f.close()


        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Save Configuue File...")
        msgBox.setText("The Configure File Saved As:<br> <b><i>"+fname+"</i></b>")
        msgBox.setIcon(1)
        msgBox.exec_()


    def changePage(self, current, previous):
        if not current:
            current = previous

        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

    def createIcons(self):
        datacenterButton = QtGui.QListWidgetItem(self.contentsWidget)
        datacenterButton.setIcon(QtGui.QIcon('./images/datacenter.png'))
        datacenterButton.setText("Data Center")
        datacenterButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        datacenterButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        hostButton = QtGui.QListWidgetItem(self.contentsWidget)
        hostButton.setIcon(QtGui.QIcon('./images/config.png'))
        hostButton.setText("Host")
        hostButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        hostButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        vmButton = QtGui.QListWidgetItem(self.contentsWidget)
        vmButton.setIcon(QtGui.QIcon('./images/update.png'))
        vmButton.setText("VM")
        vmButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        vmButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        policyButton = QtGui.QListWidgetItem(self.contentsWidget)
        policyButton.setIcon(QtGui.QIcon('./images/query.png'))
        policyButton.setText("Policy")
        policyButton.setTextAlignment(QtCore.Qt.AlignHCenter)
        policyButton.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)

class CloudConf(QtGui.QMainWindow):

    def __init__(self):
        super(CloudConf, self).__init__()

        self.initUI()

    def save(self):

        self.centralWidget().saveAs()

    def configure_datacenter(self):

        print "datacenter"
        self.centralWidget().contentsWidget.setCurrentRow(0)


    def configure_host(self):

        print "host"
        self.centralWidget().contentsWidget.setCurrentRow(1)

    def configure_vm(self):

        print "virtual machine"
        self.centralWidget().contentsWidget.setCurrentRow(2)

    def configure_policy(self):

        print "policy"
        self.centralWidget().contentsWidget.setCurrentRow(3)

    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        
        self.mainWidget = ConfigDialog(self)
        self.setCentralWidget(self.mainWidget)

        self.exitAction = QtGui.QAction(QtGui.QIcon('./images/exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(self.close)

        self.saveAction = QtGui.QAction(QtGui.QIcon('./images/save.png'), '&Save', self)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Save Configuration')
        self.connect(self.saveAction, SIGNAL('triggered()'), self.save)

        self.showDatacenterAction = QtGui.QAction(QtGui.QIcon('./images/datacenter.png'), '&Data Center', self)
        self.showDatacenterAction.setStatusTip('Show Datacenter Configuration')
        self.showDatacenterAction.setShortcut('Ctrl+D')
        self.connect(self.showDatacenterAction, SIGNAL('triggered()'), self.configure_datacenter)


        self.showHostAction = QtGui.QAction(QtGui.QIcon('./images/host.png'), '&Host', self)
        self.showHostAction.setStatusTip('Show Host Configuration')
        self.showHostAction.setShortcut('Ctrl+H')
        self.connect(self.showHostAction,SIGNAL('triggered()'), self.configure_host)
    
        self.showVMAction = QtGui.QAction(QtGui.QIcon('./images/vm.png'), '&VM', self)
        self.showVMAction.setStatusTip('Show Virtual Machine Configuration')
        self.showVMAction.setShortcut('Ctrl+M')
        self.connect(self.showVMAction, SIGNAL('triggered()'), self.configure_vm)

        self.showPolicyAction = QtGui.QAction(QtGui.QIcon('./images/policy.png'), '&Policy', self)
        self.showPolicyAction.setStatusTip('Show Policy Configuration')
        self.showPolicyAction.setShortcut('Ctrl+P')
        self.connect(self.showPolicyAction, SIGNAL('triggered()'), self.configure_policy)


        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('&File')
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.exitAction)

        self.confMenu = self.menuBar.addMenu('&Configure')
        self.confMenu.addAction(self.showDatacenterAction)
        self.confMenu.addAction(self.showHostAction)
        self.confMenu.addAction(self.showVMAction)
        self.confMenu.addAction(self.showPolicyAction)
        
        self.toolbar = self.addToolBar('File')
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.setIconSize(QtCore.QSize(36, 36))
        self.toolbar.addAction(self.saveAction)

        self.toolbar = self.addToolBar('Configure')
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.setIconSize(QtCore.QSize(36, 36))
        self.toolbar.addAction(self.showDatacenterAction)
        self.toolbar.addAction(self.showHostAction)
        self.toolbar.addAction(self.showVMAction)
        self.toolbar.addAction(self.showPolicyAction)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.setIconSize(QtCore.QSize(36, 36))
        self.toolbar.addAction(self.exitAction)
#        self.statusBar().showMessage('Ready')


        self.resize(640, 500)
        self.center()
        self.setWindowIcon(QtGui.QIcon('./images/icon.png'))
        self.setWindowTitle('IAAS CloudSim Configuration')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = CloudConf()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
