Summary:	Add-Ons for the KDE PIM suite
Name:		kdepim-addons
Version:	23.08.5
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
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
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Prison)
BuildRequires:	cmake(KF5Holidays)
BuildRequires:	cmake(KPim5Libkleo)
BuildRequires:	cmake(KPim5CalendarUtils)
BuildRequires:	cmake(KPim5MailCommon)
BuildRequires:	cmake(KPim5AddressbookImportExport)
BuildRequires:	cmake(KPim5GrantleeTheme)
BuildRequires:	cmake(KPim5PimCommonAkonadi)
BuildRequires:	cmake(KPim5IncidenceEditor)
BuildRequires:	cmake(KPim5AkonadiNotes)
BuildRequires:	cmake(KPim5MessageCore)
BuildRequires:	cmake(KPim5MessageComposer)
BuildRequires:	cmake(KPim5MessageList)
BuildRequires:	cmake(KPim5MessageViewer)
BuildRequires:	cmake(KPim5TemplateParser)
BuildRequires:	cmake(KPim5WebEngineViewer)
BuildRequires:	cmake(KF5TextGrammarCheck)
BuildRequires:	cmake(KF5TextTranslator)
BuildRequires:	cmake(KF5CalendarSupport)
BuildRequires:	cmake(KPim5EventViews)
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5AkonadiCalendar)
BuildRequires:	cmake(KPim5Gravatar)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KPim5IdentityManagement)
BuildRequires:	cmake(KPim5IMAP)
BuildRequires:	cmake(KPim5LibKSieve)
BuildRequires:	cmake(KPim5Tnef)
BuildRequires:	cmake(KPim5MailTransport)
BuildRequires:	cmake(KPim5AkonadiContact)
BuildRequires:	cmake(KPimImportWizard)
BuildRequires:	cmake(KPimAddressbookImportExport)
BuildRequires:	cmake(KPimImportWizard)
BuildRequires:	cmake(KPim5MailImporterAkonadi)
BuildRequires:	cmake(KPim5KontactInterface)
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
%{_libdir}/libkmailconfirmbeforedeleting.so.*
%{_libdir}/libkmailmarkdown.so.5*
%{_libdir}/libdkimverifyconfigure.so.5*
%{_libdir}/libkmailquicktextpluginprivate.so.5*
%{_libdir}/qt5/plugins/pim5/akonadi/*.so
%{_libdir}/qt5/plugins/pim5/importwizard/*.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/importexportplugin
%{_libdir}/qt5/plugins/pim5/korganizer/datenums.so
%{_libdir}/qt5/plugins/pim5/korganizer/picoftheday.so
%{_libdir}/qt5/plugins/pim5/korganizer/thisdayinhistory.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/*.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%{_libdir}/qt5/plugins/pim5/libksieve
%{_libdir}/qt5/plugins/pim5/templateparser
%{_libdir}/qt5/plugins/pim5/mailtransport/mailtransport_sendplugin.so
%{_libdir}/libopenurlwithconfigure.so.5*
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/qmldir
%{_datadir}/kconf_update/webengineurlinterceptoradblock.upd
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_checkgravatarplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_mergecontactsplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_searchduplicatesplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_sendmailplugin.so
%{_libdir}/qt5/plugins/pim5/kaddressbook/mainview/kaddressbook_sendvcardsplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_antispamplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_antivirusplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_expertplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugincheckbeforesend/kmail_automaticaddcontactseditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugincheckbeforesend/kmail_checkbeforesendeditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugincheckbeforesend/kmail_confirmaddresseditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_autocorrectioneditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_changecaseeditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_insertemaileditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_insertshorturleditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_insertspecialcharactereditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_nonbreakingspaceeditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_quicktextplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_sharetexteditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditor/kmail_zoomtexteditorplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorconverttext/kmail_markdownplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorgrammar/kmail_grammalecteplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorgrammar/kmail_languagetoolplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/plugineditorinit/kmail_externalcomposereditorplugin.so
%{_libdir}/qt5/plugins/pim5/messageviewer
%{_libdir}/qt5/plugins/pim5/pimcommon
%{_libdir}/qt5/plugins/pim5/webengineviewer
%{_libdir}/libscamconfiguresettings.so.5*
%{_libdir}/qt5/plugins/pim5/korganizer/lunarphases.so
%{_datadir}/icons/hicolor/scalable/status/moon-phase-first-quarter.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-full.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-last-quarter.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-new.svg
%{_libdir}/libakonadidatasetools.so.5*
%{_libdir}/qt5/plugins/pim5/contacteditor/editorpageplugins/cryptopageplugin.so
%{_libdir}/qt5/plugins/pim5/kmail/mainview/kmail_akonadidatabasetoolplugin.so

%prep
%autosetup -p1
%cmake_kde5 \
	-DKDEPIMADDONS_BUILD_EXAMPLES:BOOL=true

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
