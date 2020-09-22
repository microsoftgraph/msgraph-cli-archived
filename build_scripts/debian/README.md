# Debian Packaging
================

Building the Debian package
---------------------------

On a machine with Docker, execute the following command from the root directory of this repository:

``` bash
docker build --target build-env -f ./build_scripts/debian/Dockerfile -t microsoft/msgraph-cli:ubuntu-builder.
```

After several minutes, this will have created a Docker image named `microsoft/msgraph-cli:ubuntu-builder` containing an
unsigned `.deb` built from the current contents of your msgraph-cli directory. To extract the build product from the image
you can run the following commands:

``` bash
docker run --name debian microsoft/msgraph-cli:ubuntu-builder
docker cp debian:/msgraph-cli_all.deb .
```


Run the commands below in a linux environment like wsl if you're on windows.
Verification
------------

``` bash
sudo dpkg -i msgraph-cli_all.deb
mg
```
