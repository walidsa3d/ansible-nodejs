def test_nodejs_installed(host):
    node = host.package("nodejs")
    assert node.is_installed

def test_npm_installed(host):
    npm = host.exists("npm")
    assert npm