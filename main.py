from flet import *
import speech_recognition as sr
import Speech_SOS
import pywhatkit
import datetime
import math
import threading
import requests

nums = []
def what():
    global nums
    for num in nums:
        time = datetime.datetime.now()
        hr = time.hour
        mnt = time.minute
        pywhatkit.sendwhatmsg(num, 'Hi There', hr, mnt+1, 20, True, 5 )

#main page

#def handle_shake(event):
    #threading.Thread(target=prime).start()

def record_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            return MyText
    except sr.RequestError as e:
        print("Could not request results;{0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
    return None


def output_text(text):
    with open("output.txt", "w") as f:
        f.write(text + "\n")


def prime():
    #shake = ShakeDetector(on_shake=handle_shake)
    #page.add(shake)

    text = record_text()
    if text:
        output_text(text)
        print("wrote text")

        sos = "help is required"
        sos1= "i am in danger"
        sos2= "help help help"
        with open('output.txt') as file:
            text = file.read()
            if sos in text or sos1 in text or sos2 in text:
                Speech_SOS.help_sos()
                what()

    #page.remove(shake)

def main(page: Page):

    login = Container(
        width=400,
        height=850,
        bgcolor="#fffffff",
        border_radius=10,
        content=Column(
            width=320,
            controls=[
                Container(
                    width=300,
                    margin=margin.only(left=110, right=10, top=10),
                    content=Text(
                        "Login",
                        size=30,
                        color="#000000",
                        weight='w700'

                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=20),
                    content=Text(
                        "Please enter your information below in order to login to your account",
                        size=15,
                        color="#000000",
                        weight='w700',
                        text_align="center"
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=10, top=30),
                    content=Column(
                        controls=[
                            Text(
                                "Username",
                                size=14,
                                color="#000000"
                            ),

                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=5),
                    content=Column(
                        controls=[
                            Text(
                                "Phone Number",
                                size=14,
                                color="#000000"
                            ),

                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=5),
                    content=Column(
                        controls=[
                            Text(
                                "Email",
                                size=14,
                                color="#000000"
                            ),

                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=5),
                    content=Column(
                        controls=[
                            Text(
                                "Blood group",
                                size=14,
                                color="#000000"
                            ),

                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20, right=20, top=20),
                    content=Column(

                    ),
                ),

            ]
        ),
    )


    def close_dlg(e):
        log_dlg.open = False
        page.update()

    def log_click(e):
        if U1.value and P1.value:
            page.client_storage.set("LU1", U1.value)
            page.client_storage.set("LP1", P1.value)
            page.client_storage.set("LE1", E1.value)
            page.client_storage.set("LB1", B1.value)
            page.dialog = log_dlg
            log_dlg.open = True
            page.update()
            page.window.go("/")  # Redirect to home page
            #close_dlg()


        else:
            if not U1.value:
                U1.error_text = "Please enter your username!!"

            if not P1.value:
                P1.error_text = "Please enter your password!!"
    page.update()
    us1=page.client_storage.get("LU1")
    ph1=page.client_storage.get("LP1")
    em1=page.client_storage.get("LE1")
    bg1=page.client_storage.get("LB1")







    # Rest of the code remains the same
    log_dlg = AlertDialog(
        modal=True,
        title=Text("Login Success!!"),
        actions=[
            TextButton("OK", on_click=close_dlg)
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    U1 = TextField(
        text_style=TextStyle(
            color="#000000",

        ),
        border_radius=15,
        border_color=colors.BLACK,
        focused_border_color=colors.ORANGE_700,

    )

    P1 = TextField(
        text_style=TextStyle(
            color="#000000",

        ),
        border_radius=15,
        border_color=colors.BLACK,
        focused_border_color=colors.ORANGE_700,

    )
    E1 = TextField(
        text_style=TextStyle(
            color="#000000",

        ),
        border_radius=15,
        border_color=colors.BLACK,
        focused_border_color=colors.ORANGE_700,

    )
    B1 = Dropdown(
        options=[
            dropdown.Option("A+"),
            dropdown.Option("B+"),
            dropdown.Option("AB+"),
            dropdown.Option("O+"),
            dropdown.Option("A-"),
            dropdown.Option("B-"),
            dropdown.Option("AB-"),
            dropdown.Option("O-"),

        ],
        border_radius=15,
        border_color=colors.BLACK,
        focused_border_color=colors.ORANGE_700,

    )
    tb=TextButton(
        "Login",
        width=300,
        height=50,
        style=ButtonStyle(
            color="#ffffff",
            bgcolor=colors.ORANGE_700,
            shape={
                MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                MaterialState.HOVERED: RoundedRectangleBorder(radius=5),
            },
            padding=20,

        ),
        on_click=log_click
    )


    login.content.controls[6].content.controls.append(tb),
    login.content.controls[2].content.controls.append(U1),
    login.content.controls[3].content.controls.append(P1),
    login.content.controls[4].content.controls.append(E1),
    login.content.controls[5].content.controls.append(B1),

    BG = '#041955'
    FWG = '#ffffff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5,0.5],
                    colors=['#00000000', PINK]
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                            alignment='center',
                            controls=[
                                Container(padding=padding.all(5),
                                          bgcolor=BG,
                                          width=90, height=90,
                                          border_radius=50,
                                          content=Container(bgcolor=FG,
                                                            height=80, width=80,
                                                            border_radius=40,
                                                            content=CircleAvatar(opacity=0.8,
                                                                                 foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                                                                                 )
                                                            )
                                          )
                    ]
                )
            )
        ]
    )


    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        page_2.controls[0].border_radius = border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right
        )
        page_2.update()

    create_task_view = Container(
        width=400,
        height=900,
        bgcolor="cyan",
        border_radius=36,
        padding=padding.only(left=15,top=18),
        content=Column(
            controls=[
                Row(
                    controls=[
                    Container(
                                  padding=padding.only(top=18,left=12),
                                  content=Icon(icons.ARROW_BACK_ROUNDED, size=30, color='white'),
                                  on_click=lambda _: page.go('/'),
                              ),
                    ]
                ),
                Container(height=15),
                Text("Enter Your Emergency Contacts", size=30, font_family='poppins', weight='bold'),
                Container(height=20),
                Column(

                )
            ]
        )
    )

    DLG = AlertDialog(
        title=Text('Added!!')
    )

    def success(e):
        dlg.open = False

        page.dialog = DLG
        DLG.open = True

        page.client_storage.set("ATY", txt_num.value)
        if txt_num1.value:
            page.client_storage.set("ATY1", txt_num1.value)
        if txt_num2.value:
            page.client_storage.set("ATY2", txt_num2.value)
        page.update()

    def fail(e):
        dlg.open = False
        page.update()

    dlg = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to add all those contacts?"),
        actions=[
            TextButton("Yes", on_click=success),
            TextButton("No", on_click=fail),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_modal(e):
        page.dialog = dlg
        dlg.open = True
        page.update()


    def btn_click(e):
        if not txt_num.value:
            txt_num.error_text = "Please enter your emergency contact!!"
            page.update()
        else:
            open_dlg_modal(e)
            page.update()
        page.update()



    txt_num = TextField(label="Contact 1*", width=369)
    txt_num1= TextField(label="Contact 2", width=369)
    txt_num2= TextField(label="Contact 3", width=369)
    create_task_view.content.controls[4].controls.append(txt_num)
    create_task_view.content.controls[4].controls.append(Container(height=20))
    create_task_view.content.controls[4].controls.append(txt_num1)
    create_task_view.content.controls[4].controls.append(Container(height=20))
    create_task_view.content.controls[4].controls.append(txt_num2)
    create_task_view.content.controls[4].controls.append(Container(height=10))
    create_task_view.content.controls[4].controls.append(ElevatedButton('Add Contact', on_click=btn_click))

    def fail_rm(e):
        remove_modal.open = False

        page.update()
    def fail_rm1(e):
        remove_modal1.open = False

        page.update()
    def fail_rm2(e):
        remove_modal2.open = False

        page.update()

    def suc_rm(e):
        remove_modal.open = False
        page.dialog = remove
        remove.open = True
        page.client_storage.remove('ATY')
        page.update()
    def suc_rm1(e):
        remove_modal1.open = False
        page.dialog = remove
        remove.open = True
        page.client_storage.remove('ATY1')
        page.update()
    def suc_rm2(e):
        remove_modal2.open = False
        page.dialog = remove
        remove.open = True
        page.client_storage.remove('ATY2')
        page.update()


    remove_modal = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to delete this contact?"),
        actions=[
            TextButton("Yes", on_click=suc_rm),
            TextButton("No", on_click=fail_rm),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    remove_modal1 = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to delete this contact?"),
        actions=[
            TextButton("Yes", on_click=suc_rm1),
            TextButton("No", on_click=fail_rm1),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    remove_modal2 = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to delete this contact?"),
        actions=[
            TextButton("Yes", on_click=suc_rm2),
            TextButton("No", on_click=fail_rm2),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    remove = AlertDialog(
        title=Text("Deleted!")
    )

    def open_remove_modal(e):
        page.dialog = remove_modal
        remove_modal.open = True
        page.update()
    def open_remove_modal1(e):
        page.dialog = remove_modal1
        remove_modal1.open = True
        page.update()
    def open_remove_modal2(e):
        page.dialog = remove_modal2
        remove_modal2.open = True
        page.update()

    def rm(e):
        open_remove_modal(e)
        page.update()
    def rm1(e):
        open_remove_modal1(e)
        page.update()
    def rm2(e):
        open_remove_modal2(e)
        page.update()

    global num,num1,num2
    num=page.client_storage.get('ATY')
    num1=page.client_storage.get('ATY1')
    num2=page.client_storage.get('ATY2')

    if num!=None:
        nums.append('+91'+num)
    if num1!=None:
        nums.append('+91'+num1)
    if num2!=None:
        nums.append('+91'+num2)

    em_con = Container(
        width=400,
        height=900,
        bgcolor="cyan",
        border_radius=36,
        padding=padding.only(top=18, left=18),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                                  padding=padding.only(top=18,left=12),
                                  content=Icon(icons.ARROW_BACK_ROUNDED, size=30, color='white'),
                                  on_click=lambda _: page.go('/'),
                                  ),
                    ]
                ),
                Container(
                    padding=padding.only(top=18,left=18,right=18),
                content =Column(
                controls=[
                    Text('Emergency Contacts', size=36, weight='bold', font_family='Consolas'),
                    Container(height=30),
                    Row(
                        controls=[
                            Icon(icons.QUICK_CONTACTS_DIALER_OUTLINED),
                            Text('Contact 1', size=28,)
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Text(f"{num}", color='black', size=18),
                            Container(
                                Icon(icons.DELETE_FOREVER, size=18),
                                on_click=rm
                            )
                        ]
                    ),
                    Container(height=20),
                    Row(
                        controls=[
                            Icon(icons.QUICK_CONTACTS_DIALER_OUTLINED),
                            Text('Contact 2', size=25,)
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Text(f"{num1}", color='black', size=18),
                            Container(
                                Icon(icons.DELETE_FOREVER, size=18),
                               on_click=rm1
                            )
                        ]
                    ),
                    Container(height=20),
                    Row(
                        controls=[
                            Icon(icons.QUICK_CONTACTS_DIALER_OUTLINED),
                            Text('Contact 3', size=22,)
                        ]
                    ),
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Text(f"{num2}", color='black', size=18),
                            Container(
                                Icon(icons.DELETE_FOREVER, size=18),
                                on_click=rm2
                            )
                        ]
                    ),
                    Container(height=20),
                    ],
                    alignment = MainAxisAlignment.CENTER,
                )
                )
            ]
        )
    )
    tasks = Column(
        height=336,
        scroll='auto',
    )
    tasks.controls.append(
        Container(
            height=120,
            width=400,
            border_radius=36,
            bgcolor=BG,
            padding=padding.only(top=15,left=40,),
            content=Row(
                controls=[
                    Icon(icons.CONTACT_EMERGENCY_OUTLINED, color=PINK),
                    Text('Emergency Contacts', color=FWG)
                ]
            ),
            on_click= lambda  _: page.go('/emc'),
        )
    )


    def get_location(e):
        page.client.get_location(on_success=show_location, on_error=show_error)

    def show_location(location):
        latitude = location.latitude
        longitude = longitude = location.longitude
        page.update()

        # Optionally, you can use external APIs to get more information about the location
        url = f"https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key=YOUR_API_KEY"
        response = requests.get(url)
        data = response.json()

        # Extract relevant information from the API response
        city = data["results"][0]["components"]["city"]
        country = data["results"][0]["components"]["country"]

        display_location.value = f"Latitude: {latitude}\nLongitude: {longitude}\nCity: {city}\nCountry: {country}"
        page.update()

    def show_error(error):
        display_location.value = f"Error: {error}"
        page.update()

    display_location = Text()

    tasks.controls.append(
        Container(
            height=120,
            width=400,
            border_radius=36,
            bgcolor=BG,
            padding=padding.only(top=15, left=40, ),
            content=Row(
                controls=[
                    Icon(icons.EMERGENCY_SHARE_OUTLINED, color=PINK),
                    Text('Location Tracking', color=FWG),
                    display_location
                ]
            ),
            on_click=get_location,

        )
    )

    def dial_100(e):
        page.window.open_url("tel:100")

    tasks.controls.append(
        Container(
            height=120,
            width=400,
            border_radius=36,
            bgcolor=BG,
            padding=padding.only(top=15,left=40,),
            content=Row(
                controls=[
                    Icon(icons.LOCAL_POLICE_OUTLINED, color=PINK),
                    Text('Dial 100', color=FWG)
                ]
            ),
            on_click=dial_100
        )
    )
    categories_card = Row(
        scroll='auto'
    )

    i=len(nums)
    fill = math.ceil((i/3)*160)
    profile  = []
    if us1!=None:
        profile.append(us1)
    if ph1!=None:
        profile.append(us1)
    if bg1!=None:
        profile.append(us1)
    if em1!=None:
        profile.append(us1)
    j = len(profile)
    categories = [f'{i}/3', f'{j}/4']
    categories_card.controls.append(
            Container(
                bgcolor=BG,
                height=110,
                width=170,
                border_radius=18,
                padding=15,
                content=Column(
                    controls=[
                        Text('No.of Emergency\ncontacts', color=FWG),
                        Text(categories[0],color=FWG),
                        Container(
                            width=160,
                            height=5,
                            bgcolor=PINK,
                            border_radius=20,
                            padding=padding.only(left=fill),
                            content=Container(
                                bgcolor='#000099',
                            ),
                        )
                    ]
                )
            )
        )
    categories_card.controls.append(
        Container(
            bgcolor=BG,
            height=110,
            width=170,
            border_radius=18,
            padding=15,
            content=Column(
                controls=[
                    Text('Profile\nCompletion', color=FWG),
                    Text(categories[1], color=FWG),
                    Container(
                        width=160,
                        height=5,
                        bgcolor=PINK,
                        border_radius=20,
                        padding=padding.only(left=j*40),
                        content=Container(
                            bgcolor='#000099',
                        ),
                    )
                ]
            )
        )
    )


    con_1 = Container(
                padding=padding.only(left=120),
                content=Container(
                    height=135,
                    width=135,
                    border_radius=360,
                    bgcolor=BG,
                    padding=padding.only(top=30,left=48,),
                    content=Column(
                        controls=[
                            Icon(icons.FIBER_SMART_RECORD_ROUNDED, color=PINK, size=39),
                            Text('ATY',color=FWG, size=19, weight='bold', font_family='poppins')
                        ]
                    )
                ),
                on_click=lambda _:prime()
            )

    note = Container(
        width=400,
        height=900,
        bgcolor="cyan",
        border_radius=36,
        padding=padding.only(top=18, left=18),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            padding=padding.only(top=18, left=12),
                            content=Container(
                                Row(
                                   controls=[
                                       Icon(icons.ARROW_BACK_ROUNDED, size=30, color='white'),
                                       Text('Notifications', size=27, color='white')
                                   ],
                                )
                            ),
                            on_click=lambda _: page.go('/'),
                        ),
                    ]
                ),
                Container(height=360),
                Container(
                    padding=padding.only(left=99),
                    content=Text('No New Notifications', size=15)
                )
            ]
        ),
    )

    first_page_contents = Container(
        content = Column(
            controls = [
                Row(
                    alignment='spaceBetween',
                    controls = [
                        Container(
                            on_click = lambda e: shrink(e),
                            content=Icon(
                                icons.MENU, color=FWG)),
                        Container(
                            on_click =lambda _:page.go('/noti'),
                            content=Icon(icons.NOTIFICATIONS_OUTLINED, color=FWG),
                        ),
                    ]
                ),
                Text(
                    value=f'What\'s up, {us1}!',color=FWG,
                ),
                Text(
                    value='CATEGORIES', color=FWG,
                ),
                Container(
                    padding=padding.only(top=10, bottom=20, ),
                    content = categories_card
                ),
                con_1,
                Text('Available services:', color=FWG),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(bottom=2,right=20,
                            icon = icons.ADD, on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ],
        ),
    )

    def logout(e):
        page.client_storage.clear()
        page.update()
        page.window.go("/log")


    page_1 = Container(
        width=400,
        height=900,
        bgcolor=BG,
        border_radius=36,
        padding=padding.only(left=50, right=200, top=60),
        content=Column(
            controls=[
                Row(alignment='end',controls=[
                    Container(border_radius=25,
                              padding=padding.only(left=12),
                              height=50,
                              width=50,
                              border=border.all(color='white', width=2),
                              on_click=lambda e: restore(e),
                              content=Text('<', color=FWG, size=30)
                        )
                    ]
                ),
                Container(height=20),
                circle,
                Text(f'{us1}', color= PINK,size=32,weight='bold'),
                Container(height=20),
                Row(
                    controls=[
                        Icon(icons.LOCAL_PHONE_OUTLINED, color=PINK),
                        Text(f'+91{ph1}',color=FWG)
                    ]
                ),
                Container(height=10),
                Row(
                    controls=[
                        Icon(icons.EMAIL, color=PINK),
                        Text(f'{em1}', color=FWG)
                    ]
                ),
                Container(height=10),
                Row(
                    controls=[
                        Icon(icons.BLOODTYPE, color=PINK),
                        Text(f'{bg1}', color=FWG)
                    ]
                ),
                Container(height=210),
                Row(
                    controls=[
                        Icon(icons.LOGOUT, color=PINK),
                        TextButton(
                            'Logout',
                            on_click=logout
                        ),
                    ]
                ),
            ]
        )
    )
    page_2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=900,
                bgcolor=FG,
                border_radius=36,
                animate = animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale = animation.Animation(400, curve='decelerate'),
                padding = padding.only(top=50,left=20,right=20,bottom=5),
                content = Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width = 400,
        height= 850,
        bgcolor = BG,
        border_radius=36,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )

    pages = {
        '/log': View(
            route='/log',
            controls=[
                login
            ],
        ),
        '/': View(
            route="/",
            controls=[
                container
            ],
        ),
        '/create_task': View(
            route='/create_task',
            controls=[
                create_task_view
            ],
        ),
        '/emc': View(
            route='/emc',
            controls=[
                em_con
            ],
        ),
        '/noti': View(
            route='/noti',
            controls=[
                note
            ],
        ),
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    if page.client_storage.contains_key("LU1") and page.client_storage.contains_key("LP1"):
        page.add(container)
    else:
        page.add(login)
    page.on_route_change=route_change
    page.go(page.route)
app(target=main, assets_dir='')