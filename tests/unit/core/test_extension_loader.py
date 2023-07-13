from bandit.core import extension_loader


def test_load_plugins():
    mgr = extension_loader.MANAGER
    print(mgr.plugins)
