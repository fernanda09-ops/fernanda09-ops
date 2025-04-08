import flet as ft

def main(page: ft.Page):

    page.window.width = 1000
    page.window.height = 600
    page.window_center()
    page.padding = 0
    page.window_resizable = False
    page.window.title_bar_hidden = True
    page.bgcolor= "#D7D7D9"
    
    te = '01'


    c1 = ft.Row([
    
        ft.Container(bgcolor='#0D0D0D', width=150, height=591, padding=10, border_radius=5,           
            content= ft.Column([
                        

                            ft.Container(content =ft.Row(controls=[
                                            
                            ft.IconButton(icon='Home', icon_color="#F2F2F2", on_click=lambda e: sair()),
                            ft.Text("Inicio", color='#F2F2F2')
                            
                            ])),

                            ft.Container(content =ft.Row(controls=[
                                            
                            ft.IconButton(icon=ft.icons.APP_REGISTRATION, icon_color="#F2F2F2", on_click=lambda e: sair()),
                            ft.Text("Registrar", color='#F2F2F2')
                            
                            ])),

                            ft.Container(content =ft.Row(controls=[
                                            
                            ft.IconButton(icon=ft.icons.MONETIZATION_ON_ROUNDED, icon_color="#F2F2F2", on_click=lambda e: sair()),
                            ft.Text("Financeiro", color='#F2F2F2')
                            
                            ])),

                            ft.Container(content =ft.Row(controls=[
                                            
                            ft.IconButton(icon=ft.icons.LOGOUT_OUTLINED, icon_color="#F2F2F2", on_click=lambda e: sair()),
                            ft.Text("Sair", color='#F2F2F2')
                            
                            ]))
                        
                        ])
              

                                
        ),

        ft.Container(bgcolor='#F2F2F2', width=812, height=591, border_radius=5, content=
    
                ft.Container(bgcolor='#F2F2F2', width=812, height=200, border_radius=5, 
                                content=
                                ft.DataTable(
                                        columns=[
                                            ft.DataColumn(ft.Text("ID")),
                                            ft.DataColumn(ft.Text("Nome")),
                                            ft.DataColumn(ft.Text("Valor por Hora")),
                                            ft.DataColumn(ft.Text("Categoria")),
                                            ft.DataColumn(ft.Text("Data de Aluguel")),
                                            ft.DataColumn(ft.Text("Horas Contratada")),
                                        ],
                                        rows=[
                                            ft.DataRow(
                                                cells=[
                                                    ft.DataCell(ft.Text(te)),
                                                    ft.DataCell(ft.Text("Escavadeira")),
                                                    ft.DataCell(ft.Text("R$ 160,90")),
                                                    ft.DataCell(ft.Text("Máquina")),
                                                    ft.DataCell(ft.Text("04/06/2025")),
                                                    ft.DataCell(ft.Text("06")),
                                                ],
                                            ),   
                                            
                                        ],
                                            ),
                            ),

        )
    ])

    def sair():

        page.window_close()
        

    page.add(c1)

ft.app(main)
