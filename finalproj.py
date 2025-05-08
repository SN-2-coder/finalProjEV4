import flet as ft

def main(page:ft.page):
    page.title = "Sky Map"
    star = ft.image(src="star.png", width=20,height=20)
    text= ft.Text("SKY MAP", size=30, color="blue", font_family="Georgia", italic=True, weight=ft.FontWeight.W_200)
    page.add(ft.Row([star,text,star],ft.MainAxisAlignment.CENTER),ft.Divider())
    
ft.app(target = main,assets_dir="assets")
