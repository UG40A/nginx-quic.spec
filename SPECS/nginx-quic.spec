%global         _performance_build  1
%global         _hardened_build     1

%global         nginx_user          nginx
%global         nginx_group         nginx
%global         nginx_uid           996
%global         nginx_gid           996
%global         nginx_moddir        %{_libdir}/nginx/modules
%global         nginx_confdir       %{_sysconfdir}/nginx
%global         nginx_tempdir       %{_var}/cache/nginx
%global         nginx_logdir        %{_localstatedir}/log/nginx
%global         nginx_rundir        %{_rundir}
%global         nginx_lockdir       %{_rundir}/lock/subsys/nginx
%global         nginx_home          %{_datadir}/nginx
%global         nginx_webroot       %{nginx_home}/html
%global         nginx_client_tempdir   %{nginx_tempdir}/client_body_temp
%global         nginx_proxy_tempdir    %{nginx_tempdir}/proxy_temp
%global         nginx_fastcgi_tempdir  %{nginx_tempdir}/fastcgi_temp
%global         nginx_uwsgi_tempdir    %{nginx_tempdir}/uwsgi_temp
%global         nginx_scgi_tempdir     %{nginx_tempdir}/scgi_temp
%global         nginx_proxy_cachedir   %{nginx_tempdir}/proxy_cache
%global         nginx_fastcgi_cachedir %{nginx_tempdir}/fastcgi_cache
%global         nginx_uwsgi_cachedir   %{nginx_tempdir}/uwsgi_cache
%global         nginx_scgi_cachedir    %{nginx_tempdir}/scgi_cache

%global         nginx_quic_commit   5b1011b5702b
%global         njs_version         0.7.4
%global         cf_zlib_version     1.2.8
%global         zlib_ng_version     2.0.6
%global         quictls_version     3.0.3
%global         ngx_brotli_version  v1.0.0rc
%global         ngx_devel_kit_version 	b4642d6ca01011bd8cd30b253f5c3872b384fd21

%global					modsecurity_version	v1.0.3
%global         ngx_naxsi_version   d68c33b0d214318fc1abb7e6ef751b7539681cc9 
%global         ngx_zstd_version    1e0fa0bfb995e72f8f7e4c0153025c3306f1a5cc

# openresty:
%global         ngx_more_headers_version    v0.33
%global         ngx_echo_version            v0.62
%global         ngx_memc_version            v0.19
%global         ngx_set_misc_version        v0.33
%global         ngx_pgs_version             1.0
%global         ngx_srcache_version         v0.32

# others:
%global         ngx_geoip2_version          3.3
%global         ngx_vts_version             v0.1.18  
%global         ngx_pta_version             v1.0.0
%global         ngx_fancyindex_version      v0.5.2
%global         ngx_secure_token_version    d3d8cead244a0b3083c895043fa86de2f399d488

# forks:
%global         ngx_push_stream_version     ead73a54cfd32dd804087580c41041648dcf5240
%global         ngx_sticky_version          e26ad8c81dd729343234531a6d47c029bad59153
%global         ngx_cookie_flag_version     1cfba16c22d39743240d734fc0c04f7ed1c5929b
%global         ngx_sysguard_version        aa65c0b71b23229bd9408cc69096bfe2838c34ce
%global         ngx_cache_purge_version     2.5.2

# GetPageSpeed repo:
%global         ngx_security_headers_version 0.0.1
%global         ngx_dynamic_etag_version    0.2.1
%global         ngx_immutable_version       v0.0.1

## build failed:
%global         ngx_pagespeed_version   v1.14.33.1-RC1

###

%global         pkg_name            nginx-quic
%global         main_version        1.22
%global         main_release        4%{?dist}.quictls%{quictls_version}

Name:           %{pkg_name}
Version:        %{main_version}
Release:        %{main_release}
Summary:        A high performance web server and reverse proxy
Group:          System Environment/Daemons 
License:        BSD
URL:            https://nginx.org/

Source0:        https://hg.nginx.org/nginx-quic/archive/%{nginx_quic_commit}.tar.gz#/nginx-quic-%{nginx_quic_commit}.tar.gz
Source1:        https://hg.nginx.org/njs/archive/%{njs_version}.tar.gz#/njs-%{njs_version}.tar.gz
Patch0:					https://raw.githubusercontent.com/UG40A/nginx-quic.spec/master/SOURCES/dyntls_hpack.patch

