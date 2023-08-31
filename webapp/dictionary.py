import justpy as jp
import definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(self, req):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get definition of any English word instantly as you type them", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        output_div = jp.Div(a=div, classes="m2 p-2 text=lg border-2 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type your word here ...", outputdiv=output_div,
                             classes="m-2 bg-gray-200 border-2 border-gray-20 w-64 focus:by-white focus:outline-none"
                                     "focus:bordr-purple-500 py-2 px-4")
        input_box.on('input', self.get_definition)

        print(self, req)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
