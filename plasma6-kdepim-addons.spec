#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Add-Ons for the KDE PIM suite
Name:		plasma6-kdepim-addons
Version:	24.02.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kdepim-addons/-/archive/%{gitbranch}/kdepim-addons-%{gitbranchd}.tar.bz2#/kdepim-addons-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kdepim-addons-%{version}.tar.xz
%endif
BuildRequires:	sasl-devel
BuildRequires:	boost-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KPim6MailCommon)
BuildRequires:	cmake(KPim6GrantleeTheme)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(KPim6IncidenceEditor)
BuildRequires:	cmake(KPim6AkonadiNotes)
BuildRequires:	cmake(KPim6MessageCore)
BuildRequires:	cmake(KPim6MessageComposer)
BuildRequires:	cmake(KPim6MessageList)
BuildRequires:	cmake(KPim6MessageViewer)
BuildRequires:	cmake(KPim6TemplateParser)
BuildRequires:	cmake(KPim6WebEngineViewer)
BuildRequires:	cmake(KF6TextGrammarCheck)
BuildRequires:	cmake(KF6TextTranslator)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KF6TextAddonsWidgets)
BuildRequires:	cmake(KF6TextUtils)
BuildRequires:	cmake(KPim6CalendarSupport)
BuildRequires:	cmake(KPim6EventViews)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiCalendar)
BuildRequires:	cmake(KPim6Gravatar)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	%mklibname -d KPim6KSieve
BuildRequires:	cmake(KPim6Tnef)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KPim6ImportWizard)
BuildRequires:	cmake(KPim6AddressbookImportExport)
BuildRequires:	cmake(KPim6ImportWizard)
BuildRequires:	cmake(KPim6MailImporterAkonadi)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	cmake(KPimPkPass)
BuildRequires:	cmake(KPim6Itinerary)
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(libmarkdown)
Conflicts:	kmail <= 3:16.04.3-2

%description
Add-Ons for the KDE PIM suite.

%files -f %{name}.lang
%{_datadir}/messageviewerplugins/externalscriptexample.desktop
%{_datadir}/qtcreator/templates/kmaileditorconvertertextplugins
%{_datadir}/qlogging-categories6/kdepim-addons.categories
%{_datadir}/qlogging-categories6/kdepim-addons.renamecategories
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
%{_libdir}/libkaddressbookmergelibprivate.so.*
%{_libdir}/libshorturlpluginprivate.so.*
%{_libdir}/libexpireaccounttrashfolderconfig.so.*
%{_libdir}/libfolderconfiguresettings.so.*
%{_libdir}/libkmailconfirmbeforedeleting.so.*
%{_libdir}/libkmailmarkdown.so.*
%{_libdir}/libdkimverifyconfigure.so.*
%{_libdir}/libkmailquicktextpluginprivate.so.*
%{_libdir}/qt6/plugins/pim6/akonadi/*.so
%{_libdir}/qt6/plugins/pim6/importwizard/*.so
%{_libdir}/qt6/plugins/pim6/kaddressbook/importexportplugin
%{_libdir}/qt6/plugins/pim6/korganizer/datenums.so
%{_libdir}/qt6/plugins/pim6/korganizer/picoftheday.so
%{_libdir}/qt6/plugins/pim6/korganizer/thisdayinhistory.so
%{_libdir}/qt6/plugins/plasmacalendarplugins/*.so
%{_libdir}/qt6/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%{_libdir}/qt6/plugins/pim6/libksieve
%{_libdir}/qt6/plugins/pim6/templateparser
%{_libdir}/qt6/plugins/pim6/mailtransport/mailtransport_sendplugin.so
%{_libdir}/libopenurlwithconfigure.so.*
%{_libdir}/qt6/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/PimCalendars/qmldir
%{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_checkgravatarplugin.so
%{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_mergecontactsplugin.so
%{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_searchduplicatesplugin.so
%{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_sendmailplugin.so
%{_libdir}/qt6/plugins/pim6/kaddressbook/mainview/kaddressbook_sendvcardsplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_antispamplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_antivirusplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_expertplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugincheckbeforesend/kmail_automaticaddcontactseditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugincheckbeforesend/kmail_checkbeforesendeditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugincheckbeforesend/kmail_confirmaddresseditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_autocorrectioneditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_changecaseeditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_insertemaileditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_insertshorturleditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_insertspecialcharactereditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_nonbreakingspaceeditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_quicktextplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_sharetexteditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditor/kmail_zoomtexteditorplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditorconverttext/kmail_markdownplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditorgrammar/kmail_grammalecteplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditorgrammar/kmail_languagetoolplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/plugineditorinit/kmail_externalcomposereditorplugin.so
%{_libdir}/qt6/plugins/pim6/messageviewer
%{_libdir}/qt6/plugins/pim6/pimcommon
%{_libdir}/qt6/plugins/pim6/webengineviewer
%{_libdir}/qt6/plugins/pim6/korganizer/lunarphases.so
%{_datadir}/icons/hicolor/scalable/status/moon-phase-first-quarter.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-full.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-last-quarter.svg
%{_datadir}/icons/hicolor/scalable/status/moon-phase-new.svg
%{_libdir}/libakonadidatasetools.so.*
%{_libdir}/qt6/plugins/pim6/contacteditor/editorpageplugins/cryptopageplugin.so
%{_libdir}/qt6/plugins/pim6/kmail/mainview/kmail_akonadidatabasetoolplugin.so

%prep
%autosetup -p1 -n kdepim-addons-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja \
	-DKDEPIMADDONS_BUILD_EXAMPLES:BOOL=true

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
