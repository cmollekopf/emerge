import info
import os

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.gitTargets[ 'gitHEAD' ] = '[git]kde:rkward'
        for ver in ['0.5.7', '0.6.0', '0.6.1', '0.6.2']:
            self.targets[ver] = 'http://downloads.sourceforge.net/rkward/rkward-' + ver + '.tar.gz'
            self.targetInstSrc[ ver] = 'rkward-' + ver
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.dependencies[ 'testing/r-base' ] = 'default'
        self.dependencies[ 'kde/kate' ] = 'default'  # provides katepart; runtime
        self.dependencies[ 'kde/okular' ] = 'default'  # not strictly required, but useful for print preview; runtime

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        r_executable = os.path.join( self.mergeDestinationDir(), "lib", "R", "bin", "R.exe" )
        self.subinfo.options.configure.defines = " -DR_EXECUTABLE=" + r_executable.replace( "\\\\", "/" )

if __name__ == '__main__':
    Package().execute()

