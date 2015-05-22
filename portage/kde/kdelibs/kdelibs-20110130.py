import info
import kdedefaults as kd

class subinfo(info.infoclass):
    def setTargets( self ):
#        self.patchToApply['gitHEAD'] = [("kde.conf-extended-fix.diff", 1),
#                                        ("fix-dir-separator.diff", 1)]
        self.svnTargets['gitHEAD'] = '[git]https://github.com/kolab-groupware/kdelibs|kolab/integration/4.14.0|'
        self.shortDescription = "The KDE Library"
        self.defaultTarget = 'gitHEAD'


    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.buildDependencies['dev-util/perl'] = 'default'
        self.buildDependencies['win32libs/automoc'] = 'default'
        #self.dependencies['kdesupport/hupnp'] = 'default'
        self.dependencies['kdesupport/kdewin'] = 'default'
        self.dependencies['kdesupport/phonon'] = 'default'
        self.dependencies['kdesupport/attica'] = 'default'
        self.dependencies['kdesupport/dbusmenu-qt'] = 'default'
        self.dependencies['kdesupport/grantlee'] = 'default'
        self.dependencies['kdesupport/qca'] = 'default'
        self.dependencies['kdesupport/qimageblitz'] = 'default'
        self.dependencies['data/docbook-xsl'] = 'default'
        self.dependencies['data/shared-desktop-ontologies'] = 'default'
        if self.options.features.phononBackend.vlc:
            self.runtimeDependencies['kdesupport/phonon-vlc'] = 'default'
        elif self.options.features.phononBackend.ds9:
            self.runtimeDependencies['kdesupport/phonon-ds9'] = 'default'
        self.dependencies['win32libs/aspell']  = 'default'
#        self.dependencies['win32libs/enchant']  = 'default'
        self.dependencies['win32libs/gettext']  = 'default'
        self.dependencies['win32libs/giflib']  = 'default'
#        self.dependencies['win32libs/gssapi']  = 'default'
#        self.dependencies['win32libs/hspell']  = 'default'
        if not emergePlatform.isCrossCompilingEnabled():
            self.dependencies['win32libs/jasper']  = 'default'
        self.dependencies['win32libs/jpeg']  = 'default'
        self.dependencies['win32libs/libbzip2']  = 'default'
        self.dependencies['win32libs/libpng']  = 'default'
        self.dependencies['win32libs/libxml2']  = 'default'
        self.dependencies['win32libs/libxslt']  = 'default'
#        self.dependencies['win32libs/openexr']  = 'default'
        self.dependencies['win32libs/openssl']  = 'default'
        self.dependencies['win32libs/pcre']  = 'default'
        self.dependencies['win32libs/shared-mime-info']  = 'default'
        self.dependencies['win32libs/zlib']  = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = ""
        if compiler.isMinGW():
          self.subinfo.options.configure.defines += " -DKDE_DISTRIBUTION_TEXT=\"MinGW %s\" " % compiler.getMinGWVersion()
        elif compiler.isMSVC():
          self.subinfo.options.configure.defines = " -DKDE_DISTRIBUTION_TEXT=\"%s\" " % compiler.getVersion()

    def install( self ):
        if not CMakePackageBase.install( self ):
            return False
        if compiler.isMinGW():
            manifest = os.path.join( self.packageDir(), "kconf_update.exe.manifest" )
            executable = os.path.join( self.installDir(), "bin", "kconf_update.exe" )
            utils.embedManifest( executable, manifest )
        return True

if __name__ == '__main__':
    Package().execute()
