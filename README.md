# nginx-quic.spec

nginx quic preview package build for AARCH64 Ampere A1 CPU.

- Enable QUIC and HTTP/3
- SSL library uses quictls (Support kernel TLS)
- Use cloudflare zlib
- Use jemalloc or mimalloc optionally (-secure is WIP, all commented)
- Many dynamic modules
- ~~Enable debug option~~
- Enable FastTCP option
- And some optimize for Ampere A1 CPU (~~Disable~~ Enable LTO, -mtune=ampere1 and etc.)
- ASLR enabled (-fPIC, -fPIE)
- WIP, to be continued.
## Build

Requirement

- epel repository
- scl repository [reference](https://wiki.centos.org/AdditionalResources/Repositories/SCL)

enable other repository

```
sudo yum install -y epel-release
sudo yum install -y centos-release-scl
```

install tools

```
sudo yum install -y rpmlint rpm-build rpmdevtools yum-utils 
```

prepare

```
git clone https://github.com/ryoh/nginx-quic.spec.git
cd nginx-quic
cp -p .rpmmacros $HOME/

# Install build dependent packages
yum-builddep -y SPECS/nginx-quic.spec

# Download SOURCES files
./prepare.sh
```

build

```
rpmbuild -ba SPECS/nginx-quic.spec
```
