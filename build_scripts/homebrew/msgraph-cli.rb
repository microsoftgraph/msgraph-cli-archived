class MsgraphCli < Formula
  include Language::Python::Virtualenv

  desc "Python based command line tools for interacting with Microsoft Graph"
  homepage "https://developer.microsoft.com/en-us/graph"
  version "0.1.3"
  url "https://codeload.github.com/microsoftgraph/msgraph-cli/tar.gz/refs/tags/beta"
  sha256 "045fa59b9b2ce399f7ff1da7e069b3d1f93a6553c7e9e71da0e94dbbee33ed0b"
  license "MIT"

  depends_on "openssl@1.1"
  depends_on "python@3.9"

  uses_from_macos "libffi"

  on_linux do
    depends_on "pkg-config" => :build
  end

  #   resource "cffi" do
  #   url "https://files.pythonhosted.org/packages/a8/20/025f59f929bbcaa579704f443a438135918484fffaacfaddba776b374563/cffi-1.14.5.tar.gz"
  #   sha256 "fd78e5fee591709f32ef6edb9a015b4aa1a5022598e36227500c8f4e02328d9c"
  # end

  # resource "cryptography" do
  #   url "https://files.pythonhosted.org/packages/9b/77/461087a514d2e8ece1c975d8216bc03f7048e6090c5166bc34115afdaa53/cryptography-3.4.7.tar.gz"
  #   sha256 "3d10de8116d25649631977cb37da6cbdd2d6fa0e0281d014a5b7d337255ca713"
  # end

  # resource "msgraph" do
  #   url "https://files.pythonhosted.org/packages/99/73/487a66f4cb58ef5b6246b67923850a79389f4fcceaf44526edf084eb2a7e/msgraph-0.1.2.tar.gz"
  #   sha256 "11f46f930c14958499479101c528ece87744498e81310b163d1bfd6a9598b441"
  # end

  # resource "pycparser" do
  #   url "https://files.pythonhosted.org/packages/0f/86/e19659527668d70be91d0369aeaa055b4eb396b0f387a4f92293a20035bd/pycparser-2.20.tar.gz"
  #   sha256 "2d475327684562c3a96cc71adf7dc8c4f0565175cf86b6d7a404ff4c771f15f0"
  # end

  def install
    # Work around Xcode 11 clang bug
    # https://code.videolan.org/videolan/libbluray/issues/20
    ENV.append_to_cflags "-fno-stack-check" if DevelopmentTools.clang_build_version >= 1010
    venv = virtualenv_create(libexec, "python3")

    # venv.pip_install resources

    extensions = Dir.glob('msgraph/cli/command_modules/*')

    venv.pip_install buildpath

    # Install extensions
    extensions.each do |extension|
      if File.directory?(buildpath/"#{extension}")
        cd buildpath/"#{extension}" do
            begin
                puts("Installing #{extension}")
                venv.instance_variable_get(:@formula).system venv.instance_variable_get(:@venv_root)/"bin/pip", "install", "install", "."
            rescue => error
               # pass
            end
        end
      end
    end

  #
  cd buildpath do
    system('git clone --branch beta git@github.com:microsoftgraph/azure-cli.git')
    cd buildpath/"azure-cli/src/azure-cli-core" do
      puts("Installing azure-cli-core")
      venv.instance_variable_get(:@formula).system venv.instance_variable_get(:@venv_root)/"bin/pip", "install", "install", "."
    end
  end


    (bin/"graph").write <<~EOS
      #!/usr/bin/env bash
      MG_INSTALLER=HOMEBREW #{libexec}/bin/python -m msgraph.cli \"$@\"
    EOS

    bash_completion.install "az.completion" => "graph"
  end
end
