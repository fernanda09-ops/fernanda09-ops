 ft.Container(

        width=450,
        height=540,
        border_radius= 5,
        padding=30,

         content= ft.Column ([  
        ft.Image (src=f'mulher.png',
        width = 550, height = 300,
        fit = ft.ImageFit.CONTAIN),
        ft.Text('A melhor experiencia para \n o seu login que você teve na vida',
        size=20, 
        color='#ffffff')

    ],alignment=ft.MainAxisAlignment.CENTER,
       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=40
    )
    )
     ])
