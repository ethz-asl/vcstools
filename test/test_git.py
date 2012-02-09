    @classmethod
    def setUpClass(self):
       
        self.local_path = os.path.join(self.root_directory, "ros")


    @classmethod
    def tearDownClass(self):
    def tearDown(self):
        if os.path.exists(self.local_path):
            shutil.rmtree(self.local_path)
            
        client = GitClient(self.local_path)
        client = GitClient(self.local_path)
        client = GitClient(self.local_path)
        
        client = GitClient(self.local_path)
        self.assertEqual(client.get_path(), self.local_path)
        client = GitClient(self.local_path)
        self.assertEqual(client.get_path(), self.local_path)
        
        client = GitClient(self.local_path)
        self.assertEqual(client.get_path(), self.local_path)
        
        client = GitClient(self.local_path)
        self.assertEqual(client.get_path(), self.local_path)
        
        client = GitClient(self.local_path)
        self.assertEqual(client.get_path(), self.local_path)
    def test_fast_forward(self):
        from vcstools.git import GitClient
        
        url = self.remote_path
        client = GitClient(self.local_path)
        self.assertTrue(client.checkout(url, "master"))
        subprocess.check_call(["git", "reset", "--hard", "test_tag"], cwd=self.local_path)
        self.assertTrue(client.update())

    def test_fast_forward_simple_ref(self):
        from vcstools.git import GitClient
        
        url = self.remote_path
        client = GitClient(self.local_path)
        self.assertTrue(client.checkout(url, "master"))
        subprocess.check_call(["git", "reset", "--hard", "test_tag"], cwd=self.local_path)
        # replace "refs/head/master" with just "master"
        subprocess.check_call(["git", "config", "--replace-all", "branch.master.merge", "master"], cwd=self.local_path)
        
        self.assertTrue(client.get_branch_parent() is not None)
        
        GitClientTestSetups.setUpClass()
        client.checkout(self.remote_path)
    @classmethod
    def setUpClass(self):
        GitClientTestSetups.setUpClass()
        
        client = GitClient(self.local_path)
        client.checkout(self.remote_path, self.readonly_version)
        subprocess.check_call(["rm", "deleted-fs.txt"], cwd=self.local_path)
        subprocess.check_call(["git", "rm", "deleted.txt"], cwd=self.local_path)
        f = io.open(os.path.join(self.local_path, "modified.txt"), 'a')
        f = io.open(os.path.join(self.local_path, "modified-fs.txt"), 'a')
        subprocess.check_call(["git", "add", "modified.txt"], cwd=self.local_path)
        f = io.open(os.path.join(self.local_path, "added-fs.txt"), 'w')
        f = io.open(os.path.join(self.local_path, "added.txt"), 'w')
        subprocess.check_call(["git", "add", "added.txt"], cwd=self.local_path)
    def tearDown(self):
        pass
        
        client = GitClient(self.local_path)
        client = GitClient(self.local_path)
        self.assertEquals('diff --git ros/added.txt ros/added.txt\nnew file mode 100644\nindex 0000000..454f6b3\n--- /dev/null\n+++ ros/added.txt\n@@ -0,0 +1 @@\n+0123456789abcdef\n\\ No newline at end of file\ndiff --git ros/deleted-fs.txt ros/deleted-fs.txt\ndeleted file mode 100644\nindex e69de29..0000000\ndiff --git ros/deleted.txt ros/deleted.txt\ndeleted file mode 100644\nindex e69de29..0000000\ndiff --git ros/modified-fs.txt ros/modified-fs.txt\nindex e69de29..454f6b3 100644\n--- ros/modified-fs.txt\n+++ ros/modified-fs.txt\n@@ -0,0 +1 @@\n+0123456789abcdef\n\\ No newline at end of file\ndiff --git ros/modified.txt ros/modified.txt\nindex e69de29..454f6b3 100644\n--- ros/modified.txt\n+++ ros/modified.txt\n@@ -0,0 +1 @@\n+0123456789abcdef\n\\ No newline at end of file\n', client.get_diff(basepath=os.path.dirname(self.local_path)))
        client = GitClient(self.local_path)
        client = GitClient(self.local_path)
        self.assertEquals('A  ros/added.txt\n D ros/deleted-fs.txt\nD  ros/deleted.txt\n M ros/modified-fs.txt\nM  ros/modified.txt\n', client.get_status(basepath=os.path.dirname(self.local_path)))
        client = GitClient(self.local_path)