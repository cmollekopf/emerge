# -*- coding: utf-8 -*-
import info
import emergePlatform
import os

class subinfo(info.infoclass):
    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.buildDependencies['win32libs/automoc'] = 'default'
        self.dependencies['win32libs/boost-program-options']   = 'default'
        self.dependencies['win32libs/libxslt'] = 'default'
        self.dependencies['libs/qt'] = 'default'
        #self.dependencies['win32libs/sqlite'] = 'default'
        self.dependencies['win32libs/shared-mime-info'] = 'default'

    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]http://git.kolab.org/diffusion/A/akonadi|kolab/integration/1.12.0|'
        self.shortDescription = "a storage service for PIM data and meta data"
        self.defaultTarget = 'gitHEAD'
        self.patchToApply['gitHEAD'] = [("akonadi-kde.conf-fix-1.10.80.diff", 1)]

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = ""
        self.subinfo.options.configure.defines += " -DWITH_SOPRANO=FALSE"


if __name__ == '__main__':
    Package().execute()
