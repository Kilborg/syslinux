Summary:	Simple bootloader
Summary(pl):	Prosty bootloader
Summary(pt_BR):	Carregador de boot simples
Summary(zh_CN):	Linux操作系统的启动管理器
Name:		syslinux
Version:	2.09
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
# Source0-md5:	703f11a01acf67a9f83ec082ca395565
Patch0:		%{name}-nowin32.patch
Patch1:		%{name}-cpp-comment.patch
URL:		http://syslinux.zytor.com/
BuildRequires:	perl
BuildRequires:	nasm
Requires:	mtools
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SYSLINUX is a boot loader for the Linux operating system which
operates off MS-DOS floppies. It is intended to simplify first-time
installation of Linux, rescue disks, and other uses for boot floppies.
A SYSLINUX floppy can be manipulated using standard MS-DOS (or any
other OS that can access an MS-DOS filesystem) tools once it has been
created, and requires only a ~ 7K DOS program or ~ 13K Linux program
to create it in the first place. It also includes PXELINUX, a program
to boot off a network server using a boot PROM compatible with the
Intel PXE (Pre-Execution Environment) specification.

%description -l pl
SYSLINUX jest boot-loaderem dla Linux'a, kt髍y operuje na dyskietkach
z systemem plik體 MS-DOS. Jego przeznaczeniem jest uproszczenie
pierwszej instalacji Linux'a, dyskietki ratunkowe oraz inne rzeczy
zwi眤ane z dyskietkami. Dyskietka SYSLINX'owa mo縠 by� modyfikowana w
systemie MS-DOS (a tak縠 ka縟ym innym systemie z dost阷em do systemu
plik體 MS-DOS) gdy narz阣zia sa ju� stworzone, a tak縠 potrzebuje
tylko ~7K programu DOS'owego lub ~13K programu Linux'owego do
stworzenia ich po raz pierwszy. Zawiera tak縠 program PXELINUX -
program s硊勘cy do bootowania servera sieciowego poprzez Boot-PROM
kompatybilny ze specyfikacj� Intel PXE (Pre-Execution Environment).

%description -l pt_BR
SYSLINUX � um carregador de boot para o linux, operando em disquetes
com formata玢o DOS. Sua inten玢o � simplificar instala珲es do Linux,
discos de recupera玢o, e outros usos para disquetes de boot. Um
disquete SYSLINUX pode ser manipulado usando ferramentas padr鉶 do DOS
(ou qualquer sistema que possa acessar um filesystem DOS) e requer
somente um programa DOS de aproximadamente 7K ou linux de 13K para
cri�-lo na primeira vez.

Tamb閙 inclui o PXELINUX, um programa para boot remoto a partir de um
servidor de rede usando um boot PROM compat韛el com a especifica玢o
Intel PXE (Pre-Execution Environment).

%package libs
Summary:        syslinux shared libraries
Summary(pl):    Biblioteki wsp蟪dzielone syslinux
Group:          Libraries

%description libs
syslinux shared libraries.

%description libs -l pl
Biblioteki wsp蟪dzielone syslinux.

%package devel
Summary:        syslinux static libraries
Summary(pl):    Biblioteki statyczne syslinux
Summary(pt_BR): Bibliotecas est醫icas para desenvolvimento com openldap
Summary(ru):    笤猎赊庞松� 律绿上耘松 syslinux
Summary(uk):    笤猎赊桅 娄绿ο耘松 syslinux
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description devel
This package includes the development libraries and header files
needed for compilation of applications that are making use of the syslinux
internals. Install this package only if you plan to develop or will
need to compile cutomized syslinux clients.

%description devel -l pl
Biblioteki statyczne syslinux.

%package static
Summary:        syslinux static libraries
Summary(pl):    Biblioteki statyczne syslinux
Summary(pt_BR): Bibliotecas est醫icas para desenvolvimento com openldap
Summary(ru):    笤猎赊庞松� 律绿上耘松 syslinux
Summary(uk):    笤猎赊桅 娄绿ο耘松 syslinux
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
This package includes the development libraries and header files
needed for compilation of applications that are making use of the syslinux
internals.

%description static -l pl
Biblioteki statyczne syslinux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} installer CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_includedir}}

%{__make} install install-lib \
	INSTALLROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README *.doc */*.doc
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}

%files libs
%defattr(644,root,root,755)
%{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
