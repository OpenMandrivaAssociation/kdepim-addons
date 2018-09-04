Summary:	Add-Ons for the KDE PIM suite
Name:		kdepim-addons
Version:	 18.08.1
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
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(Qt5WebKit)
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
BuildRequires:	cmake(KF5LibkdepimAkonadi)
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
BuildRequires:	cmake(KF5MailImporterAkonadi)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(SharedMimeInfo)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(shared-mime-info)
Conflicts:	kmail <= 3:16.04.3-2

%description
Add-Ons for the KDE PIM suite.

%files -f %{name}.lang
%config %{_sysconfdir}/xdg/kdepim-addons.categories
%config %{_sysconfdir}/xdg/kdepim-addons.renamecategories
%config %{_sysconfdir}/xdg/kmail.antispamrc
%config %{_sysconfdir}/xdg/kmail.antivirusrc
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
%{_libdir}/libkaddressbookimportexportlibprivate.so.5*
%{_libdir}/libadblocklibprivate.so.5*
%{_libdir}/contacteditor
%{_libdir}/qt5/plugins/contacteditor
%{_libdir}/qt5/plugins/importwizard/*.so
%{_libdir}/qt5/plugins/kaddressbook/*.so
%{_libdir}/qt5/plugins/kmail/*.so
%{_libdir}/qt5/plugins/korg_datenums.so
%{_libdir}/qt5/plugins/korg_picoftheday.so
%{_libdir}/qt5/plugins/korg_thisdayinhistory.so
%{_libdir}/qt5/plugins/messageviewer/*.so
%{_libdir}/qt5/plugins/messageviewer/bodypartformatter
%{_libdir}/qt5/plugins/pimcommon/*.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/*.so
%{_libdir}/qt5/plugins/plasmacalendarplugins/pimevents/PimEventsConfig.qml
%{_libdir}/qt5/plugins/webengineviewer/*.so
%{_libdir}/qt5/plugins/libksieve
%{_libdir}/qt5/plugins/mailtransport
%{_libdir}/qt5/plugins/messageviewer/grantlee/*/kitinerary_grantlee_extension.so
%{_libdir}/qt5/plugins/templateparser
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/libpimcalendarsplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/PimCalendars/qmldir
%{_datadir}/contacteditor
%{_datadir}/kmail2/pics/*
%{_datadir}/kservices5/korganizer/datenums.desktop
%{_datadir}/kservices5/korganizer/picoftheday.desktop
%{_datadir}/kservices5/korganizer/thisdayinhistory.desktop
%{_datadir}/kconf_update/webengineurlinterceptoradblock.upd

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
