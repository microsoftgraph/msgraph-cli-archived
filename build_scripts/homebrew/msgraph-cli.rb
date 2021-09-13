class MsgraphCli < Formula
  include Language::Python::Virtualenv

  desc "Python based command line tools for interacting with Microsoft Graph"
  homepage "https://developer.microsoft.com/en-us/graph"
  version "0.1.5.1"
  url "https://codeload.github.com/microsoftgraph/msgraph-cli/tar.gz/refs/tags/0.1.5.1"
  sha256 "9875f0f729bde45290f941cc9e3e80be8eb8a48ce51eb745465c86e4161c9e7d"
  license "MIT"

  depends_on "openssl@1.1"
  depends_on "python@3.8"

  uses_from_macos "libffi"

  on_linux do
    depends_on "pkg-config" => :build
  end

    resource "msgraph" do
    url "https://files.pythonhosted.org/packages/99/73/487a66f4cb58ef5b6246b67923850a79389f4fcceaf44526edf084eb2a7e/msgraph-0.1.2.tar.gz"
    sha256 "11f46f930c14958499479101c528ece87744498e81310b163d1bfd6a9598b441"
  end

  def install
    # Work around Xcode 11 clang bug
    # https://code.videolan.org/videolan/libbluray/issues/20
    ENV.append_to_cflags "-fno-stack-check" if DevelopmentTools.clang_build_version >= 1010
    venv = virtualenv_create(libexec, "python3")

    venv.pip_install resources

    extensions = Dir.glob('msgraph/cli/command_modules/*')

    # install msgraph module
    venv.instance_variable_get(:@formula).system venv.instance_variable_get(:@venv_root)/"bin/pip", "install", buildpath

   # Install extensions
    extensions.each do |extension|
      if File.directory?(buildpath/"#{extension}")
        cd buildpath/"#{extension}" do
            begin
                puts("Installing #{extension}")
                venv.instance_variable_get(:@formula).system venv.instance_variable_get(:@venv_root)/"bin/pip", "install", "."
            rescue => error
               # pass
            end
        end
      end
    end

    (bin/"graph").write <<~EOS
      #!/usr/bin/env bash
      MG_INSTALLER=HOMEBREW #{libexec}/bin/python -m msgraph.cli \"$@\"
    EOS

    bash_completion.install "az.completion" => "graph"
  end
end