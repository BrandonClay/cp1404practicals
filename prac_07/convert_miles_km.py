from kivy.app import App
from kivy.lang import Builder
KM_PER_MILE = 1.6


class MilesToKilometres(App):

    def build(self):
        self.title = "Convert Miles to kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.handle_inputs()
        result = value * KM_PER_MILE
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.handle_inputs() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def handle_inputs(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometres().run()