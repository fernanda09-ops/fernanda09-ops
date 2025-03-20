import flet as ft
import  pessoa
def main (page: ft.Page):
    page.window_center()
    page.window_width = '400'
    page.window_height = '500'
    page.window_resizable = False
    page.window_maximizable = False


    p1= ft.Text(pessoa.pessoa1)
    p2= ft.Text(pessoa.pessoa2)
    p3= ft.Text(pessoa.pessoa3)
    p4= ft.Text(pessoa.pessoa4)
    
    page.add(p1, p2, p3, p4)
ft.app(target=main)
