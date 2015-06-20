import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.targets['1.2.21'] = 'http://oligarchy.co.uk/xapian/1.2.21/xapian-core-1.2.21.tar.xz'
        self.targetInstSrc['1.2.21'] = 'xapian-core-1.2.21'
        self.patchToApply['1.2.21'] = [('xapian-core-1.2.16-20131221.diff', 1)]
        self.defaultTarget = '1.2.21'

    def setDependencies( self ):
        self.dependencies['win32libs/zlib'] = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__(self)

if __name__ == '__main__':
    Package().execute()
