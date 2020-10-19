# Microsoft Graph CLI

It is said that imitation is the sincerest form of flattery and if you are familiar with the Azure CLI, you can tell we are fans. The Microsoft Graph CLI leverages the same tool chain that is used to build the Azure CLI, but instead brings the entire surface area of Microsoft Graph to your command shell.

This project is still in its early phases, but we are building not only on the work of the Azure CLI team but also on the [Microsoft Graph PowerShell SDK](https://github.com/microsoftgraph/msgraph-sdk-powershell) project to enable us to quickly generate a CLI for all the new capabilities of Microsoft Graph as soon as they are available.

## Installation

**Windows**

Download the .msi package from the latest [release](https://github.com/microsoftgraph/msgraph-cli/releases)

**Linux**

Download the .deb package from the latest [release](https://github.com/microsoftgraph/msgraph-cli/releases) and install the package with the command below.
``` bash
sudo dpkg -i msgraph-cli_all.deb
```

**Docker**

Build the image. Run the command from project root.
```bash
docker build --target build-env -f ./build_scripts/debian/Dockerfile -t microsoft/msgraph-cli:ubuntu-builder .
```

Run the container interactively
```bash
docker run -it --name deb microsoft/msgraph-cli:ubuntu-builder   
```

## Usage

```bash
$ mg [ group ] [ command ] {parameters}
```

### Get Started

#### Login
```bash
$ mg login --scopes "user.read.all"
```

#### Query

You can use the `--query` parameter and the [JMESPath](http://jmespath.org/) query syntax to customize your output.

```bash
$ mg users list-user --query "[?userType=='Member'].{name: displayName, email: mail}" --output table

Name                      Email
------------------------  -------------------------------------
Conf Room Adams           Adams@M365x555627.OnMicrosoft.com
Adele Vance               AdeleV@M365x555627.OnMicrosoft.com
MOD Administrator         admin@M365x555627.OnMicrosoft.com
Alex Wilber               AlexW@M365x555627.OnMicrosoft.com
```

#### Exit codes

For scripting purposes, we output certain exit codes for differing scenarios.

|Exit Code   |Scenario   |
|---|---|
|0  |Command ran successfully.   |
|1   |Generic error; server returned bad status code, CLI validation failed, etc.   |
|2   |Parser error; check input to command line.   |


### Common scenarios and use Microsoft Graph CLI effectively

### More samples and snippets

## Reporting issues and feedback

If you encounter any bugs with the tool please file an issue in the [Issues](https://github.com/microsoftgraph/graph-cli/issues) section of our GitHub repo.

To provide feedback from the command line, try the `az feedback` command.


## Developer setup

If you would like to setup a development environment and contribute to the CLI, see:


## Contribute code

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
