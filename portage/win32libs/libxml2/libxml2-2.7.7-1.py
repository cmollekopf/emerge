import shutil
import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets( self ):
        for ver in ['2.7.7', '2.7.8','2.8.0']:
            self.targets[ver] = 'ftp://xmlsoft.org/libxml2/libxml2-' + ver + '.tar.gz'
            self.targetInstSrc[ver] = 'libxml2-' + ver
        self.patchToApply['2.7.7'] = [("libxml2-2.7.7-20110406.diff", 1),
                                     ("fix-mingw-catalog.diff", 0)]
        self.targetDigests['2.7.7'] = '8592824a2788574a172cbddcdc72f734ff87abe3'
        self.patchToApply['2.7.8'] = [("libxml2-2.7.8-20110105.diff", 1),
                                      ("fix-mingw-catalog.diff", 0)]
        self.targetDigests['2.7.8'] = '859dd535edbb851cc15b64740ee06551a7a17d40'
        self.patchToApply['2.8.0'] = [("libxml2-2.8.0-20110105.diff", 1),
                                     ("fix-mingw-catalog.diff", 0)]
        self.targetDigests['2.8.0'] = 'a0c553bd51ba79ab6fff26dc700004c6a41f5250'
        self.shortDescription = "XML C parser and toolkit (runtime and applications)"

        self.defaultTarget = '2.7.7'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.dependencies['win32libs/zlib'] = 'default'
        self.dependencies['win32libs/win_iconv'] = 'default'

    def setBuildOptions( self ):
        self.disableHostBuild = False
        self.disableTargetBuild = False

class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.package.packageName = 'libxml2'
        self.subinfo.options.configure.defines = "-DBUILD_tests=OFF"


if __name__ == '__main__':
    Package().execute()

