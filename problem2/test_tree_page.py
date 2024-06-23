class TestRemovalNodes():
    # не забываем передать первым аргументом self                       
    def test_tree_node_removes(self, browser):
        link = "http://target"
        page = TreePage(browser,link)
        page.open()
        page.delete_child_node()
        page.shouldn_not_see_deleted_element()

    def test_delete_group_node(self,browser):
        link = "http://target"
        page = TreePage(browser, link)
        page.open()
        page.delete_group_node()
        page.shouldn_not_see_deleted_elements_children()
        
    ...