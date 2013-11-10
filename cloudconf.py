#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

class DatacenterPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(DatacenterPage, self).__init__(parent)

        configGroup = QtGui.QGroupBox("Datacenter configuration")

        serverLabel = QtGui.QLabel("Server:")
        self.serverCombo = QtGui.QComboBox()
        self.serverCombo.addItem("Trolltech (Australia)")
        self.serverCombo.addItem("Trolltech (Germany)")
        self.serverCombo.addItem("Trolltech (Norway)")
        self.serverCombo.addItem("Trolltech (People's Republic of China)")
        self.serverCombo.addItem("Trolltech (USA)")

        serverLayout = QtGui.QHBoxLayout()
        serverLayout.addWidget(serverLabel)
        serverLayout.addWidget(self.serverCombo)

        configLayout = QtGui.QVBoxLayout()
        configLayout.addLayout(serverLayout)
        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def save(self):
        print self.serverCombo.currentText()

class HostPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HostPage, self).__init__(parent)

        configGroup = QtGui.QGroupBox("Host configuration")

        serverLabel = QtGui.QLabel("Server:")
        serverCombo = QtGui.QComboBox()
        serverCombo.addItem("Trolltech (Australia)")
        serverCombo.addItem("Trolltech (Germany)")
        serverCombo.addItem("Trolltech (Norway)")
        serverCombo.addItem("Trolltech (People's Republic of China)")
        serverCombo.addItem("Trolltech (USA)")

        serverLayout = QtGui.QHBoxLayout()
        serverLayout.addWidget(serverLabel)
        serverLayout.addWidget(serverCombo)

        configLayout = QtGui.QVBoxLayout()
        configLayout.addLayout(serverLayout)
        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class VMPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(VMPage, self).__init__(parent)

        updateGroup = QtGui.QGroupBox("Virtual Machine Configure")
        systemCheckBox = QtGui.QCheckBox("Update system")
        appsCheckBox = QtGui.QCheckBox("Update applications")
        docsCheckBox = QtGui.QCheckBox("Update documentation")

        packageGroup = QtGui.QGroupBox("Existing packages")

        packageList = QtGui.QListWidget()
        qtItem = QtGui.QListWidgetItem(packageList)
        qtItem.setText("Qt")
        qsaItem = QtGui.QListWidgetItem(packageList)
        qsaItem.setText("QSA")
        teamBuilderItem = QtGui.QListWidgetItem(packageList)
        teamBuilderItem.setText("Teambuilder")

        startUpdateButton = QtGui.QPushButton("Start update")

        updateLayout = QtGui.QVBoxLayout()
        updateLayout.addWidget(systemCheckBox)
        updateLayout.addWidget(appsCheckBox)
        updateLayout.addWidget(docsCheckBox)
        updateGroup.setLayout(updateLayout)

        packageLayout = QtGui.QVBoxLayout()
        packageLayout.addWidget(packageList)
        packageGroup.setLayout(packageLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(updateGroup)
        mainLayout.addWidget(packageGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startUpdateButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class PolicyPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(PolicyPage, self).__init__(parent)

        packagesGroup = QtGui.QGroupBox("Policy Selection")

        nameLabel = QtGui.QLabel("Name:")
        nameEdit = QtGui.QLineEdit()

        dateLabel = QtGui.QLabel("Released after:")
        dateEdit = QtGui.QDateTimeEdit(QtCore.QDate.currentDate())

        releasesCheckBox = QtGui.QCheckBox("Releases")
        upgradesCheckBox = QtGui.QCheckBox("Upgrades")

        hitsSpinBox = QtGui.QSpinBox()
        hitsSpinBox.setPrefix("Return up to ")
        hitsSpinBox.setSuffix(" results")
        hitsSpinBox.setSpecialValueText("Return only the first result")
        hitsSpinBox.setMinimum(1)
        hitsSpinBox.setMaximum(100)
        hitsSpinBox.setSingleStep(10)

        startQueryButton = QtGui.QPushButton("Start query")

        packagesLayout = QtGui.QGridLayout()
        packagesLayout.addWidget(nameLabel, 0, 0)
        packagesLayout.addWidget(nameEdit, 0, 1)
        packagesLayout.addWidget(dateLabel, 1, 0)
        packagesLayout.addWidget(dateEdit, 1, 1)
        packagesLayout.addWidget(releasesCheckBox, 2, 0)
        packagesLayout.addWidget(upgradesCheckBox, 3, 0)
        packagesLayout.addWidget(hitsSpinBox, 4, 0, 1, 2)
        packagesGroup.setLayout(packagesLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(packagesGroup)
        mainLayout.addSpacing(12)
        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class ConfigDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)

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

        closeButton = QtGui.QPushButton("Close")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        closeButton.clicked.connect(self.close)

        horizontalLayout = QtGui.QHBoxLayout()
    #    horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(closeButton)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

#        self.setWindowTitle("Config Dialog")

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

        print "-------------------save--------------------"
        dcWidget = self.centralWidget().pagesWidget.widget(0)
        hostWidget = self.centralWidget().pagesWidget.widget(1)
        vmWidget = self.centralWidget().pagesWidget.widget(2)
        pyWidget = self.centralWidget().pagesWidget.widget(3)
        print dcWidget.save()

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
        
        self.mainWidget = ConfigDialog()
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


        self.resize(800, 600)
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
