#!/usr/bin/python
# -*- coding: utf-8 -*-

# 工程文件的路径
projectDir = ''

xcworkspaceName = ''
targetName = ''
# 导出路径
exportPath = ''
# Xcode8.3之后只需导入一个plist 不需要再配置证书，配置文件
# 此文件可用Xcode正常的打一个包，就可以在对应的.ipa文件下，找到该文件
exportOptionsPath = '.../ExportOptions.plist'