#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import config
import subprocess
import time

def autoPage():
	timeName = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))	
	xcarchivePath = os.path.join(config.projectDir, 'build', '%s.xcarchive' % config.targetName)
	xcworkspacePath = os.path.join(config.projectDir, config.xcworkspaceName)
	xcworkspacePath = '%s.xcworkspace' % xcworkspacePath

	archiveCmd = "xcodebuild -workspace " + xcworkspacePath + " -scheme " + config.targetName + ' clean archive -archivePath ' + xcarchivePath
	
	print('\n== Start Archive Please Wait ... ==')
	process = subprocess.Popen(archiveCmd, shell=True)
	# 等上一步执行完再执行下一步
	process.wait()
	# todo...需要做容错处理
	# todo...命名可以和分支绑定在一块
	exportName = config.targetName + ' ' + timeName
	exportPath = os.path.join(config.exportPath, exportName)
	print('\n== Start Export Please Wait ... ==')
	exportCmd = 'xcodebuild -exportArchive -archivePath ' + xcarchivePath + ' -exportPath ' + exportPath + ' -exportOptionsPlist ' + config.ExportOptionsPath
	exportProcess = subprocess.Popen(exportCmd, shell=True)
	exportProcess.wait()



if __name__ == '__main__':
	autoPage()