# Multi.patch is:
#	https://raw.githubusercontent.com/nginx-modules/ngx_http_tls_dyn_size/master/nginx__dynamic_tls_records_1.17.7%2B.patch
#	https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/nginx_hpack_push_1.15.3.patch
# Patch: https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/remove_nginx_server_header.patch \
# has not been applied yet.

# Modsecurity patch:
Patch2:         modsecurity_nginx_memleaks_and_severity.patch

# Naxsi patch:
Patch223:       naxsi_header.patch

# QuicTLS patch:
Patch100:       openssl-multi.patch

Source10:       nginx.service
Source11:       nginx.sysconf
Source12:       nginx.logrotate
Source13:       nginx.conf
Source14:       nginx-http.conf
Source15:       nginx-http-log_format.conf
Source16:       nginx-http-client.conf
Source17:       nginx-http-proxy.conf
Source18:       nginx-http-gzip.conf
Source19:       nginx-http-ssl.conf
Source20:       nginx-http-security_headers.conf
Source21:       nginx-http-proxy_headers.conf
Source22:       nginx-http-brotli.conf
Source50:       00-default.conf

Source100:      https://github.com/quictls/openssl/archive/openssl-%{quictls_version}+quic.tar.gz
Source101:      https://github.com/cloudflare/zlib/archive/v%{cf_zlib_version}.tar.gz#/zlib-%{cf_zlib_version}.tar.gz
Source102:      https://github.com/zlib-ng/zlib-ng/archive/%{zlib_ng_version}.tar.gz#/zlib-ng-%{zlib_ng_version}.tar.gz

Source200:      https://github.com/google/ngx_brotli/archive/%{ngx_brotli_version}.tar.gz#/ngx_brotli-%{ngx_brotli_version}.tar.gz
Source201:      https://github.com/leev/ngx_http_geoip2_module/archive/%{ngx_geoip2_version}.tar.gz#/ngx_http_geoip2_module-%{ngx_geoip2_version}.tar.gz
Source202:      https://github.com/SpiderLabs/ModSecurity-nginx/archive/%{modsecurity_version}.tar.gz#/modsecurity-nginx-%{modsecurity_version}.tar.gz
Source203:      https://github.com/vozlt/nginx-module-vts/archive/%{ngx_vts_version}.tar.gz#/nginx-module-vts-%{ngx_vts_version}.tar.gz
Source204:      https://github.com/openresty/echo-nginx-module/archive/%{ngx_echo_version}.tar.gz#/echo-nginx-module-%{ngx_echo_version}.tar.gz
Source205:      https://github.com/openresty/headers-more-nginx-module/archive/%{ngx_more_headers_version}.tar.gz#/headers-more-nginx-module-%{ngx_more_headers_version}.tar.gz
Source206:      https://github.com/tokers/zstd-nginx-module/archive/%{ngx_zstd_version}.tar.gz#/zstd-nginx-module-%{ngx_zstd_version}.tar.gz

Source207:      https://github.com/openresty/memc-nginx-module/archive/%{ngx_memc_version}.tar.gz#/memc-nginx-module-%{ngx_memc_version}.tar.gz
Source208:      https://github.com/openresty/srcache-nginx-module/archive/%{ngx_srcache_version}.tar.gz#/srcache-nginx-module-%{ngx_srcache_version}.tar.gz
Source209:      https://github.com/openresty/ngx_postgres/archive/%{ngx_pgs_version}.tar.gz#/ngx_postgres-%{ngx_pgs_version}.tar.gz
Source210:      https://github.com/openresty/set-misc-nginx-module/archive/%{ngx_set_misc_version}.tar.gz#/set-misc-nginx-module-%{ngx_set_misc_version}.tar.gz

Source211:      https://github.com/dvershinin/ngx_dynamic_etag/archive/%{ngx_dynamic_etag_version}.tar.gz#/{ngx_dynamic_etag_version}.tar.gz
Source212:      https://github.com/GetPageSpeed/ngx_security_headers/archive/%{ngx_security_headers_version}.tar.gz#/{ngx_security_headers_version}.tar.gz
Source213:      https://github.com/GetPageSpeed/ngx_immutable/archive/%{ngx_immutable_version}.tar.gz#/{ngx_immutable_version}.tar.gz

