from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.selectioncontrol import MDSwitch


class CoalApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        root = BoxLayout(orientation="vertical")

        # ================= TOP BAR =================
        self.toolbar = MDTopAppBar(
            title="Coal Business Calculator",
            elevation=10,
            right_action_items=[["theme-light-dark", lambda x: self.toggle_theme()]],
        )

        root.add_widget(self.toolbar)

        scroll = ScrollView()
        content = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20,
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter("height"))

        # =====================================================
        # ================= ENERGY CONVERTER ==================
        # =====================================================

        energy_card = MDCard(
            orientation="vertical",
            padding=20,
            spacing=20,
            size_hint=(1, None),
            height=dp(300),
            elevation=8,
            radius=[20]
        )

        self.gcv_input = MDTextField(
            hint_text="GCV (kcal/kg)",
            mode="rectangle",
            input_filter="float"
        )

        self.ncv_label = MDLabel(
            text="NCV result will appear here",
            halign="center",
            theme_text_color="Secondary"
        )

        convert_btn = MDRaisedButton(
            text="CONVERT TO NCV",
            pos_hint={"center_x": 0.5}
        )
        convert_btn.bind(on_release=self.convert_energy)

        energy_card.add_widget(self.gcv_input)
        energy_card.add_widget(convert_btn)
        energy_card.add_widget(self.ncv_label)

        content.add_widget(energy_card)

        # =====================================================
        # ================= MARGIN CALCULATOR =================
        # =====================================================

        margin_card = MDCard(
            orientation="vertical",
            padding=20,
            spacing=20,
            size_hint=(1, None),
            height=dp(350),
            elevation=8,
            radius=[20]
        )

        self.buy_price = MDTextField(
            hint_text="Buy Price per Ton",
            mode="rectangle",
            input_filter="float"
        )

        self.sell_price = MDTextField(
            hint_text="Sell Price per Ton",
            mode="rectangle",
            input_filter="float"
        )

        self.margin_label = MDLabel(
            text="Margin result will appear here",
            halign="center",
            theme_text_color="Secondary"
        )

        margin_btn = MDRaisedButton(
            text="CALCULATE MARGIN",
            pos_hint={"center_x": 0.5}
        )
        margin_btn.bind(on_release=self.calculate_margin)

        margin_card.add_widget(self.buy_price)
        margin_card.add_widget(self.sell_price)
        margin_card.add_widget(margin_btn)
        margin_card.add_widget(self.margin_label)

        content.add_widget(margin_card)

        # =====================================================
        # ================= PROFIT SIMULATION =================
        # =====================================================

        profit_card = MDCard(
            orientation="vertical",
            padding=20,
            spacing=20,
            size_hint=(1, None),
            height=dp(400),
            elevation=8,
            radius=[20]
        )

        self.volume_input = MDTextField(
            hint_text="Volume (MT)",
            mode="rectangle",
            input_filter="float"
        )

        self.cif_input = MDTextField(
            hint_text="Selling Price (CIF per Ton)",
            mode="rectangle",
            input_filter="float"
        )

        self.cost_input = MDTextField(
            hint_text="Total Cost per Ton",
            mode="rectangle",
            input_filter="float"
        )

        self.profit_label = MDLabel(
            text="Profit result will appear here",
            halign="center",
            theme_text_color="Secondary"
        )

        profit_btn = MDRaisedButton(
            text="CALCULATE PROFIT",
            pos_hint={"center_x": 0.5}
        )
        profit_btn.bind(on_release=self.calculate_profit)

        profit_card.add_widget(self.volume_input)
        profit_card.add_widget(self.cif_input)
        profit_card.add_widget(self.cost_input)
        profit_card.add_widget(profit_btn)
        profit_card.add_widget(self.profit_label)

        content.add_widget(profit_card)

        scroll.add_widget(content)
        root.add_widget(scroll)

        return root

    # ================= ENERGY =================
    def convert_energy(self, instance):
        try:
            gcv = float(self.gcv_input.text)
            ncv = gcv - 150  # estimasi rata-rata selisih
            self.ncv_label.text = f"Estimated NCV ≈ {ncv:,.2f} kcal/kg"
        except:
            self.ncv_label.text = "Invalid input"

    # ================= MARGIN =================
    def calculate_margin(self, instance):
        try:
            buy = float(self.buy_price.text)
            sell = float(self.sell_price.text)
            margin = sell - buy
            percent = (margin / buy) * 100
            self.margin_label.text = (
                f"Margin ≈ {margin:,.2f}\n"
                f"Profit % ≈ {percent:.2f}%"
            )
        except:
            self.margin_label.text = "Invalid input"

    # ================= PROFIT =================
    def calculate_profit(self, instance):
        try:
            volume = float(self.volume_input.text)
            cif = float(self.cif_input.text)
            cost = float(self.cost_input.text)

            revenue = volume * cif
            total_cost = volume * cost
            profit = revenue - total_cost

            self.profit_label.text = (
                f"Revenue ≈ {revenue:,.2f}\n"
                f"Total Cost ≈ {total_cost:,.2f}\n"
                f"Net Profit ≈ {profit:,.2f}"
            )
        except:
            self.profit_label.text = "Invalid input"

    # ================= DARK MODE =================
    def toggle_theme(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


CoalApp().run()