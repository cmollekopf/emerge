# -*- coding: utf-8 -*-
import info
import utils
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets( self ):
        for ver in [ '0.8.2', '0.8.4','1.0.1']:
            self.targets[ ver ] = 'http://git.kolab.org/libkolabxml/snapshot/libkolabxml-' + ver + '.tar.gz'
            self.targetInstSrc[ ver ] = "libkolabxml-" + ver
        self.svnTargets['gitHEAD'] = '[git]http://git.kolab.org/libkolabxml'
        self.patchToApply['0.8.2'] = [("libkolabxml-fixes.diff", 1)]
        self.patchToApply['0.8.4'] = [("libkolabxml-fixes.diff", 1)]
        self.patchToApply['1.0.1'] = [("libkolabxml-1.0.1-fixes.diff", 1)]
        self.patchToApply['gitHEAD'] = [("libkolabxml-1.0.1-fixes.diff", 1)]

        self.shortDescription = 'Kolab XML Format Schema Definitions Library'
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.buildDependencies['binary/xsd'] = 'default'
        self.buildDependencies['win32libs/xerces-c'] = 'default'

        # the following dependencies are runtime dependencies for packages linking to the static! libkolabxml
        self.dependencies['win32libs/boost-thread'] = 'default'
        self.dependencies['win32libs/boost-system'] = 'default'
        self.dependencies['win32libs/libcurl'] = 'default'

class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = "-DBUILD_TESTS=OFF"

if __name__ == '__main__':
    Package().execute()
