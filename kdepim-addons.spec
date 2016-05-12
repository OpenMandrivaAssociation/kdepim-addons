Summary:	Add-Ons for the KDE PIM suite
Name:		kdepim-addons
Version:	16.04.1
Release:	1
Epoch:		1
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
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5GAPI)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5MailCommon)
BuildRequires:	cmake(KF5KaddressbookGrantlee)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(KF5PimCommon)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5IncidenceEditor)
BuildRequires:	cmake(KF5MessageCore)
BuildRequires:	cmake(KF5MessageComposer)
BuildRequires:	cmake(KF5MessageList)
BuildRequires:	cmake(KF5CalendarSupport)
BuildRequires:	cmake(KF5EventViews)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Gravatar)
BuildRequires:	cmake(KF5Tnef)
BuildRequires:	pkgconfig(shared-mime-info)

%description
Add-Ons for the KDE PIM suite

%files
%config %{_sysconfdir}/xdg/kdepim-addons.categories
%config %{_sysconfdir}/xdg/kmail.antispamrc
%config %{_sysconfdir}/xdg/kmail.antivirusrc
%{_bindir}/kmail_antivir.sh
%{_bindir}/kmail_clamav.sh
%{_bindir}/kmail_fprot.sh
%{_bindir}/kmail_sav.sh
%{_libdir}/akonadi/contact/editorpageplugins/cryptopageplugin.so
%{_libdir}/libkaddressbookmergelibprivate.so.5*
%{_libdir}/libshorturlpluginprivate.so.5*
%{_libdir}/qt5/plugins/kaddressbook/kaddressbook_checkgravatarplugin.so
%{_libdir}/qt5/plugins/kaddressbook/kaddressbook_mergecontactsplugin.so
%{_libdir}/qt5/plugins/kaddressbook/kaddressbook_searchduplicatesplugin.so
%{_libdir}/qt5/plugins/kaddressbook/kaddressbook_sendmailplugin.so
%{_libdir}/qt5/plugins/kaddressbook/kaddressbook_sendvcardsplugin.so
%{_libdir}/qt5/plugins/kmail/kmail_antispamplugin.so
%{_libdir}/qt5/plugins/kmail/kmail_antivirusplugin.so
%{_libdir}/qt5/plugins/kmail/kmail_changecaseeditorplugin.so
%{_libdir}/qt5/plugins/kmail/kmail_insertspecialcharactereditorplugin.so
%{_libdir}/qt5/plugins/kmail/kmail_zoomtexteditorplugin.so
%{_libdir}/qt5/plugins/korg_datenums.so
%{_libdir}/qt5/plugins/korg_hebrew.so
%{_libdir}/qt5/plugins/korg_picoftheday.so
%{_libdir}/qt5/plugins/korg_thisdayinhistory.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_allheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_briefheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_createeventplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_createnoteplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_createtodoplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_defaultgrantleeheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_enterpriseheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_expandurlplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_fancyheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_grantleeheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_longheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_standardsheaderstyleplugin.so
%{_libdir}/qt5/plugins/messageviewer/messageviewer_translatorplugin.so
%{_libdir}/qt5/plugins/messageviewer_bodypartformatter_application_mstnef.so
%{_libdir}/qt5/plugins/messageviewer_bodypartformatter_text_vcard.so
%{_libdir}/qt5/plugins/messageviewer_bodypartformatter_text_xdiff.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_boxplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_dropboxplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_gdriveplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_hubicplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_isgdshorturlengineplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_shorturlplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_tinyurlengineplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_translatorplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_triopabshorturlengineplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_ur1cashorturlengineplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_webdavplugin.so
%{_libdir}/qt5/plugins/pimcommon/pimcommon_yousenditplugin.so
%{_datadir}/kmail2/pics/*
%{_datadir}/kservices5/korganizer/datenums.desktop
%{_datadir}/kservices5/korganizer/hebrew.desktop
%{_datadir}/kservices5/korganizer/picoftheday.desktop
%{_datadir}/kservices5/korganizer/thisdayinhistory.desktop
%{_datadir}/messageviewer/defaultthemes/*/*
%{_datadir}/messageviewer/plugins/bodypartformatter/*.desktop

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
