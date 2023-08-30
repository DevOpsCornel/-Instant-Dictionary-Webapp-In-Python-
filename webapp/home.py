import justpy as jp

class Home:

    path = "/"
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home Page", classes="text-4xl m-2")
        jp.Div(a=div, text="""It is a long established fact
         that a reader will be distracted by the readable
         content of a page when looking at its layout. 
         The point of using Lorem Ipsum is that it
          has a more-or-less normal distribution of letters, 
         as opposed to using 'Content here, content here',
          making it look like readable English. """,
               classes="text-lg")
        return wp

