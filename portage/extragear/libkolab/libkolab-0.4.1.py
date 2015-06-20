# -*- coding: utf-8 -*-
import info
import utils
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets( self ):
        for ver in [ '0.4.1', '0.5.0' ]:
            self.targets[ ver ] = 'http://mirror.kolabsys.com/pub/releases/libkolab-' + ver + '.tar.gz'
            self.targetInstSrc[ ver ] = "libkolab-" + ver
        self.patchToApply['0.4.1'] = [("libkolab-fixes.diff", 1)]
        # self.patchToApply['0.5.0'] = [("libkolab-0.5.0-fixes.diff", 1)]
        self.svnTargets['gitHEAD'] = '[git]http://git.kolab.org/diffusion/LK/libkolab'

        self.shortDescription = ''
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.buildDependencies['win32libs/libkolabxml'] = 'default'

        # the following dependencies are dragged in by the static libkolabxml library
        self.dependencies['binary/xerces-c-bin'] = 'default'
        self.dependencies['win32libs/boost-system'] = 'default'
        self.dependencies['win32libs/boost-thread'] = 'default'

        # this is a real dependency of libkolab
        self.dependencies['kde/kdepimlibs'] = 'default'

class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = "-DBUILD_TESTS=OFF -DBUILD_TOOLS=OFF -DMAKE_KOLAB_LIB"

if __name__ == '__main__':
    Package().execute()
