# -*- coding: utf-8 -*-
import info
import os
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = 'git://gitorious.org/quassel/quassel.git'
        self.svnTargets['0.6'] = 'git://gitorious.org/quassel/quassel.git|0.6|'
        for ver in ['0.7.1','0.7.2','0.7.3','0.8.0','0.9.0','0.9.1','0.9.2','0.9.3', '0.10.0']:
            self.targets[ver] = 'http://quassel-irc.org/pub/quassel-%s.tar.bz2' % ver
            self.targetInstSrc[ver] = 'quassel-%s' % ver
        self.targetDigests['0.7.1'] = '791086da977033a1bbee3effa317668b3726bd7f'
        self.targetDigests['0.8.0'] = 'b74967fa9f19b5d7c708279075cc0ef3a3dbbe8b'
        self.targetDigests['0.10.0'] = '305d56774b1af2a891775a5637174d9048d875a7'
        
        self.defaultTarget = '0.10.0'


    def setDependencies( self ):
        self.dependencies['libs/qt'] = 'default'
        self.dependencies['kde/kde-runtime'] = 'default'
        if not self.options.isActive("kde/kde-runtime"):
            self.dependencies['kdesupport/snorenotify'] = 'default'
            self.dependencies['kdesupport/phonon-ds9'] = 'default'
        self.dependencies['win32libs/zlib'] = 'default'
        self.dependencies['kdesupport/qca'] = 'default'
        self.dependencies['dev-util/pkg-config'] = 'default'
        self.shortDescription = "a distributed IRC client"


class Package( CMakePackageBase ):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.defines = " -DWITH_SYSLOG=OFF"
        if self.subinfo.options.isActive("kde/kde-runtime"):
            self.subinfo.options.configure.defines += " -DWITH_KDE=ON"
            
    def install(self):
        if not CMakePackageBase.install(self):
            return False
        if not self.subinfo.options.isActive("kde/kde-runtime"): 
            os.makedirs(os.path.join(self.installDir(),"bin"))
            shutil.move(os.path.join(self.installDir(),"quassel.exe"),os.path.join(self.installDir(),"bin","quassel.exe"))
            shutil.move(os.path.join(self.installDir(),"quasselcore.exe"),os.path.join(self.installDir(),"bin","quasselcore.exe"))
            shutil.move(os.path.join(self.installDir(),"quasselclient.exe"),os.path.join(self.installDir(),"bin","quasselclient.exe"))
        return True
        



if __name__ == '__main__':
    Package().execute()
