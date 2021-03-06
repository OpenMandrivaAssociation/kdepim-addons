Summary:	Add-Ons for the KDE PIM suite
Name:		kdepim-addons
Version:	21.04.2
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	sasl-devel
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5WebEngineViewer)
BuildRequires:	cmake(KF5TemplateParser)
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:	cmake(KF5KaddressbookGrantlee)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5KaddressbookImportExport)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5IncidenceEditor)
BuildRequires:	cmake(KF5MessageCore)
BuildRequires:	cmake(KF5MessageComposer)
BuildRequires:	cmake(KF5MessageList)
BuildRequires:	cmake(KF5CalendarSupport)
BuildRequires:	cmake(KF5EventViews)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiCalendar)
BuildRequires:	cmake(KF5Gravatar)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5LibKSieve)
BuildRequires:	cmake(KF5Tnef)
BuildRequires:	cmake(KF5MailTransportAkonadi)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KPimImportWizard)
BuildRequires:	cmake(KPimAddressbookImportExport)
BuildRequires:	cmake(KPimImportWizard)
BuildRequires:	cmake(KF5MailImporterAkonadi)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(KPimPkPass)
BuildRequires:	cmake(KPimItinerary)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(libmarkdown)
Conflicts:	kmail <= 3:16.04.3-2

%description
Add-Ons for the KDE PIM suite.

%files -f %{name}.lang
%{_datadir}/messageviewerplugins/externalscriptexample.desktop
%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins
%{_datadir}/qtcreator/templates/kmaileditorplugins
%{_datadir}/qlogging-categories5/kdepim-addons.categories
%{_datadir}/qlogging-categories5/kdepim-addons.renamecategories
%{_sysconfdir}/xdg/kmail.antispamrc
%{_sysconfdir}/xdg/kmail.antivirusrc
%{_bindir}/kmail_antivir.sh
%{_bindir}/kmail_clamav.sh
%{_bindir}/kmail_fprot.sh
%{_bindir}/kmail_sav.sh
# (tpg) these libs should be splitted into separate subpackages ?
# (bero) let's not do it until either something else starts using them
# (which is not going to happen given make install doesn't even install
# headers...) or they become optional here.
# No point in splitting a package if both sides are useless without
# the other...
%{_libdir}/libkaddressbookmergelibprivate.so.5*
%{_libdir}/libshorturlpluginprivate.so.5*
%{_libdir}/libadblocklibprivate.so.5*
%{_libdir}/libexpireaccounttrashfolderconfig.so.5*
%{_libdir}/libfolderconfiguresettings.so.5*
%{_libdir}/libgrammarcommon.so.5*
%{_libdir}/libkmailgrammalecte.so.5*
%{_libdir}/libkmaillanguagetool.so.5*
%{_libdir}/libkmailmarkdown.so.5*
%{_libdir}/libdkimverifyconfigure.so.5*
%{_libdir}/libkmailquicktextpluginprivate.so.5*
%{_libdir}/contacteditor
%{_libdir}/qt5/plugins/akonadi/*.so
%{_libdir}/qt5/plugins/importwizard/*.so
%{_libdir}/qt5/plugins/kaddressbook/importexportplugin
%{_libdir}/qt5/plugins/korg_datenums.so
%{_libdir}/qt5/plugins/korg_picoftheday.so
%{_libdir}/qt5/plugins/korg_thisdayinhistory.so
%{_libdir}/qt5/plugins/messageviewer/bodypartformatter
%{_libdir}/qt5/plugins/plasmacalendarplugins/*.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%{_libdir}/qt5/plugins/libksieve
%{_libdir}/qt5/plugins/mailtransport
%{_libdir}/qt5/plugins/messageviewer/grantlee/*/kitinerary_grantlee_extension.so
%{_libdir}/qt5/plugins/templateparser
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/qmldir
%{_datadir}/kservices5/korganizer/datenums.desktop
%{_datadir}/kservices5/korganizer/picoftheday.desktop
%{_datadir}/kservices5/korganizer/thisdayinhistory.desktop
%{_datadir}/kconf_update/webengineurlinterceptoradblock.upd
%{_datadir}/kconf_update/languagetool_kmail.upd
%{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_checkgravatarplugin.so
%{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_mergecontactsplugin.so
%{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_searchduplicatesplugin.so
%{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_sendmailplugin.so
%{_libdir}/qt5/plugins/kaddressbook/mainview/kaddressbook_sendvcardsplugin.so
%{_libdir}/qt5/plugins/kmail/mainview/kmail_antispamplugin.so
%{_libdir}/qt5/plugins/kmail/mainview/kmail_antivirusplugin.so
%{_libdir}/qt5/plugins/kmail/mainview/kmail_expertplugin.so
%{_libdir}/qt5/plugins/kmail/mainview/kmail_logactivitiesplugin.so
%{_libdir}/qt5/plugins/kmail/plugincheckbeforesend/kmail_automaticaddcontactseditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugincheckbeforesend/kmail_checkbeforesendeditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugincheckbeforesend/kmail_confirmaddresseditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_autocorrectioneditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_changecaseeditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_insertemaileditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_insertshorturleditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_insertspecialcharactereditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_nonbreakingspaceeditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_quicktextplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_sharetexteditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditor/kmail_zoomtexteditorplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditorconverttext/kmail_markdownplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditorgrammar/kmail_grammalecteplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditorgrammar/kmail_languagetoolplugin.so
%{_libdir}/qt5/plugins/kmail/plugineditorinit/kmail_externalcomposereditorplugin.so
%{_libdir}/qt5/plugins/messageviewer
%{_libdir}/qt5/plugins/pimcommon
%{_libdir}/qt5/plugins/webengineviewer

%prep
%autosetup -p1
%cmake_kde5 \
	-DKDEPIMADDONS_BUILD_EXAMPLES:BOOL=true

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
