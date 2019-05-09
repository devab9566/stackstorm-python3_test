from st2common.runners.base_action import Action


class TestStdlibImportAction(Action):
    """
    Action which imports cassandra driver which then imports "concurrent" module
    which is available in Python 3 standard libary, but also in Python 2
    site-packages.

    If Python 3 functionality works correclty, this action shouldn't break and
    concurrent module should be imported from Python 3 stdlib when using
    --python3 flag.
    """
    def run(self):
        from cassandra.cluster import Cluster
        cluster = Cluster()  # NOQA

        import concurrent
        if 'lib/python3' not in concurrent.__file__:
            msg = 'concurrent module was not imported from Python 3 stdlib'
            return False, msg

        return True, 'imports work correctly'