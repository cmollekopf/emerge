import info
import kdedefaults as kd

class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]https://git.kolab.org/diffusion/KP/kdepim|kolab/integration/4.13.0|'
        for ver in ['0', '1', '2', '3', '4', '5']:
            self.targets[kd.kdeversion + ver] = "http://download.kde.org/stable/" + kd.kdeversion + ver + "/src/" + self.package + "-" + kd.kdeversion + ver + ".tar.xz"
            self.targetInstSrc[kd.kdeversion + ver] = self.package + '-' + kd.kdeversion + ver
            self.targetDigestUrls[ kd.kdeversion + ver  ] = 'http://download.kde.org/stable/' + kd.kdeversion + ver + '/src/' + self.package + '-' + kd.kdeversion + ver + '.tar.xz.sha1'
            self.patchToApply[kd.kdeversion + ver] = [('fix_introduction_screen.diff', 1),  # not to be upstreamed, this is an ugly hack, the fix is somewhere else (ref. bug 302342)
                                                      ('0001-fixed-windows-x64-build.patch', 1),# reverted upstream (does not compile on Linux)
                                                      ('0002-fixed-windows-x64-build.patch', 1),
                                                      ("fixknote.diff",1)] #this needs some review

        self.defaultTarget = 'gitHEAD'

        self.patchToApply['gitHEAD'] = [('fix_introduction_screen.diff', 1),
                                        ('0001-fixed-windows-x64-build.patch', 1)]

    def setDependencies( self ):
        self.runtimeDependencies['kde/kde-runtime'] = 'default'
        self.runtimeDependencies['kde/kdepim-runtime'] = 'default'
        self.dependencies['kde/kdepimlibs'] = 'default'
        self.dependencies['kdesupport/grantlee'] = 'default'
        self.dependencies['kde/baloo'] = 'default'
        self.shortDescription = "KDE's Personal Information Management suite"

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = ""
        self.subinfo.options.configure.defines += " -DKDE4_BUILD_TESTS=OFF"
        self.subinfo.options.configure.defines += ( " -DKDEPIM_BUILD_MOBILE=FALSE -DKDEPIM_MOBILE_UI=FALSE -DDISABLE_ALL_OPTIONAL_SUBDIRECTORIES=TRUE"
                  " -DBUILD_korganizer=TRUE -DBUILD_kmail=TRUE -DBUILD_korgac=TRUE -DBUILD_kaddressbook=TRUE"
                  " -DBUILD_kontact=TRUE -DBUILD_kaddressbook=TRUE -DBUILD_doc=TRUE -DBUILD_akonadiconsole=TRUE"
                  " -DBUILD_messagecomposer=TRUE -DBUILD_mailimporter=TRUE -DBUILD_sieveeditor=TRUE -DBUILD_importwizard=TRUE"
                  " -DBUILD_agents=TRUE -DBUILD_sendlateragent=TRUE -DBUILD_archivemailagent=TRUE -DBUILD_mailfilteragent=TRUE"
                  " -DBUILD_kleopatra=TRUE -DDISABLE_ALL_OPTIONAL_PLUGINS=TRUE" )


if __name__ == '__main__':
    Package().execute()
