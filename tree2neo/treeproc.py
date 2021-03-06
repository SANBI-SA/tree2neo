"""
Interface to handle VCF files
"""
import glob
import time


class NewickTree(object):
    """
    Handling Tree processing.
    """

    def __init__(self, history_id, db, tree_dir=None):
        self.tree_dir = tree_dir
        self.db = db
        self.history_id = history_id

    def process(self):
        print("We have the following TREE files in directory ({}):\n".format(
            self.tree_dir))
        for tree_file in glob.glob(self.tree_dir + "/*.nhx"):
            start = time.time()

            # read the file contents
            with open(tree_file) as tree_f:
                data_str = tree_f.read()

            # TODO: Pass Tree File Name in the tool arguments
            tree_file_name = str(tree_file).rsplit('/', 1)[-1]

            # TODO: Let's use the file name for now
            self.db.create_tree_nodes(name=tree_file_name,
                                      data=data_str,
                                      history_id=self.history_id)

            end = time.time()
            print("Processed {} in {}!".format(tree_file_name.upper(),
                                               end - start))
            # time.sleep(2)
