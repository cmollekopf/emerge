; basic script template for NullsoftInstallerPackager
;
; Copyright 2013 Patrick von Reth <vonreth@kde.org>
; Copyright 2010 Patrick Spendrin <ps_ml@gmx.de>
; adapted from marble.nsi

; depends on http://nsis.sourceforge.net/WinShell_plug-in
var ToBeRunned
var nameOfToBeRunend

; registry stuff
!define regkey "Software\${company}\${productname}"
!define uninstkey "Software\Microsoft\Windows\CurrentVersion\Uninstall\Quassel"
 
!define startmenu "$SMPROGRAMS\${productname}"
!define uninstaller "uninstall.exe"

Var StartMenuFolder
 
!define PRODUCT_WEB_SITE http://quassel-irc.org/
!define MyApp_AppUserModelId  QuasselProject.QuasselIRC

;Start Menu Folder Page Configuration
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKLM" 
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${regkey}" 
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Start Menu Folder"

InstType "Minimal"
InstType "Full"
;--------------------------------
 

XPStyle on
ShowInstDetails hide
ShowUninstDetails hide

SetCompressor /SOLID lzma
 
Name "${productname}"
Caption "${productname} ${version}"
 
OutFile "${setupname}"
!include "MUI2.nsh"
!include "LogicLib.nsh"

!define MUI_ICON quassel.ico

!insertmacro MUI_PAGE_WELCOME

;!insertmacro MUI_PAGE_LICENSE
${license}
;!insertmacro MUI_PAGE_LICENSE

!insertmacro MUI_PAGE_DIRECTORY

!insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder

!define MUI_COMPONENTSPAGE_NODESC
!insertmacro MUI_PAGE_COMPONENTS

!insertmacro MUI_PAGE_INSTFILES

!define MUI_FINISHPAGE_RUN $ToBeRunned
!define MUI_FINISHPAGE_RUN_TEXT $nameOfToBeRunend
!define MUI_FINISHPAGE_LINK "Visit project homepage"
!define MUI_FINISHPAGE_LINK_LOCATION "${PRODUCT_WEB_SITE}"
!insertmacro MUI_PAGE_FINISH

;uninstaller
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH
;-------

!insertmacro MUI_LANGUAGE "English"
 
SetDateSave on
SetDatablockOptimize on
CRCCheck on
SilentInstall normal
 
InstallDir "$PROGRAMFILES\${productname}"
InstallDirRegKey HKLM "${regkey}" ""
 

 
;--------------------------------
 
AutoCloseWindow false
 
 
; beginning (invisible) section
Section "--hidden Quassel Base" QUASSEL_BASE
   SectionIn RO
   SetOutPath $INSTDIR
   SetShellVarContext all
   StrCpy $ToBeRunned ""
    
    WriteRegStr HKLM "${regkey}" "Install_Dir" "$INSTDIR"
    WriteRegStr HKLM "${regkey}" "Version" "${version}"
    WriteRegStr HKLM "${regkey}" "" "$INSTDIR\uninstall.exe"
    
    WriteRegStr HKLM "${uninstkey}" "DisplayName" "Quassel (remove only)"
    WriteRegStr HKLM "${uninstkey}" "DisplayIcon" "$INSTDIR\${MUI_ICON}"
    WriteRegStr HKLM "${uninstkey}" "DisplayVersion" "${version}"
    WriteRegStr HKLM "${uninstkey}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
    WriteRegStr HKLM "${uninstkey}" "UninstallString" '"$INSTDIR\${uninstaller}"'
    WriteRegStr HKLM "${uninstkey}" "Publisher" "${company}"
 
  SetOutPath $INSTDIR
 
 
    ; package all files, recursively, preserving attributes
    ; assume files are in the correct places

    File /a /r /x "*.nsi" /x "*quassel.exe" /x "*quasselclient.exe" /x "*quasselcore.exe" /x "${setupname}" "${srcdir}\*.*" 
    File /a  ${MUI_ICON}

    WriteUninstaller "${uninstaller}"
    
    ;Create shortcuts
    !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
        CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
        CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd


Section "Quassel"  QUASSEL_ALL_IN_ONE
    SectionIn 1 2
    SetOutPath $INSTDIR
    StrCpy $ToBeRunned "$INSTDIR\bin\quassel.exe"
    StrCpy $nameOfToBeRunend "Run Quassel"
    File /a /oname=bin\quassel.exe "${srcdir}\bin\quassel.exe"
    !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
        CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Quassel.lnk" "$INSTDIR\bin\quassel.exe"
        WinShell::SetLnkAUMI "$SMPROGRAMS\$StartMenuFolder\Quassel.lnk" "${MyApp_AppUserModelId}"
    !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section /o "QuasselClient"  QUASSEL_CLIENT
    SectionIn 2
    SetOutPath $INSTDIR
    ${If} $ToBeRunned == ""
        StrCpy $ToBeRunned "$INSTDIR\bin\quasselclient.exe"
        StrCpy $nameOfToBeRunend "Run QuasselClient"
    ${Endif}
    File /a /oname=bin\quasselclient.exe "${srcdir}\bin\quasselclient.exe"
    !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
        CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Quassel Client.lnk" "$INSTDIR\bin\quasselclient.exe"
        WinShell::SetLnkAUMI "$SMPROGRAMS\$StartMenuFolder\Quassel Client.lnk" "${MyApp_AppUserModelId}"
    !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section /o "QuasselCore"  QUASSEL_CORE
    SectionIn 2
    SetOutPath $INSTDIR
    ${If} $ToBeRunned == ""
        StrCpy $ToBeRunned "$INSTDIR\bin\quasselcore.exe"
        StrCpy $nameOfToBeRunend "Run QuasselCore"
    ${Endif}
     File /a /oname=bin\quasselcore.exe "${srcdir}\bin\quasselcore.exe"
    !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
        CreateShortCut "$SMPROGRAMS\$StartMenuFolder\Quassel Core.lnk" "$INSTDIR\bin\quasselcore.exe"
    !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

