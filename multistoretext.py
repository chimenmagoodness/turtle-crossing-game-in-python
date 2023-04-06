from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import OneLineAvatarListItem, MDList
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar

class MultistoreApp(MDApp):

    def build(self):
        screen = MDScreen()

        # create the top toolbar

        toolbar = MDToolbar()
        toolbar.left_action_items = [["menu", lambda x: self.navigation_drawer.set_state("open")]]
        #screen.add_widget(toolbar)

        # create the navigation drawer
        self.navigation_drawer = MDNavigationDrawer()
        stores = [{'name': 'Store 1', 'logo': 'store1.png'}, {'name': 'Store 2', 'logo': 'store2.png'}, {'name': 'Store 3', 'logo': 'store3.png'}]
        for store in stores:
            item = OneLineAvatarListItem(text=store['name'])
            item.add_widget(MDIconButton(icon=store['logo']))
            self.navigation_drawer.add_widget(item)

        # create the main screen layout
        layout = MDBoxLayout(orientation="vertical", spacing=10, padding=10)
        screen.add_widget(layout)

        # create the product list
        products = [{'name': 'Product 1', 'image': 'product1.png', 'price': 9.99},
                    {'name': 'Product 2', 'image': 'product2.png', 'price': 19.99},
                    {'name': 'Product 3', 'image': 'product3.png', 'price': 29.99},
                    {'name': 'Product 4', 'image': 'product4.png', 'price': 39.99}]
        product_list = MDList()
        for product in products:
            item = OneLineAvatarListItem(text=product['name'])
            item.add_widget(MDIconButton(icon=product['image']))
            item.add_widget(MDIconButton(icon='cart', on_release=self.add_to_cart))
            item.secondary_text = "$" + str(product['price'])
            product_list.add_widget(item)
        layout.add_widget(product_list)

        return screen

    def add_to_cart(self, instance):
        # implement cart functionality here
        pass


if __name__ == '__main__':
    MultistoreApp().run()
