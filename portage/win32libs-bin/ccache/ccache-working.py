# This package-script is automatically updated by the script win32libsupdater.py
# which can be found in your emerge/bin folder. To update this package, run
# win32libsupdater.py (and commit the results)
# based on revision gita7c2a11bea1203153d7f09b40c407a5c63b464d3

from Package.BinaryPackageBase import *
import os
import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        repoUrl = 'http://downloads.sourceforge.net/kde-windows'

        for version in [ 'working' ]:
            self.targets[ version ]          = self.getPackage( repoUrl, 'ccache', version , packagetypes=['bin'] )
            self.targetDigestUrls[ version ] = self.getPackage( repoUrl, 'ccache', version, '.tar.bz2.sha1' , packagetypes=['bin'] )

        self.shortDescription = 'ccache is a compiler cache. It speeds up recompilation by caching previous compilations and detecting when the same compilation is being done again. Supported languages are C, C++, Objective-C and Objective-C++.'

        self.defaultTarget = 'working'


    def setDependencies( self ):
        if not utils.envAsBool( 'EMERGE_ENABLE_IMPLICID_BUILDTIME_DEPENDENCIES' ):
            self.buildDependencies[ 'virtual/bin-base' ] = 'default'


    def setBuildOptions( self ):
        self.disableHostBuild = False
        self.disableTargetBuild = True

class Package(BinaryPackageBase):
  def __init__(self):
    self.subinfo = subinfo()
    BinaryPackageBase.__init__( self )

if __name__ == '__main__':
    Package().execute()