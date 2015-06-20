import info

class subinfo( info.infoclass ):
    def setDependencies( self ):
        self.buildDependencies[ 'virtual/base' ] = 'default'
        self.buildDependencies[ 'dev-util/upx' ] = 'default'

    def setTargets( self ):
        self.svnTargets[ 'gitHEAD' ] = '[git]kde:automoc|no-qt|'
        for ver in ['20130507']:
            self.targets[ ver ] = "http://www.winkde.org/pub/kde/ports/win32/repository/other/automoc-" + ver + ".tar.xz"
            self.targetInstSrc[ ver ] = "automoc-" + ver
        self.defaultTarget = 'gitHEAD'

    def setBuildOptions( self ):
        self.disableHostBuild = False
        self.disableTargetBuild = True

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        #self.subinfo.options.package.version = "20130507"

if __name__ == '__main__':
    Package().execute()
