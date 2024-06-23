class TreePage(BasePage):


    def delete_child_node()(self):
        self.find(*Locator.PRODUCT)
        self.click(*Locator.PRODUCT_DEL)
        assert self.is_disappeared(*Locator.PRODUCT), \
        "Product disappearces, but shouldn't!"

    def should_be_succes_message_on_the_product_add(self):
        gr_node_del = self.get_text(*Locator.NODE_GROUPE_DEL)
        self.click(gr_node_del)
        assert childre in self.get_text(*ProductPageLocators.Children), "Childre elements haven't been deleted"
