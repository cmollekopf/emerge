import os
import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        for ver in ['4.13.0', '4.13.1', '4.13.2', '4.13.3', '4.13.4', '4.13.0.0']:
          self.targets[ ver] = 'http://download.kde.org/stable/%s/src/kde-l10n/kde-l10n-de-%s.tar.xz' % (ver , ver )
          self.targetInstSrc[ ver] = 'kde-l10n-de-%s'  % ver
          self.svnTargets['4.13.0.0'] = '[git]git@github.com:kolab-groupware/kde-l10n-de.git|kolab/integration/4.13.0|'

        self.defaultTarget = '4.13.0.0'


    def setDependencies( self ):
        self.buildDependencies['dev-util/cmake'] = 'default'
        self.buildDependencies['kde/kdelibs'] = 'default'
        self.buildDependencies['dev-util/gettext-tools'] = 'default'


from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )


if __name__ == '__main__':
    Package().execute()
