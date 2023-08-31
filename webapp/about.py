import justpy as jp
from webapp import layout
from webapp import page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page", classes="text-4xl m-2")
        jp.Div(a=div, text="""It is a long established fact
         that a reader will be distracted by the readable
         content of a page when looking at its layout. 
         The point of using Lorem Ipsum is that it
          has a more-or-less normal distribution of letters, 
         as opposed to using 'Content here, content here',
          making it look like readable English. """,
               classes="text-lg")
        return wp