Source214:      https://github.com/kaltura/nginx-secure-token-module/archive/%{ngx_secure_token_version}.tar.gz#/%{ngx_secure_token_version}.tar.gz
Source215:      https://github.com/iij/pta/archive/%{ngx_pta_version}.tar.gz#/%{ngx_pta_version}.tar.gz
Source216:      https://github.com/aperezdc/ngx-fancyindex/archive/%{ngx_fancyindex_version}.tar.gz#/%{ngx_fancyindex_version}.tar.gz

Source217:      https://github.com/RekGRpth/nginx-push-stream-module/archive/%{ngx_push_stream_version}.tar.gz#/%{ngx_push_stream_version}.tar.gz
Source218:      https://github.com/levonet/nginx-sticky-module-ng/archive/%{ngx_sticky_version}.tar.gz#/%{ngx_sticky_version}.tar.gz
Source219:      https://github.com/acastlesibm/nginx_cookie_flag_module/archive/%{ngx_cookie_flag_version}.tar.gz#/%{ngx_cookie_flag_version}.tar.gz
Source220:      https://github.com/devnexen/nginx-module-sysguard/archive/%{ngx_sysguard_version}.tar.gz#/%{ngx_sysguard_version}.tar.gz
Source221:      https://github.com/nginx-modules/ngx_cache_purge/archive/%{ngx_cache_purge_version}.tar.gz#/%{ngx_cache_purge_version}.tar.gz
Source222:      https://github.com/vision5/ngx_devel_kit/archive/%{ngx_devel_kit_version}.tar.gz#/%{ngx_devel_kit_version}.tar.gz

Source223:      https://github.com/nbs-system/naxsi/archive/%{ngx_naxsi_version}.tar.gz#/%{ngx_naxsi_version}.tar.gz
Source224:      https://github.com/apache/incubator-pagespeed-ngx/archive/%{ngx_pagespeed_version}.tar.gz#/%{ngx_pagespeed_version}.tar.gz


# Requires:       jemalloc
Requires:       mimalloc
Requires:       brotli
Requires:       libzstd
Requires:       libslz
Requires(pre):  shadow-utils
Requires(post):   systemd 
Requires(preun):  systemd 
Requires(postun): systemd 
BuildRequires:    systemd

BuildRequires:  make gcc lld automake autoconf libtool
BuildRequires:  zlib-devel pcre-devel
# BuildRequires:  jemalloc-devel
BuildRequires:  mimalloc-devel
BuildRequires:  libunwind-devel
BuildRequires:  brotli-devel
BuildRequires:  openssl-devel
BuildRequires:  GeoIP-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  readline-devel
BuildRequires:  perl-IPC-Cmd perl-CPAN
BuildRequires:  libzstd-devel
BuildRequires:  libslz-devel
BuildRequires:  libpq-devel
BuildRequires:  gd-devel
BuildRequires:  libxslt-devel
BuildRequires:  gcc-toolset-11 gcc-toolset-11-annobin-plugin-gcc 

%description
nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server,
and a generic TCP/UDP proxy server, originally written by Igor Sysoev.

%prep
%setup -q -n %{name}-%{nginx_quic_commit}

pushd ..
MODULE="quictls"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE100} --strip 1
popd

pushd ..
MODULE="cf-zlib"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE101} --strip 1
popd

pushd ..
MODULE="njs"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE1} --strip 1
popd

pushd ..
MODULE="ngx_brotli"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE200} --strip 1
popd

pushd ..
MODULE="ngx_http_geoip2_module"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE201} --strip 1
popd

pushd ..
MODULE="ModSecurity-nginx"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE202} --strip 1
popd

pushd ..
MODULE="nginx-module-vts"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE203} --strip 1
popd

pushd ..
MODULE="echo-nginx-module"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE204} --strip 1
popd

pushd ..
MODULE="headers-more-nginx-module"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE205} --strip 1
popd

pushd ..
MODULE="zstd-nginx-module"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE206} --strip 1
popd

pushd ..
MODULE="ngx_memc"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE207} --strip 1
popd

pushd ..
MODULE="ngx_srcache"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE208} --strip 1
popd

pushd ..
MODULE="ngx_pgs"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE209} --strip 1
popd

pushd ..
MODULE="ngx_set_misc"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE210} --strip 1
popd

