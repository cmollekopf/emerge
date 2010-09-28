import utils
import info
from Package.CMakePackageBase import *

# see http://wiki.mozilla.org/LDAP_C_SDK_SASL_Windows

class subinfo(info.infoclass):
    def setTargets( self ):
        self.targets['2.1.22'] = 'ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/cyrus-sasl-2.1.22.tar.gz'
        self.targetInstSrc['2.1.22'] = 'cyrus-sasl-2.1.22'
        self.patchToApply['2.1.22'] = ( 'cyrus-sasl-2.1.22.patch', 1 )
        self.defaultTarget = '2.1.22'

    def setDependencies( self ):
        self.hardDependencies['virtual/base'] = 'default'
        if platform.isCrossCompilingEnabled():
            self.hardDependencies['win32libs-sources/wcecompat-src'] = 'default'

class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        self.subinfo.options.package.withCompiler = None
#        self.subinfo.options.configure.defines = "-DSTATIC_LIBRARY=OFF"
        CMakePackageBase.__init__( self )

if __name__ == '__main__':
    Package().execute()
