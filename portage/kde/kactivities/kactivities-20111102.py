import info
import kdedefaults as kd

class subinfo(info.infoclass):
    def setTargets( self ):
        # self.svnTargets['gitHEAD'] = '[git]kde:%s|%s|' % (self.package, kd.kdebranch)
        self.svnTargets['gitHEAD'] = '[git]https://github.com/kolab-groupware/kactivities.git|kolab/integration/4.13.0|'
        for ver in ['0', '1', '2', '3', '4', '5']:
            self.targets[kd.kdeversion + ver] = "http://download.kde.org/stable/" + kd.kdeversion + ver + "/src/" + self.package + "-" + kd.kdeversion + ver + ".tar.xz"
            self.targetInstSrc[kd.kdeversion + ver] = self.package + '-' + kd.kdeversion + ver
            self.targetDigestUrls[ kd.kdeversion + ver  ] = 'http://download.kde.org/stable/' + kd.kdeversion + ver + '/src/' + self.package + '-' + kd.kdeversion + ver + '.tar.xz.sha1'
            # see https://git.reviewboard.kde.org/r/114098/
            self.patchToApply[kd.kdeversion + ver] = [("make-declarative-plugin-a-plugin-4.10.2.diff", 1)]
        self.patchToApply['gitHEAD'] = [("make-declarative-plugin-a-plugin-4.10.2.diff", 1)]

        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.dependencies['kde/kdelibs'] = 'default'
        self.shortDescription = "KDE Activity Manager"

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__(self)

if __name__ == '__main__':
    Package().execute()