pushd ..
MODULE="ngx_dynamic_etag"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE211} --strip 1
popd

pushd ..
MODULE="ngx_security_headers"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE212} --strip 1
popd

pushd ..
MODULE="ngx_immutable"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE213} --strip 1
popd

pushd ..
MODULE="ngx_secure_token"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE214} --strip 1
popd

pushd ..
MODULE="ngx_pta"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE215} --strip 1
popd

pushd ..
MODULE="ngx_fancyindex"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE216} --strip 1
popd

pushd ..
MODULE="ngx_push_stream"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE217} --strip 1
popd

pushd ..
MODULE="ngx_sticky"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE218} --strip 1
popd

pushd ..
MODULE="ngx_cookie_flag"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE219} --strip 1
popd

pushd ..
MODULE="ngx_sysguard"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE220} --strip 1
popd

pushd ..
MODULE="ngx_cache_purge"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE221} --strip 1
popd

pushd ..
MODULE="ngx_devel_kit"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE222} --strip 1
popd

pushd ..
MODULE="ngx_naxsi"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE223} --strip 1
popd

pushd ..
MODULE="ngx_pagespeed"
%{__rm} -rf ${MODULE}
%{__mkdir} ${MODULE}
cd ${MODULE}
%{__tar} -xf %{SOURCE224} --strip 1
popd

%build
source scl_source enable gcc-toolset-11

# Change ModSecurity RPATH behavior:
# If NGX_IGNORE_RPATH is set to "YES", we will ignore explicit
# library path specification on resulting binary, allowing libmodsecurity.so
# to be relocated across configured library pathes (adjust /etc/ld.so.conf
# or set $LD_LIBRARY_PATH environment variable to manage them)
NGX_IGNORE_RPATH="NO"
# Explicit PATH env (only for NGX_IGNORE_RPATH=NO):
MODSECURITY_LIB="/usr/local/lib"
MODSECURITY_INC="/usr/local/include"

export MAKEFLAGS='-j$(nproc)'
EXCC_OPTS="-mcpu=native -O3 -ftree-vectorize -fuse-linker-plugin -fuse-ld=gold -fopenmp -fPIC -fomit-frame-pointer"
CFLAGS="$(echo %{optflags} $(pcre-config --cflags))"
CFLAGS="${CFLAGS} ${EXCC_OPTS}"; export CFLAGS;
export CXXFLAGS="${CFLAGS}"
LDFLAGS="%{?__global_ldflags} $(pcre-config --libs) -lmimalloc -lslz"
export LDFLAGS;

# Dynamic: 
# CFLAGS: -fPIC
# openssl-opts: -fPIC shared (enable-fips)
# Nginx-modules: "add-dynamic-module=../"
#
# Fully-Static: 
# CFLAGS: -fPIE -pie
# openssl-opts: -fPIE -pie (fips NOT supported, because strict-shared)
# Nginx-modules: "add-module=../"
#
# WIP: add args filter .so nginx dynamic modules and executable: -fPIC to libs and -fPIE to executable only

