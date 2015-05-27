import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]https://git.kolab.org/diffusion/KB/baloo.git|kolab/integration/4.13.0|'
        self.shortDescription = "the next generation nepomuk"
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.dependencies['kde/kdelibs'] = 'default'
        self.dependencies['kde/kdepimlibs'] = 'default'
        self.dependencies['kde/kfilemetadata'] = 'default'
        self.dependencies['testing/xapian'] = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__(self)

if __name__ == '__main__':
    Package().execute()
