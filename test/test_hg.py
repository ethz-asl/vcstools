        # in hg, tagging creates an own changeset, so we need to fetch version before tagging
        subprocess.check_call(["hg", "tag", "test_tag"], cwd=remote_path)

        self.assertEqual(client.get_version(self.readonly_version_init[0:6]), self.readonly_version_init)
        self.assertEqual(client.get_version("test_tag"), self.readonly_version_init)
    def test_get_version_modified(self):
        from vcstools.hg import HgClient
        client = HgClient(self.readonly_path)
        self.assertFalse(client.get_version().endswith('+'))
    