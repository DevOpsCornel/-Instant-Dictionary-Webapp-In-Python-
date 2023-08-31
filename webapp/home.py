import justpy as jp

from webapp import layout


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home Page", classes="text-4xl m-2")
        jp.Div(a=div, text="""It is a long established fact
         that a reader will be distracted by the readable
         content of a page when looking at its layout. """,
               classes="text-lg")
        return wp