./auto/configure \
  --with-ld-opt="${LDFLAGS} -L../quictls/build/lib" \
  --with-cc-opt="${CFLAGS} -I../quictls/build/include -DTCP_FASTOPEN=23" \
  --with-openssl=../quictls \
  --with-openssl-opt="--prefix=/opt/openssl --openssldir=/opt/openssl -Wl,-rpath=/opt/openssl/lib -Wl,--enable-new-dtag -DOPENSSL_PIC -DOPENSSL_TLS_SECURITY_LEVEL=2 -DL_ENDIAN -DOPENSSL_USE_NODELETE -DNDEBUG -DPURIFY -DDEVRANDOM="\"/dev/urandom\"" -DOPENSSL_PIC enable-ec_nistp_64_gcc_128 enable-ktls zlib-dynamic" \
  --prefix=%{nginx_home} \
  --sbin-path=%{_sbindir}/nginx \
  --modules-path=%{nginx_moddir} \
  --conf-path=%{nginx_confdir}/nginx.conf \
  --pid-path=%{nginx_rundir}/nginx.pid \
  --lock-path=%{nginx_lockdir} \
  --error-log-path=%{nginx_logdir}/error.log \
  --http-log-path=%{nginx_logdir}/access.log \
  --http-client-body-temp-path=%{nginx_client_tempdir} \
  --http-proxy-temp-path=%{nginx_proxy_tempdir} \
  --http-fastcgi-temp-path=%{nginx_fastcgi_tempdir} \
  --http-uwsgi-temp-path=%{nginx_uwsgi_tempdir} \
  --http-scgi-temp-path=%{nginx_scgi_tempdir} \
  --user=%{nginx_user} \
  --group=%{nginx_group} \
  --build=%{name}-%{version}-%{release} \
  --with-threads \
  --with-file-aio \
  --with-compat \
  --with-pcre-jit \
  --with-http_ssl_module \
  --with-http_realip_module \
  --with-http_addition_module \
  --with-http_sub_module \
  --with-http_dav_module \
  --with-http_flv_module \
  --with-http_mp4_module \
  --with-http_gunzip_module \
  --with-http_gzip_static_module \
  --with-http_auth_request_module \
  --with-http_random_index_module \
  --with-http_secure_link_module \
  --with-http_degradation_module \
  --with-http_slice_module \
  --with-http_stub_status_module \
  --with-http_geoip_module \
  --with-stream \
  --with-stream_ssl_module \
  --with-stream_ssl_preread_module \
  --with-stream_realip_module \
  --with-stream_geoip_module \
  --with-select_module	\
  --with-http_xslt_module \
  --with-http_image_filter_module \
  --with-http_v2_module \
  --with-http_v3_module \
  --with-stream_quic_module \
  --with-mail \
  --with-mail_ssl_module \
  --add-dynamic-module=../njs/nginx \
  --add-dynamic-module=../ngx_brotli \
  --add-dynamic-module=../ngx_http_geoip2_module \
  --add-dynamic-module=../nginx-module-vts \
  --add-dynamic-module=../echo-nginx-module \
  --add-dynamic-module=../zstd-nginx-module \
  --add-dynamic-module=../ngx_memc \
  --add-dynamic-module=../ngx_pgs \
  --add-dynamic-module=../ngx_devel_kit \
  --add-dynamic-module=../ngx_set_misc \
  --add-dynamic-module=../ngx_dynamic_etag \
  --add-dynamic-module=../ngx_security_headers \
  --add-dynamic-module=../ngx_fancyindex \
  --add-dynamic-module=../ngx_push_stream \
  --add-dynamic-module=../ngx_cookie_flag \
  --add-dynamic-module=../ngx_sysguard \
  --add-dynamic-module=../ngx_cache_purge \
  --add-dynamic-module=../ngx_immutable \
  --add-dynamic-module=../ngx_secure_token \
  --add-dynamic-module=../ngx_pta \
  --add-dynamic-module=../ngx_sticky \
  --add-dynamic-module=../headers-more-nginx-module \
  --add-dynamic-module=../ngx_srcache
  
  #Failed to build:
  # Due to AARCH64:
  #  --add-dynamic-module=../ngx_pagespeed \
  # Due to LibModSecurity.so.3 linking problems (WIP):
  #  --add-dynamic-module=../ModSecurity-nginx
  # Due to "struct in6_pktinfo pkt6; undefined" error:
  # --add-dynamic-module=../ngx_naxsi/naxsi_src
  
%make_build

%install
[[ -d %{buildroot} ]] && rm -rf "%{buildroot}"
%{__mkdir} -p "%{buildroot}"
%make_install INSTALLDIRS=vendor