; Section /o "QuasselCoreService"  QUASSEL_CORE_SERVICE
    ; SimpleSC::ExistsService "QuasselCore"
    ; Pop $0 ; returns an errorcode if the service doesn�t exists (<>0)/service exists (0)
    ; ${If} $0 == 0
        ; MessageBox MB_OK|MB_ICONSTOP "Install Service QUassel failed - Reason: Service already exists"
    ; ${Else}
        ; SimpleSC::InstallService "QuasselCore" "QuasselCore" "16" "2" "$INSTDIR\bin\quasselcore.exe" "" "" ""
        ; Pop $0 ; returns an errorcode (<>0) otherwise success (0)
            ; ${If} $0 != 0
                ; Push $0
                ; SimpleSC::GetErrorMessage
                ; Pop $0
                ; MessageBox MB_OK|MB_ICONSTOP "Install of Service QUassel failed - Reason: $0"
            ; ${Else}
                ; SimpleSC::StartService "QuasselCore" "" 30
                ; Pop $0 ; returns an errorcode (<>0) otherwise success (0)
                ; ${If} $0 != 0
                    ; Push $0
                    ; SimpleSC::GetErrorMessage
                    ; Pop $0
                    ; MessageBox MB_OK|MB_ICONSTOP "Install of Service QUassel failed - Reason: $0"
                ; ${EndIf}
            ; ${EndIf}
    ; ${EndIf}
; SectionEnd

; Uninstaller
; All section names prefixed by "Un" will be in the uninstaller
 
UninstallText "This will uninstall Quassel."
 

Section "Uninstall"
    SetShellVarContext all
    SetShellVarContext all

    DeleteRegKey HKLM "${uninstkey}"
    DeleteRegKey HKLM "${regkey}"

    !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuFolder


    
  ; SimpleSC::ExistsService "QuasselCore"
  ; Pop $0   ; returns an errorcode if the service doesn�t exists (<>0)/service exists (0)
  ; ${If} $0 == 0
    ; SimpleSC::ServiceIsStopped "QuasselCore"
    ; Pop $0 ; returns an errorcode (<>0) otherwise success (0)
    ; Pop $1 ; returns 1 (service is stopped) - returns 0 (service is not stopped)
    ; ${If} $0 == 0 
    ; ${AndIf} $1 == 0
        ; SimpleSC::StopService "QuasselCore" 1 30
        ; Pop $0 ; returns an errorcode (<>0) otherwise success (0)
        ; ${If} $0 != 0
            ; Push $0
            ; SimpleSC::GetErrorMessage
            ; Pop $0
            ; MessageBox MB_OK|MB_ICONSTOP "Stopping failed - Reason: $0"
        ; ${Else}
             ; SimpleSC::RemoveService "QuasselCore"
             ; Pop $0 ; returns an errorcode (<>0) otherwise success (0)
             ; ${If} $0 != 0  
                    ; Push $0
                    ; SimpleSC::GetErrorMessage
                    ; Pop $0
                    ; MessageBox MB_OK|MB_ICONSTOP "Remove fails - Reason: $0"
                ; ${EndIf}
        ; ${EndIf}
    ; ${EndIf}
  ; ${EndIf}
    
    WinShell::UninstAppUserModelId ""${MyApp_AppUserModelId}"
    WinShell::UninstShortcut "$SMPROGRAMS\$StartMenuFolder\Quassel Client.lnk"
    WinShell::UninstShortcut "$SMPROGRAMS\$StartMenuFolder\Quassel.lnk"
  
    RMDir /r "$SMPROGRAMS\$StartMenuFolder"
    RMDir /r "$INSTDIR"
SectionEnd

Function .onSelChange
    ${If} ${SectionIsSelected} ${QUASSEL_CORE}
    ${OrIf}  ${SectionIsSelected} ${QUASSEL_CLIENT}
    ${OrIf}  ${SectionIsSelected} ${QUASSEL_ALL_IN_ONE}
        GetDlgItem $0 $HWNDPARENT 1
        EnableWindow $0 1
    ${Else}
        GetDlgItem $0 $HWNDPARENT 1
        EnableWindow $0 0
    ${EndIf}
FunctionEnd
