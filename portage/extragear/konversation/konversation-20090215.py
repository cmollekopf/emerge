# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets( self ):
        for ver in ['1.2.1', '1.2.2', '1.2.3', '1.3', '1.3.1']:
            self.targets[ver] = 'http://download.kde.org/stable/konversation/' + ver + '/src/konversation-' + ver + '.tar.bz2'
            self.targetInstSrc[ver] = 'konversation-' + ver
        for ver in ['1.4', '1.5']:
            self.targets[ver] = 'http://download.kde.org/stable/konversation/' + ver + '/src/konversation-' + ver + '.tar.xz'
            self.targetInstSrc[ver] = 'konversation-' + ver
        for ver in ['1.5-d938500c']:
            self.targets[ver] = 'http://www.winkde.org/pub/kde/ports/win32/repository/other/konversation-' + ver + '.tar.xz'
            self.targetInstSrc[ver] = 'konversation-' + ver
        self.patchToApply['1.3.1'] = ("konversation-1.3.1-20110822.diff", 1)
        self.patchToApply['1.4'] = [("konversation-1.4-20130305.diff", 1)]
        self.patchToApply['1.5-d938500c'] = [("konversation-1.5-d938500c-20130421.diff", 1), ("fix-opening-of-urls-on-windows.diff", 1)]
        self.svnTargets['gitHEAD'] = '[git]kde:konversation'
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.dependencies['kde/kde-runtime'] = 'default'
        self.dependencies['kdesupport/qca'] = 'default'
        self.dependencies['kde/kdepimlibs'] = 'default'
        self.shortDescription = "a KDE based irc client"

class Package(CMakePackageBase):
    def __init__( self):
        self.subinfo = subinfo()
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.defines = "-DBUILD_doc=OFF "

if __name__ == '__main__':
    Package().execute()