# Deleting unused files
%{__rm} -f %{buildroot}%{nginx_confdir}/fastcgi.conf
%{__rm} -f %{buildroot}%{nginx_confdir}/*.default

# Create temporary directories
%{__install} -p -d -m 0755 %{buildroot}%{nginx_rundir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_lockdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_client_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_proxy_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_fastcgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_uwsgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_scgi_tempdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_proxy_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_fastcgi_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_uwsgi_cachedir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_scgi_cachedir}

# Add systemd service unit file
%{__install} -p -D -m 0644 %{SOURCE10} %{buildroot}%{_unitdir}/nginx.service

# sysconfig
%{__install} -p -D -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/nginx

# logrotate
%{__install} -p -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/logrotate.d/nginx

# nginx config
unlink %{buildroot}%{nginx_confdir}/koi-utf
unlink %{buildroot}%{nginx_confdir}/koi-win
unlink %{buildroot}%{nginx_confdir}/win-utf
%{__install} -p -D -m 0640 %{SOURCE13} %{buildroot}%{nginx_confdir}/nginx.conf
%{__install} -p -D -m 0640 %{SOURCE14} %{buildroot}%{nginx_confdir}/conf.d/http.conf
%{__install} -p -D -m 0640 %{SOURCE15} %{buildroot}%{nginx_confdir}/conf.d/http/log_format.conf
%{__install} -p -D -m 0640 %{SOURCE16} %{buildroot}%{nginx_confdir}/conf.d/http/client.conf
%{__install} -p -D -m 0640 %{SOURCE17} %{buildroot}%{nginx_confdir}/conf.d/http/proxy.conf
%{__install} -p -D -m 0640 %{SOURCE18} %{buildroot}%{nginx_confdir}/conf.d/http/gzip.conf
%{__install} -p -D -m 0640 %{SOURCE19} %{buildroot}%{nginx_confdir}/conf.d/http/ssl.conf
%{__install} -p -D -m 0640 %{SOURCE20} %{buildroot}%{nginx_confdir}/conf.d/http/security_headers.conf
%{__install} -p -D -m 0640 %{SOURCE21} %{buildroot}%{nginx_confdir}/conf.d/http/proxy_headers.conf
%{__install} -p -D -m 0640 %{SOURCE22} %{buildroot}%{nginx_confdir}/conf.d/http/brotli.conf

%{__install} -p -D -m 0640 %{SOURCE50} %{buildroot}%{nginx_confdir}/vhost.d/http/00-default.conf

# nginx modules conf
%{__install} -p -d -m 0755 %{buildroot}%{nginx_confdir}/conf.modules.d/

# brotli module
cat <<__EOL__ > %{buildroot}%{nginx_confdir}/conf.modules.d/ngx_brotli.conf
load_module "%{nginx_moddir}/ngx_http_brotli_filter_module.so";
load_module "%{nginx_moddir}/ngx_http_brotli_static_module.so";
__EOL__

# nginx reset paths
%{__sed} -i \
  -e 's|${rundir}|%{_rundir}|g' \
  -e 's|${sbindir}|%{_sbindir}|g' \
  -e 's|${sysconfdir}|%{_sysconfdir}|g' \
  -e 's|${logdir}|%{nginx_logdir}|g' \
  -e 's|${pkg_name}|nginx|g' \
  %{buildroot}%{_unitdir}/nginx.service \
  %{buildroot}%{_sysconfdir}/sysconfig/nginx \
  %{buildroot}%{_sysconfdir}/logrotate.d/nginx \
  %{buildroot}%{nginx_confdir}/nginx.conf

%{__sed} -i \
  -e 's|${client_tempdir}|%{nginx_client_tempdir}|g' \
  %{buildroot}%{nginx_confdir}/conf.d/http/client.conf

%pre
case $1 in
  1)
  : install
  getent group %{nginx_group} >/dev/null 2>&1 \
    || groupadd -r -g %{nginx_gid} %{nginx_group} \
    || groupadd -r %{nginx_group}

  getent passwd %{nginx_user} >/dev/null 2>&1 \
    || useradd -r -g %{nginx_group} -u %{nginx_uid} %{nginx_user} \
    || useradd -r -g %{nginx_group} %{nginx_user}
  ;;
  2)
  : update
  ;;
esac

%post
%systemd_post nginx.service
case $1 in
  1)
  : install
  ;;
  2)
  : update
  ;;
esac

%preun
%systemd_pre nginx.service
case $1 in
  0)
  : uninstall
  ;;
  1)
  : update
  ;;
esac

%postun
%systemd_postun nginx.service
case $1 in
  0)
  : uninstall
  getent passwd %{nginx_user} >/dev/null 2>&1 \
    && userdel %{nginx_user} >/dev/null 2>&1 ||:

  getent group %{nginx_group} >/dev/null 2>&1 \
    && groupdel %{nginx_group} >/dev/null 2>&1 ||:
  ;;
  1)
  : update
  ;;
esac


%files
%defattr(-,root,root)
%{_sbindir}/nginx

%config(noreplace) %{nginx_confdir}/nginx.conf
%config(noreplace) %{nginx_confdir}/mime.types
%config(noreplace) %{nginx_confdir}/fastcgi_params
%config(noreplace) %{nginx_confdir}/scgi_params
%config(noreplace) %{nginx_confdir}/uwsgi_params
%config(noreplace) %{nginx_confdir}/conf.d/http.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/client.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/gzip.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/log_format.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/proxy.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/ssl.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/security_headers.conf
%config(noreplace) %{nginx_confdir}/conf.d/http/proxy_headers.conf
%config(noreplace) %{nginx_confdir}/vhost.d/http/00-default.conf

%dir %{nginx_home}
%dir %{nginx_webroot}
%{nginx_webroot}/50x.html
%{nginx_webroot}/index.html

%config(noreplace) %{_unitdir}/nginx.service
%config(noreplace) %{_sysconfdir}/sysconfig/nginx
%config(noreplace) %{_sysconfdir}/logrotate.d/nginx

%dir %{nginx_rundir}
%dir %{nginx_lockdir}

%defattr(-,%{nginx_user},%{nginx_group})
%dir %{nginx_logdir}
%dir %{nginx_tempdir}
%dir %{nginx_client_tempdir}
%dir %{nginx_proxy_tempdir}
%dir %{nginx_fastcgi_tempdir}
%dir %{nginx_uwsgi_tempdir}
%dir %{nginx_scgi_tempdir}
%dir %{nginx_proxy_cachedir}
%dir %{nginx_fastcgi_cachedir}
%dir %{nginx_uwsgi_cachedir}
%dir %{nginx_scgi_cachedir}

%config(noreplace) %{nginx_confdir}/conf.d/http/brotli.conf
%config(noreplace) %{nginx_confdir}/conf.modules.d/ngx_brotli.conf

%dir %{nginx_moddir}

# load all dynamic modules
%{nginx_moddir}/*.so

%changelog
* Tue Mar 22 2022 Ryoh Kawai <kawairyoh@gmail.com> - 1.21.6-4
- Fix config files
- Change bumpup njs
* Tue Mar 22 2022 Ryoh Kawai <kawairyoh@gmail.com> - 1.21.6-3
- Change GCC 9 to 11
* Tue Mar 22 2022 Ryoh Kawai <kawairyoh@gmail.com> - 1.21.6-2
- Rename package revision
- Disable debug option
* Mon Mar 21 2022 Ryoh Kawai <kawairyoh@gmail.com> - 1.21.6-1
- Change bumpup version nginx-quic, njs
- Change support quictls
* Mon May 17 2021 Ryoh Kawai <kawairyoh@gmail.com> - 1.21.0-1
- Add zstd module
- Fix ModSecurity module
* Mon May 17 2021 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.10-2
- Change bumpup version nginx-quic, boringssl
* Sun Apr 25 2021 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.10-1
- Change bumpup version nginx-quic, boringssl
* Thu Mar 25 2021 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.8-3
- Change build flags
- Add stream module
* Wed Mar 24 2021 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.8-2
- Add Cloudflare zlib
* Wed Mar 24 2021 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.8-1
- Change bumpup version nginx-quic, boringssl
* Tue Nov 03 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.4-1
- Change bumpup version nginx-quic
* Tue Oct 27 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.3-10
- Change bumpup version nginx-quic, boringssl
- Add njs module
- Add GeoIP module
- Add GeoIP2 module
- Add ModSecurity module
- Add VTS module
- Add echo module
- Add headers more filter module
* Tue Aug 11 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-9
- Change bumpup version nginx-quic, boringssl
* Wed Jul 29 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-8
- Add h3 directive: http3_max_field_size, http3_max_table_capacity, http3_max_blocked_streams, http3_max_concurrent_pushes, http3_push, http3_push_preload
- Add "quic" listen parameter
- Add HTTP/3 Server Push
- Add support HTTP/3 $server_protocol variable
- Add QUIC support for stream module
- Change build options
* Sun Jul 19 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-7
- Add Brotli module
* Sun Jul 19 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-6
- Change build options
* Sun Jul 19 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-5
- Change nginx-quic and boringssl commit version master -> commit hash
- Change snapshot version
* Thu Jul 16 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-4
- Delete openssl11-libs, openssl11-devel
* Wed Jul 15 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-1
- Add Conf files
* Fri Jul 10 2020 Ryoh Kawai <kawairyoh@gmail.com> - 1.19.1-0
- Initial
